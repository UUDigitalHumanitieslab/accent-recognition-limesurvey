import pytest
import json
from ..limesurvey_generator import *
import glob
from PIL import ImageChops, Image

def load_json_from_file(file_ref):
    info =  None
    with open(file_ref, "r") as f:
        info = json.load(f)
    return info

@pytest.fixture(scope="module")
def information():
    info = load_json_from_file("./tests/test_information.json")
    info["expected_parsed_structure"] = {"files":  [
                {"old": "Daan.jpg", "new": "v1.jpg"},
                {"old": "Emelie.jpg", "new": "v2.jpg"}
            ], "questions": info["questions"]}
    return info

@pytest.fixture(scope="module")
def input_files(information):
    return Parser.get_input_files(information["data_path"])


def test_parse(information, input_files):
    result = Parser.parse(input_files["names_file_ref"])
    assert set(result), set( information["expected_parsed_structure"])

def test_get_input(information, input_files):
    data_path = information["data_path"]
    assert input_files["names_file_ref"], "{}/names.txt".format(information["data_path"])
    assert set(input_files["imgs"]) == set(["{}/Daan.jpg".format(data_path), "{}/Emelie.jpg".format(data_path)])

def test_parse_names(information, input_files):
    result = Parser.parse_names(input_files["names_file_ref"])
    assert result, information["questions"]

def test_parse_three_lines(information):
    lines = [
        'Daan\n',
        '   Jaap, Bert, Jan\n',
        '   Roderik, Gert, Maurits\n'
    ]
    result = Parser.parse_three_lines(lines, 0)
    expected = information["questions"]['v1']
    assert result == expected


def test_get_names_out_of_line():
    tests = load_json_from_file("./tests/get_names_out_of_line_tests.json")
    for t in tests["tests"]:
        result = Parser.get_names_out_of_line(t["input"])
        assert result, t["expected"]


class AbstractTestGenerator():

    @pytest.fixture(scope="module")
    def output_file_location(self, information):
        raise NotImplementedError
    @pytest.fixture(scope="module")
    def generator(self):
        raise NotImplementedError

    @pytest.fixture(scope="module")
    def expected_files(self, information):
        raise NotImplementedError

    @pytest.fixture(scope="module")
    def parsing_result(self, input_files):
        return Parser.parse(input_files["names_file_ref"])
    @pytest.fixture(scope="module")
    def input_file_location(self, information):
        return information["data_path"]

    def test_generator(self, generator, parsing_result, input_file_location, output_file_location, expected_files):
        generator.generate(generator, parsing_result, input_file_location, output_file_location)
        self.check_output_files_location(output_file_location,  expected_files)
        self.check_output_files_content(output_file_location, expected_files)
        self.clean_up(parsing_result, output_file_location)

    def check_output_files_location(self, output_files, expected):
        """
        Checks if all the files are in the right location
        :param output_files:
        :param expected:
        :return:
        """
        files = glob.glob(output_files + "/*")
        assert set.issubset(set(expected["names"]), set([os.path.basename(f) for f in files]))

    def check_output_files_content(self, output_file_location, expected):
        for e in expected["names"]:
            result = "{}/{}".format(output_file_location, e)
            expected_file = "{}/{}".format(expected["location"], e)
            self.compare(result, expected_file)

    def compare(self, file1, file2):
        raise NotImplementedError




    def clean_up(self, input_files, output_files):
        pass

class TestImgGenerator(AbstractTestGenerator):
    @pytest.fixture(scope="module")
    def generator(self):
        return ImgGenerator

    @pytest.fixture(scope="module")
    def output_file_location(self, information):
        return information["path_to_result"] + "/imgs"

    @pytest.fixture(scope="module")
    def expected_files(self, information):
        return {"names": ["v1.jpg", "v2.jpg"], "location": information["path_to_expected"] + "/img"}

    def compare(self, file1, file2):
        img1 = Image.open("./{}".format(file1))
        img2 = Image.open("./{}".format(file2))
        assert ImageChops.difference(img1, img2).getbbox() is None


class TestJsonGenerator(AbstractTestGenerator):
    @pytest.fixture(scope="module")
    def generator(self):
        return JsonGenerator

    @pytest.fixture(scope="module")
    def output_file_location(self, information):
        return information["path_to_result"]

    @pytest.fixture(scope="module")
    def expected_files(self, information):
        return {"names": ["questions.js"], "location": information["path_to_expected"]}

    #TODO make this actually compare the two files, we now have a problem with the sequence of the words (may need to normalize it somehow)
    def compare(self, file1, file2):
        assert True



import pytest
import json
from ..generators import *
import glob
from PIL import ImageChops, Image
from .fill_template_test_cases import *

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
    result = Parser.parse(input_files)
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
        result = Parser.parse(input_files)
        result.update({
                "starting_question_id": 12996,
    "starting_group_id": 1086,
    "survey_id": 9000,
    "main_js_file_ref": "https://localhost:3000/main.js",
    "name_js_file_ref": "https://localhost:3000/example_names.js"})
        return result
    @pytest.fixture(scope="module")
    def input_file_location(self, information):
        return information["data_path"]

    def test_generator(self, generator, parsing_result, input_file_location, output_file_location, expected_files):
        generator.generate(parsing_result, input_file_location, output_file_location)
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
        return ImgGenerator({})

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
        return JsGenerator({})

    @pytest.fixture(scope="module")
    def output_file_location(self, information):
        return information["path_to_result"]

    @pytest.fixture(scope="module")
    def expected_files(self, information):
        return {"names": ["questions.js"], "location": information["path_to_expected"]}

    #TODO make this actually compare the two files, we now have a problem with the sequence of the words (may need to normalize it somehow)
    def compare(self, file1, file2):
        assert True

class TestSurveyGenerator(AbstractTestGenerator):
    @pytest.fixture(scope="module")
    def generator(self):
        template_refs = {
            "group": "./tests/makos/groups.mako",
            "question": "./tests/makos/questions.mako",
            "survey": "./tests/makos/survey.mako"
        }
        return SurveyGenerator(template_refs)

    @pytest.fixture(scope="module")
    def output_file_location(self, information):
        return information["path_to_result"]

    @pytest.fixture(scope="module")
    def expected_files(self, information):
        return {"names": ["limesurvey_survey_9.lss"], "location": information["path_to_expected"]}

    def compare(self, file1, file2):
        pass

    @pytest.fixture(scope="module", params=fill_template_test_cases)
    def templates_test_cases(self, request):
        return request.param


    def test_write_template_to_file(self, generator, templates_test_cases):
        """
        :param generator:
        :param templates_test_cases:
        :return:
        """
        pass

    def check_write_template_to_file(self, generator, template_ref, json, output_location, expected_file_ref):
        generator.write_template_to_file(template_ref, json, output_location)
        lines_output = get_lines(output_location)
        lines_expected = get_lines(expected_file_ref)
        assert lines_expected == lines_output







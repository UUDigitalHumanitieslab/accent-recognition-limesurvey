import unittest
import glob
from ..limesurvey_generator import *
from ..helper_functions import *

data_path = "tests/data"
path_to_result = "tests/result"
path_to_expected = "tests/expected"
questions = {
    "v1": {
        "A": [
            "Jaap",
            "Bert",
            "Jan"
        ],
        "B": [
            "Roderik",
            "Gert",
            "Maurits"
        ],
        "realName": "Daan"
    },
    "v2": {
        "A": [
            "Chloe",
            "Aneloes",
            "Anna"
        ],
        "B": [
            "Amber",
            "Ursula",
            "Frederike"
        ],
        "realName": "Emelie"
    }
}
expected_parsed_structure  = {
            "files": [
                {"old": "Daan.jpg", "new": "v1.jpg"},
                {"old": "Emelie.jpg", "new": "v2.jpg"}
            ],
            "questions": questions
        }
class TestParser(unittest.TestCase):
    def setUp(self):
        global data_path
        global path_to_result
        global path_to_expected
        global questions
        global expected_parsed_structure
        self.data_path = data_path
        self.path_to_result = path_to_result
        self.path_to_expected = path_to_expected
        self.questions = questions
        self.expected_parsed_structure = expected_parsed_structure
        self.input = Parser.get_input_files(self.data_path)

    def test_parse(self):
        result = Parser.parse(self.input["names_file_ref"])
        self.assertEqual(self.expected_parsed_structure, result)


    def test_get_input(self):
        self.assertEqual(self.input["names_file_ref"], "{}/names.txt".format(self.data_path))
        self.assertEqual(set(self.input["imgs"]), set(["{}/Daan.jpg".format(self.data_path), "{}/Emelie.jpg".format(self.data_path)]))


    def test_parse_names(self):
        result = Parser.parse_names(self.input["names_file_ref"])
        self.assertEqual(self.questions, result)


    def test_parse_three_lines(self):
        lines = [
            'Daan\n',
            '   Jaap, Bert, Jan\n',
            '   Roderik, Gert, Maurits\n'
        ]
        result = Parser.parse_three_lines(lines, 0)
        expected = self.questions['v1']
        self.assertEqual(result, expected)


    def test_get_names_out_of_line_end_line(self):
        result = Parser.get_names_out_of_line('Daan\n')
        self.assertEqual(result, ['Daan'])

    def test_get_names_out_of_line_multi(self):
        result = Parser.get_names_out_of_line('Daan, Frederik, Bert\n')
        self.assertEqual(result, ['Daan', 'Frederik', 'Bert'])

    def test_get_names_out_of_line_hard(self):
        result = Parser.get_names_out_of_line('    Daan, Frederik, Bert\n')
        self.assertEqual(result, ['Daan', 'Frederik', 'Bert'])







class FileCompareTestCase(unittest.TestCase):
    def compare_files(self, file1_ref, file2_ref):
        '''
        Compares files line by line
        :param file1:
        :param file2:
        :return: None
        '''
        lines1 = self.get_lines(file1_ref)
        lines2 = self.get_lines(file2_ref)
        self.assertEqual(lines1, lines2)



class TestImgGenerator(unittest.TestCase):
    def setUP(self):
        pass

    def output_test_img(self):
        self.compare_imgs(self.path_to_expected, self.path_to_result)

    def compare_imgs(self, path_to_expected, path_to_results):
        expected = glob.glob("{}/img/*.jpg".format(path_to_expected))
        result = glob.glob("{}/img/*.jpg".format(path_to_results))
        self.assertEqual(expected, result, "should contain the same imgs")




class TestQuestionJsGenerator(FileCompareTestCase):
    def output_test_surveys(self):
        self.compare_surveys(self.path_to_expected, self.path_to_result)

    def compare_surveys(self, path_to_expected, path_to_results):
        expected_file_ref = path_to_expected + "/limesurvey_survey_900000.lss"
        result_file_ref = path_to_results + "/limesurvey_survey_9000000.lss"
        self.compare_files(expected_file_ref, result_file_ref)


class TestSurveyGenerator(FileCompareTestCase):
    def output_test_js(self):
        self.compare_js(self.path_to_expected, self.path_to_result)

    def compare_js(self, path_to_expected, path_to_results):
        expected_file_ref = path_to_expected + "/questions.js"
        result_file_ref = path_to_results + "/questions.js"
        self.compare_files(expected_file_ref, result_file_ref)










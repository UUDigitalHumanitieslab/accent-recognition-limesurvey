from .helper_functions import *
import glob

class Parser:
    @staticmethod
    def parse(settings):
        """
        :param data_path:
        :return: {"files": [
            {"old": "Daan.jpg", "new": "v1.jpg"}....
            ],
            "questions": v1: {....}} (see parser.parse_names)
        """
        questions = Parser.parse_names(settings["names_file_ref"])
        result = {}
        result["files"]= [{"old": "{}.jpg".format(questions[q]["realName"]), "new": "{}.jpg".format(q)} for q in questions]
        result["questions"] = questions
        return result

    @staticmethod
    def get_input_files(path_to_data):
        # Get all the imgs
        # Get the names files
        return (
        {"imgs": glob.glob("{}/*.jpg".format(path_to_data)), "names_file_ref": "{}/names.txt".format(path_to_data)})

    @staticmethod
    def parse_names(names_file_ref):
        """
        :param names_file_ref: reference to a names.txt file
        :return: {v1: {
            "A": [],
            "B": [],
            realName: ""
            v2: {...}}
        """
        result = {}
        lines = get_lines(names_file_ref)
        if(len(lines) % 3 != 0):
            raise ValueError("The number of lines is not correct should be a multiple of three but is {}".format(len(lines)))
        i = 0
        question_number = 1
        while(i < len(lines)):
            question = Parser.parse_three_lines(lines, i)
            result['v{}'.format(question_number)] = question
            i += 3
            question_number += 1
        return result


    @staticmethod
    def parse_three_lines(lines, i):
        """
        Parses three lines, expect the following format of the three lines:
        name:
            group A names
            group B names
        :param lines: the lines to parse
        :param i: index to look at
        :return:
        """
        return {
            "realName": Parser.get_names_out_of_line(lines[i])[0],
            "A": Parser.get_names_out_of_line(lines[i + 1]),
            "B": Parser.get_names_out_of_line(lines[i + 2])
        }

    @staticmethod
    def get_names_out_of_line(line):
        """
        Get all the names that are in a line
        :param line: A line containing names
        :return:
        """
        #Deletes the leading white spaces
        #line = re.sub('^[ ]*', "", line)
        line = line.strip()
        #Deletes all the special characters
        return line.split(", ")
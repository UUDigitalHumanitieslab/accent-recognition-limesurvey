import glob
from .helper_functions import *
import shutil
import os
import json
from mako.template import Template
from .parser import Parser

class AbstractGenerator:
    def __init__(self, settings):
        self.settings = settings

    def generate(self, parsing_result, input_location, output_location):
        """
        Generates files
        :param parsing_result: a dict containing the following information:
        the questions
        the files
        starting_question_id
        starting_group_id
        survey_id
        main_js_file_ref
        question_js_file_ref
        :param input_location:
        :param output_location:
        :return:
        """
        raise NotImplementedError()

class ImgGenerator(AbstractGenerator):
    """
    Generates img from a given parsing result, needs a list of files which has the properties 'old' and 'new'
    """
    def generate(self,  parsing_result, input_location, output_location):
        create_folder(output_location)
        for file in parsing_result["files"]:
            shutil.copy("{}/{}".format(input_location, file["old"]), "{}/{}".format(output_location, file["new"]))

class JsGenerator(AbstractGenerator):
    """
    Generates the js files containing the questions
    """
    def generate(self, parsing_result, input_location, output_location):
        with open("{}/questions.js".format(output_location), "w+") as f:
            f.write("Questions = ")
            json.dump(parsing_result["questions"], f, indent=2)


class SurveyGenerator(AbstractGenerator):
    """
    Generates the actual survey. It first generates the groups, than the questions and finally the whole survey
    """
    def __init__(self, settings):
        AbstractGenerator.__init__(self, settings)
        self.group_template_ref = settings["group"]
        self.questions_template_ref = settings["question"]
        self.survey_template = settings["survey"]

    def generate(self, parsing_result, input_location, output_location):
        groups = self.render_template( self.group_template_ref, parsing_result)
        questions = self.render_template(self.questions_template_ref, parsing_result)

        self.write_template_to_file(self.survey_template, {"groups": groups, "questions": questions, "survey_id": parsing_result["survey_id"]}, output_location)

    def write_template_to_file(self, template_ref, json, output_location):
        output = self.render_template(template_ref, json)
        with open("{}/survey_{}.lss".format(output_location,json["survey_id"]), "w+") as f:
            f.write(output)

    def render_template(self, template_ref, json):
        template = Template(filename=template_ref, strict_undefined=True)

        return template.render(**json)


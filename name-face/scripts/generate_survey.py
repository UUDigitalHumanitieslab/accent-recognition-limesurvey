"""
The script to generate nameface surveys
"""

from survey_generator.parser import Parser
from survey_generator.generators import *
from survey_generator.providers import *
from survey_generator.survey_creator import SurveyCreator

settings_provider = JsonRefProvider("./data/deploy-settings.json")
metadata_provider = ParsedMetadataProvider(Parser)
generators = [JsGenerator, ImgGenerator, SurveyGenerator]
creator = SurveyCreator(settings_provider, metadata_provider, generators)
creator.create_survey()
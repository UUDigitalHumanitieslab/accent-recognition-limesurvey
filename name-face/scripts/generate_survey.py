from .survey_creator import SurveyCreator
from .parser import Parser
from .generators import *
from .providers import *


settings_provider = JsonRefProvider("./data/develop-settings.json")
metadata_provider = ParsedMetadataProvider(Parser)
generators = [JsGenerator, ImgGenerator, SurveyGenerator]
creator = SurveyCreator(settings_provider, metadata_provider, generators)
creator.create_survey()
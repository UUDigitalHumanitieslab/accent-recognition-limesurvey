import json

class Provider:

    def get(self, *args, **kwargs):
        """
        Gets whatever the provider is providing
        :param args:
        :param kwargs:
        :return:
        """
        raise NotImplementedError


class JsonRefProvider(Provider):
    """
    provides a dict by converting a json file to a dict
    """
    def __init__(self, json_ref_file):
        self.settings_reference = json_ref_file

    def get(self, *args, **kwargs):
        result = {}
        with open(self.settings_reference) as f:
            result = json.load(f)
        return result


class ParsedMetadataProvider(Provider):
    """
    Provides by using a parser and adds the settings to the resulting parsing data
    """
    def __init__(self, parser):
        self.parser = parser

    def get(self, *args, **kwargs):
        settings = kwargs["settings"]
        metadata = self.parser.parse(settings)
        metadata.update(settings)
        return metadata



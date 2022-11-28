import json
from typing import Any


class BaseProviderClass:
    """
    Rises error when there is no such method of providing data
    """

    @staticmethod
    def get(item_name: str):

        raise NotImplementedError("get method is not implemented")


class JSONConfigProvider(BaseProviderClass):
    """
    Returns value equivalent to variable accessed from OS
    """

    @staticmethod
    def _read_config(config_path):
        """
        accesses dict from json file path
        """
        with open(config_path) as json_file:
            return json.load(json_file)

    # uses _read_config to get value
    @staticmethod
    def __getitem__(item_name: str):
        value = JSONConfigProvider._read_config(
            "/home/glo-saczkowski/TE_2.0/talent-eng/envs_config/dev.json"
        )
        return value[item_name]


class Config:
    """
    Shares provided values
    """

    # initializing object
    def __init__(self, config_providers) -> None:
        self.config_providers = config_providers
        # establishes place to keep obj from _register
        self.conf_dict = {}
        self._register("USER_NAME")
        self._register("BASE_URL_API")
        self._register("BASE_URL_UI")

        self._register("USER_LOCALIZATION")

    def __getattr__(self, item_name: str):
        """
        Returns value of registered key
        """
        return self.conf_dict[item_name]

    # creates item in conf.dict
    def _register(self, item_name: str):
        """
        Iterates through given providers and register item in config data (if item found in provider)
        """
        for provider in self.config_providers:
            value = provider[item_name]
            if value is not None:
                self.conf_dict[item_name] = value
                return
            raise ValueError(f"{item_name} name is missing in config providers")


config = Config([JSONConfigProvider()])
print(config.__getattr__("USER_NAME"))
print(config.USER_LOCALIZATION)

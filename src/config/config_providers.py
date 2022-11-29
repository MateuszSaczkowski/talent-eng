import json
import os
from typing import Any

from base_provider import BaseProviderClass


class OSConfigProvider(BaseProviderClass):
    """
    Returns value equivalent to variable accessed from OS
    """

    @staticmethod
    def get(item_name: str) -> Any:
        value = os.getenv(item_name)
        return value


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
    def __getitem__(item_name: str) -> Any:
        value = JSONConfigProvider._read_config(
            "/home/glo-saczkowski/TE_2.0/talent-eng/envs_config/dev.json"
        )
        return value[item_name]

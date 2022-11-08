from typing import Any
import json


class ConfigProvider:

    @staticmethod
    def _read_config(config_path):
        with open(config_path) as json_file:
            return json.load(json_file)

    @staticmethod
    def get(item_name: str) -> Any:
        value = ConfigProvider._read_config("/home/glo-saczkowski/TE_2.0/talent-eng/envs_config/dev.json")
        return value[item_name]
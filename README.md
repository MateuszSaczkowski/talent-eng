## Framework structure
src/config file:

src/config/config_providers.py : contains JSONConfigProvider and OSConfigProvider classes, that are responsible for providing values from file path. Providing classes are supported by parent class BaseProviderClass that raises error when exact method is not found.

src/config/config.py : contains Config class that indicate item and receive value from providers

src/envs_configs:
-dev.json : contains data
import os
from os import PathLike
from typing import Any, AnyStr, Dict, Union

import yaml
from sanic.config import Config
from yaml import Loader


class AttrDict(dict):
    __slots__ = ()
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


class YamlConfig(Config):
    """
    Our config was based on yaml files.
    So i construct a new config class for loading settings from yaml.

    Why do i choose yaml? Because i need a human-readable configruation file.

    Like django using py to keep its configuration, as i think, it will be messed in long run.
    After that, only one way to solve this, 1 is split project to many smaller one.
    """

    def __init__(self, yaml_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load(yaml_path)

    def __getattr__(self, attr):
        try:
            return super().__getattr__(attr)
        except AttributeError:
            return getattr(self._config, attr)
    
    def _load_yaml(self, yaml_path: Union[PathLike, AnyStr]):
        """
        Validate yaml path input and return loaded data from yaml.
        """
        assert isinstance(yaml_path, (PathLike, str)), "Invalid yaml path."
        assert os.path.exists(yaml_path), f"Yaml path:{yaml_path} does not exist."
        assert os.path.isfile(yaml_path), f"Yaml path:{yaml_path} is not a file."

        return yaml.load(open(yaml_path, "r").read(), Loader)

    def load(self, yaml_path: Union[PathLike, AnyStr]):
        data = self._load_yaml(yaml_path)
        self.update_config(data)

    def update_config(self, config: Dict[str, Any]):
        def upper_key(data):
            if isinstance(data, dict):
                return AttrDict(**{k.upper(): upper_key(v) for k, v in data.items()})
            elif isinstance(data, list):
                return [upper_key(v) for v in data]
            else:
                return data
        self._config = AttrDict(**upper_key(config))

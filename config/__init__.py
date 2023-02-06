import os

import yaml
from functools import partial
from config.config_parser import *


__marshalled_classes = (Config, CardTypeCombinationGenerator, GenericAttributeMap)


def __combinations_config():
    """Add constructors to PyYAML loader and load config with marshalled classes"""
    def __yaml_marker_class_constructor(marker_class, safe_loader: yaml.SafeLoader, node: yaml.nodes.MappingNode):
        """Construct an instance of a YAML marker class."""
        return marker_class(**safe_loader.construct_mapping(node))
    safe_loader = yaml.SafeLoader
    for marshalled_class, marshalled_class_name in ((mc, mc.__name__) for mc in __marshalled_classes):
        safe_loader.add_constructor(f"!{marshalled_class_name}", partial(__yaml_marker_class_constructor, marshalled_class))
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.yaml"), "r") as f:
        return yaml.load(f, Loader=safe_loader)


CONFIG = __combinations_config()

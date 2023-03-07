import os
import yaml

from config.types import *


class ConfigLoader(yaml.Loader):
    def __init__(self, stream):
        super().__init__(stream)

def read_only_attr_dict_constructor(loader: yaml.Loader, node: yaml.nodes.MappingNode):
    return ReadOnlyAttrDict(**loader.construct_mapping(node))

def card_type_combination_generator_constructor(loader: yaml.Loader, node: yaml.nodes.MappingNode):
    return CardTypeCombinationGenerator(**loader.construct_mapping(node))

ConfigLoader.add_constructor("tag:yaml.org,2002:map", read_only_attr_dict_constructor)
ConfigLoader.add_constructor("!CardTypeCombinationGenerator", card_type_combination_generator_constructor)


def __parse_config():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.yaml"), "r") as f:
        return yaml.load(f, Loader=ConfigLoader)


CONFIG = __parse_config()

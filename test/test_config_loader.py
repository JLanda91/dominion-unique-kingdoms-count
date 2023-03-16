import yaml
import unittest

from config import ConfigLoader
from config.types import ReadOnlyAttrDict


class TestConfigLoaderDoesNotChangeDefaultLoader(unittest.TestCase):
    def setUp(self) -> None:
        self.sample_yaml_string = """
        a: 1
        b: 
          c: 3
          d: 4
        """


    def assertHasAttr(self, obj, attr, msg=None):
        self.assertTrue(hasattr(obj, attr), msg)


    def test_config_loader_loads_as_attrs(self):
        doc = yaml.load(self.sample_yaml_string, Loader=ConfigLoader)
        self.assertIsInstance(doc, ReadOnlyAttrDict, f"ConfigLoader YAML root not marshalled into ReadOnlyAttrDict")
        self.assertHasAttr(doc, 'a', f"ConfigLoader YAML has no member 'a'")
        self.assertHasAttr(doc, 'b', f"ConfigLoader YAML has no member 'b'")
        self.assertIsInstance(doc.b, ReadOnlyAttrDict, f"ConfigLoader YAML non-root non-scalar not marshalled into ReadOnlyAttrDict")
        self.assertHasAttr(doc.b, 'c', f"ConfigLoader YAML has no member 'b.c'")
        self.assertHasAttr(doc.b, 'd', f"ConfigLoader YAML has no member 'b.d'")


    def test_default_loader_loads_as_dict(self):
        doc = yaml.load(self.sample_yaml_string, Loader=yaml.Loader)
        self.assertIsInstance(doc, dict, f"Default Loader YAML root not marshalled into dict")
        self.assertIn('a', doc, f"Default Loader YAML has no key 'a'")
        self.assertIn('b', doc, f"Default Loader YAML has no key 'b'")
        self.assertIsInstance(doc['b'], dict, f"Default Loader YAML non-root non-scalar not marshalled into dict")
        self.assertIn('c', doc['b'], f"Default Loader YAML has no subkey 'b.c'")
        self.assertIn('d', doc['b'], f"Default Loader YAML has no subkey 'b.d'")


if __name__ == '__main__':
    unittest.main()

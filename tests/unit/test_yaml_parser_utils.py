import os
import tempfile
import yaml
from pytest import mark, fixture
from uaf.utilities.parser.yaml_parser_utils import YamlParser


@fixture
def temp_yaml_file():
    content = {
        "section1": {"key1": "value1", "key2": "value2"},
        "section2": {"key3": "value3"},
    }
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".yml", delete=False
    ) as temp_file:
        yaml.dump(content, temp_file)
    yield temp_file.name
    os.unlink(temp_file.name)


@mark.unit_test
def test_yaml_parser_init(temp_yaml_file):
    parser = YamlParser(temp_yaml_file)
    assert parser.config == {
        "section1": {"key1": "value1", "key2": "value2"},
        "section2": {"key3": "value3"},
    }


@mark.unit_test
def test_get_section(temp_yaml_file):
    parser = YamlParser(temp_yaml_file)
    assert parser.get_section("section1") == {"key1": "value1", "key2": "value2"}


@mark.unit_test
def test_get_value(temp_yaml_file):
    parser = YamlParser(temp_yaml_file)
    assert parser.get_value("section1", "key1") == "value1"


@mark.unit_test
def test_set_value(temp_yaml_file):
    parser = YamlParser(temp_yaml_file)
    parser.set_value("section1", "key4", "value4")
    assert parser.get_value("section1", "key4") == "value4"


@mark.unit_test
def test_save(temp_yaml_file):
    parser = YamlParser(temp_yaml_file)
    parser.set_value("section3", "key5", "value5")
    parser.save()

    with open(temp_yaml_file) as f:
        content = yaml.safe_load(f)

    assert "section3" in content
    assert content["section3"]["key5"] == "value5"

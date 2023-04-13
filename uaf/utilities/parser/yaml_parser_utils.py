import os

import yaml  # type: ignore

from uaf.enums.file_paths import FilePaths


class YamlParser:
    """Utility class for parsing yaml documents"""

    def __init__(self, relativeFilepathWithExtension: FilePaths):
        """Constructor

        Args:
            relativeFilepathWithExtension (FilePaths): relative filepath of the yaml document
        """
        self.filePath = os.path.join(os.getcwd(), relativeFilepathWithExtension.value)
        with open(self.filePath, "r") as f:
            self.config = yaml.safe_load(f)

    def get_section(self, section):
        """Fetches specified section from a yaml document

        Args:
            section (str): section name

        Raises:
            ValueError: if section is invalid/doesn't exist

        Returns:
            dict[str, Any]: data in key value pair
        """
        if section in self.config:
            return self.config[section]
        else:
            raise ValueError("Selected {} section is invalid/doesn't exist!".format(section))

    def get_value(self, section, key):
        """Fetches specified key value from a specified section

        Args:
            section (str): name of the section
            key (str): name of the key

        Raises:
            ValueError: if section-key pair is invalid/doesn't exist

        Returns:
            Any: value
        """
        if section in self.config and key in self.config[section]:
            return self.config[section][key]
        else:
            raise ValueError("Selected {}-{} section-key pair is invalid/doesn't exist!".format(section, key))

    def set_value(self, section, key, value):
        """Set specified value in specified section's key

        Args:
            section (str): name of the section
            key (str): name of the key
            value (Any): data to be set
        """
        if section not in self.config:
            self.config[section] = {}
        self.config[section][key] = value

    def save(self):
        """Saves the data to the yaml document in focus"""
        with open(self.filePath, "w") as f:
            yaml.dump(self.config, f, default_flow_style=False)

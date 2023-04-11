import yaml
import os
from uaf.enums.file_paths import FilePaths


class YamlParser:
    def __init__(self, relativeFilepathWithExtension: FilePaths):
        self.filePath = os.path.join(os.getcwd(), relativeFilepathWithExtension.value)
        with open(self.filePath, "r") as f:
            self.config = yaml.safe_load(f)

    def get_section(self, section):
        if section in self.config:
            return self.config[section]
        else:
            raise ValueError(
                "Selected {} section is invalid/doesn't exist!".format(section)
            )

    def get_value(self, section, key):
        if section in self.config and key in self.config[section]:
            return self.config[section][key]
        else:
            raise ValueError(
                "Selected {}-{} section-key pair is invalid/doesn't exist!".format(
                    section, key
                )
            )

    def set_value(self, section, key, value):
        if section not in self.config:
            self.config[section] = {}
        self.config[section][key] = value

    def save(self):
        with open(self.filePath, "w") as f:
            yaml.dump(self.config, f, default_flow_style=False)

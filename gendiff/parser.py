import json
import yaml
from typing import TextIO


def get_extension(name: str) -> str:
    return name.split('.')[1]


def parse_json(file: TextIO) -> dict:
    return json.load(file)


def parse_yaml(file: TextIO) -> dict:
    return yaml.load(file, yaml.Loader)


def parse(file: TextIO) -> dict | None:
    """Parses the given file into Python's dictionary
    :arg file: The file object
    :return: A parsed dictionary"""

    extensions = {
        'json': parse_json,
        'yaml': parse_yaml,
        'yml': parse_yaml
    }
    extension = get_extension(file.name)

    if extension in extensions:
        return extensions.get(extension)(file)

    raise Exception(f'Couldn\'t parse data from \"{file.name}\"! '
                    + '(.json or .yaml expected)')

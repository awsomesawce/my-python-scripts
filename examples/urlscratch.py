"""Another json fetcher
Fetch info about pip projects in json format.
Parse info using json module.
"""

import ujson as json
import yaml
import toml
from pathlib import Path
from pprint import pprint
from urllib.request import urlopen
from yarl import URL

def get_json_web(url: str = 'https://pypi.org/pypi/mypy/json'):
    with urlopen(url) as resp:
        project_info = json.load(resp)['info']
    return project_info

def write_json(obj, file: str = "jsonfile.json"):
    with open(file, 'w', encoding='utf-8') as f:
        return f.write(json.dumps(obj))

def write_toml(obj, file: str = "tomlfile.toml"):
    with open(file, 'w', encoding='utf-8') as f:
        return toml.dump(obj, file)

def write_yaml(obj, file: str = "yamlfile.yml"):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(yaml.dump(obj))

projinfo = get_json_web()
write_json(projinfo)

with open("tomlfile.toml", 'w') as f:
    toml.dump(projinfo, f)


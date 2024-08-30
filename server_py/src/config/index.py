
# self
from config.path import config_yaml

#lib
import yaml
from pathlib import Path

conf = yaml.safe_load(Path(config_yaml).read_text(encoding="utf-8"))
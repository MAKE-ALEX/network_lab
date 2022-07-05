import yaml
import json

with open('yaml_text.Yaml') as f:
    yaml_template = yaml.safe_load(f)

with open('json_text.json', 'w') as f:
    json.dump(yaml_template, f, sort_keys=False, indent=2)
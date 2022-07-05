import yaml
import json


def yaml_transform_json(yaml_f, json_f):
    with open(yaml_f) as f:
        yaml_template = yaml.safe_load(f)

    with open(json_f, 'w') as f:
        json.dump(yaml_template, f, sort_keys=False, indent=2)


def json_transform_yaml(json_f, yaml_f):
    with open(json_f) as f:
        json_template = json.load(f)

    with open(yaml_f, 'w') as f:
        yaml.dump(json_template, f, default_flow_style=False, sort_keys=False)

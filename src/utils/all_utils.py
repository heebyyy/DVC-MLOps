import yaml
import os
import json


def read_yaml(config_path: str) -> dict:
    with open(config_path) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content


def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"The directory is created at {dir_path}")


def save_local_df(data, data_path):
    data.to_csv(data_path, index=False)
    print(f"Data saved in {data_path}")


def save_reports(report: dict, report_path: str):
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"reports is saved in {report_path}")

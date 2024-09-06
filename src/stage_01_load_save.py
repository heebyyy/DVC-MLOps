from src.utils.all_utils import read_yaml, create_directory
import pandas as pd
import argparse
import os


def get_data(config_file):
    config = read_yaml(config_file)
    remote_data_path = config['data_source']
    df = pd.read_csv(remote_data_path, sep=';')

    # artifacts/raw_local_dir/data.csv
    artifacts_dir = config['artifacts']['artifacts_directory']
    raw_local_dir = config['artifacts']['raw_local_directory']
    raw_local_file = config['artifacts']['raw_local_file']

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)
    create_directory(dirs=[raw_local_dir_path])
    raw_local_file_path = os.path.join(artifacts_dir, raw_local_dir, raw_local_file)

    df.to_csv(raw_local_file_path, index=False, sep=',')


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    parsed_args = args.parse_args()

    get_data(config_file=parsed_args.config)

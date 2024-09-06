from src.utils.all_utils import read_yaml, create_directory
import pandas as pd
import argparse
import os
from sklearn.linear_model import ElasticNet
import joblib


def train(config_file, params_path):
    config = read_yaml(config_file)
    params = read_yaml(params_path)

    artifacts_dir = config['artifacts']['artifacts_directory']
    split_data_dir = config['artifacts']['split_data_dir']
    train_data_filename = config['artifacts']['train']

    train_data_file_path = os.path.join(artifacts_dir, split_data_dir, train_data_filename)

    df = pd.read_csv(train_data_file_path)

    train_y = df['quality']
    train_x = df.drop('quality', axis=1)

    alpha = params['model_parameters']['ElasticNet']['alpha']
    l1_ratio = params['model_parameters']['ElasticNet']['l1_ratio']
    random_state = params['base']['random_state']

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    lr.fit(train_x, train_y)

    model_dir = config['artifacts']['model_dir']
    model_filename = config['artifacts']['model_filename']

    create_directory([os.path.join(artifacts_dir, model_dir)])
    model_path = os.path.join(artifacts_dir, model_dir, model_filename)

    joblib.dump(lr, model_path)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    train(config_file=parsed_args.config, params_path=parsed_args.params)

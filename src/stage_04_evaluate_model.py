from src.utils.all_utils import read_yaml, create_directory, save_reports
import pandas as pd
import argparse
import os
import joblib
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def evaluate_metrics(true_val, predicted_val):
    rmse = np.sqrt(mean_squared_error(true_val, predicted_val))
    mae = mean_absolute_error(true_val, predicted_val)
    r2 = r2_score(true_val, predicted_val)
    return rmse, mae, r2


def evaluate(config_file):
    config = read_yaml(config_file)

    artifacts_dir = config['artifacts']['artifacts_directory']

    split_data_dir = config['artifacts']['split_data_dir']
    test_data_filename = config['artifacts']['test']
    test_path = os.path.join(artifacts_dir, split_data_dir, test_data_filename)

    df = pd.read_csv(test_path)
    test_y = df['quality']
    test_x = df.drop('quality', axis=1)

    model_dir = config['artifacts']['model_dir']
    model_filename = config['artifacts']['model_filename']
    model_path = os.path.join(artifacts_dir, model_dir, model_filename)

    lr = joblib.load(model_path)
    predicted_val = lr.predict(test_x)
    rmse, mae, r2 = evaluate_metrics(test_y, predicted_val)

    reports_dir = config['artifacts']['reports_dir']
    create_directory([os.path.join(artifacts_dir, reports_dir)])
    scores_file_path = config['artifacts']['scores']
    scores_path = os.path.join(artifacts_dir, reports_dir, scores_file_path)

    scores = {
        "rmse": rmse,
        "mae": mae,
        "r2": r2
    }
    save_reports(scores, os.path.join(scores_path))


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    evaluate(config_file=parsed_args.config)

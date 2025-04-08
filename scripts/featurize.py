import time
import pandas as pd
from pathlib import Path
from ersilia import ErsiliaModel 

DATASET_NAME = "dili"


def generate_features(featurizer, DATASET_NAME, data_dir = "./data/dili"):
    data_path = Path(data_dir)
    data_file = data_path / f"{DATASET_NAME}.csv"
    features_output_path = data_path / f"{DATASET_NAME}_{featurizer}_featurized.csv"

    print(f"Featurizing {DATASET_NAME}")
    featurize_model = ErsiliaModel(model = featurizer)
    featurize_model.serve()
    
    featurize_model.run(input = str(data_file), output = str(features_output_path))
    generated_features = pd.read_csv(features_output_path)

    df = pd.read_csv(f'{data_dir}/{DATASET_NAME}.csv')
    generated_features = generated_features.merge(df[["Drug", "Y"]], left_on="input", right_on="Drug", how="inner")
    generated_features.drop(columns=["Drug"], inplace=True)
    generated_features.to_csv(features_output_path, index=False)

    print("Featurized successfully")

    return generated_features
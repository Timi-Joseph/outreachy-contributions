import pandas as pd
import numpy as np
from ersilia import ErsiliaModel

DATASET_NAME = "dili"

# Load dili Dataset
dili_train = pd.read_csv(f"./data/{DATASET_NAME}/{DATASET_NAME}_train.csv")
dili_valid = pd.read_csv(f"./data/{DATASET_NAME}/{DATASET_NAME}_valid.csv")
dili_test = pd.read_csv(f"./data/{DATASET_NAME}/{DATASET_NAME}_test.csv")

dili_all = pd.concat([dili_train, dili_valid, dili_test])
dili_smiles = [
    smi for smi in dili_all["Drug"].tolist() if isinstance(smi, str) and smi
]  # and smi removes falsey values ("" or None)
dili_labels = [
    lbl
    for smi, lbl in zip(dili_all["Drug"], dili_all["Y"])
    if isinstance(smi, str) and smi
]

print(f"Length of {DATASET_NAME} Smiles = {len(dili_smiles)}")


model = ErsiliaModel("eos9gg2")
model.serve()

print("Model Served Successfully ✅")


# # Featurizing with batching (Didn't run with out batching -- Huge data)
def batch_run(smiles_list: list, batch_size: int = 20):
    features = []
    for i in range(0, len(smiles_list), batch_size):
        print(f"Loop {i} running")
        batch = smiles_list[i : i + batch_size]
        batch_features = [item["output"]["outcome"] for item in model.run(batch)]
        features.extend(batch_features)
        print(f"Processed {len(features)} of {len(smiles_list)}")
    return np.array(features)


dili_features = batch_run(dili_smiles)

# Saving dili
dili_features_df = pd.DataFrame(
    dili_features,
    columns=["PCA1", "PCA2", "PCA3", "PCA4", "UMAP1", "UMAP2", "tSNE1", "tSNE2"],
)
dili_features_df["SMILES"] = dili_smiles
dili_features_df["Label"] = dili_labels
dili_features_df.to_csv(
    f"./data/{DATASET_NAME}/{DATASET_NAME}_ccsign_features.csv", index=False
)

print("dili features shape:", dili_features.shape)

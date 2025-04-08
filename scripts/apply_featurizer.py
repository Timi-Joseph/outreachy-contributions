from featurize import generate_features


test_path = 'dili_test'
test_df = generate_features(featurizer = 'eos9gg2', DATASET_NAME = test_path)

train_path = 'dili_train'
train_df = generate_features(featurizer = 'eos9gg2', DATASET_NAME = train_path)

valid_path = 'dili_valid'
valid_df = generate_features(featurizer = 'eos9gg2', DATASET_NAME = valid_path)
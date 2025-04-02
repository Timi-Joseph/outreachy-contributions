# Outreachy contribution period

<!--
This repository contains a basic folder structure to be used during the Outreachy contribution period. Please make a fork to start contributing, and detail progress in the open issue. 

## Project goals:
- Understand how to use and interact with the Ersilia Model Hub
- Demonstrate basic AI/ML knowledge
- Show your Python coding skills 
- Practice code documentation and end user documentation


## Structure overview
The template repository already has pre-defined folders. Please restrict your project to using them for easy review:
- data: folder where data needs to be stored once downloade
- notebooks: jupyter notebooks
- scripts: python/bash scripts necessary to run the project
- models: folder with model checkpoints

Please modify this README to write your project documentation. -->

## Week 2/3 Task
Below is a list of steps to reproduce the task completed from week 2 of the application phase

Tools needed to complete this task

- Python3 Installation on the host machine
- Vscode enabled with Jupyter support or Google Colab or Jupyter notebook
- Git

1. Download the Ames Mutagenicity Dataset from [Therapeutics Data Commons](https://tdcommons.ai/single_pred_tasks/tox#ames-mutagenicity). The Ames Mutagenencity Datab

- Open the [ames_mutagenicity.ipynb](notebooks/ames_mutagenicity.ipynb) Notebook and run each cell the to download the dataset

    1. The notebook install TDC library using
        ```bash
        !pip install PyTDC
        ```
    2. Load the AMES Dataset with the library
       ```python
       from tdc.single_pred import Tox
       data = Tox(name = 'AMES')
       ```
    3. Split the dataset into Train, Validation and Test sets
        ```python
        split = data.get_split()
        ```
    This gave me 5094 Train data, 1456 Validation data and 738 test data

    4. Save the Downloaded dataset to the project environment data directory
       ```python
        split['train'].to_csv("../data/ames/ames_train.csv", index=False)
        split['valid'].to_csv("../data/ames/ames_valid.csv", index=False)
        split['test'].to_csv("../data/ames/ames_test.csv", index=False)
       ```
    This saves the downloaded dataset in an Ames folder under the data directory at the root of the project.


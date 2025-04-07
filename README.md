# Outreachy contribution period

## Installation
Tools needed;

- Python3 Installation on the host machine
- Vscode enabled with Jupyter support or Google Colab or Jupyter notebook
- Git
- Create And Activate Python Virtual Environment
  ```bash
  python3 -m venv venv && source venv/bin/activate && pip install requirements.txt
  ```
- Install libmp: Needed for Macos to run XGBoost package
  ```bash
  brew install libomp
  ```

## Dataset Details
Drug-induced liver injury (DILI) is fatal liver disease caused by drugs and it has been the single most frequent cause of safety-related drug marketing withdrawals for the past 50 years (e.g. iproniazid, ticrynafen, benoxaprofen). This dataset is aggregated from U.S. FDA’s National Center for Toxicological Research.

### Download and Save Dataset
Download the Dataset from [Therapeutics Data Commons](https://tdcommons.ai/single_pred_tasks/tox#ames-mutagenicity). The DILI (Drug Induced Liver Injury) Dataset

- Open the [drug_induced_liver_injury.ipynb](notebooks/drug_induced_liver_injury.ipynb) Notebook and run each cell the to download the dataset

    1. The notebook install TDC library using
        ```bash
        !pip install PyTDC
        ```
    2. Load the AMES Dataset with the library
       ```python
       from tdc.single_pred import Tox
       data = Tox(name = 'Dili')
       ```
    3. Split the dataset into Train, Validation and Test sets
        ```python
        split = data.get_split()
        ```
    This gave me 5094 Train data, 1456 Validation data and 738 test data

    4. Save the Downloaded dataset to the project environment data directory
       ```python
        split['train'].to_csv("../data/dili/dili_train.csv", index=False)
        split['valid'].to_csv("../data/dili/dili_valid.csv", index=False)
        split['test'].to_csv("../data/dili/dili_test.csv", index=False)
       ```
    This saves the downloaded dataset in an Ames folder under the data directory at the root of the project.


## How to Run the Code


### Step 2


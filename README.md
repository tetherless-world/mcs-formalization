# MCS Formalization

MCS Formalization is a repository that performs evaluation metrics from categorization exercizes on the CycIC benchmark released on 12/1/2020. The metrics used are accuracy, balanced accuracy, and p-value and are calculated using sklearn modules. 

For more information on the sklearn metrics, refer to: https://scikit-learn.org/stable/modules/model_evaluation.html and https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html.

## One-time Setup

### Create the Python virtual environment

From the current directory:

    python3.6 -m venv venv
    
## Before Evaluating

### Activate the virtual environment

On Unix:

    source venv/bin/activate

On Windows:

    venv\Scripts\activate

### Install the dependencies and the project module

    pip install -r requirements.txt
    
### Categorization Data

Place the categorization data in mcs_formalization/data/categorizations in the format of the given files. Refer to the examples for proper formatting.
    
## Performing the Evaluation

From mcs_formalization/ run 

    python3.6 metrics.py
    
Output files will be located in mcs_formalization/data/results

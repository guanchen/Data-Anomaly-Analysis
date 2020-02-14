# Scripts to prepare data for analysis

## Introduction
The Script to prepare data from SQL databases
remove duplicates rows

### Input and output
Data input accepted:
.csv or .txt file

Data output:
.csv file

### Prerequisites
- Python3
- virtualenv (optional but recommended to run script in isolated Python env)

## Environment preparation

### Create your Python3 environment (optional)
Create the Python3 isolated environment with virtualenv
```
virtualenv <DEST_DIR> -p python3
```
You can now access to the environment
```
source <DEST_DIR>/bin/activate
```

### Install the Python module prerequisites
Install the Python module prerequisites with pip 
```
pip install -r requirements.txt
```

## How to use the script

```
python prepare_data.py data [-h] [--output OUTPUT] [--sep SEP]


positional arguments:
  data             Data file

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  CSV file output
  --sep SEP        Separator
```

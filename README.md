# catalog-to-csv
Convert a JSON-formatted Puppet agent catalog to CSV for analysis.

- [catalog-to-csv](#catalog-to-csv)
  - [Requirements](#requirements)
  - [Usage](#usage)
    - [Example](#example)

## Requirements
We use the `pandas` library for conversion. You must install this package through pip in order to run the program properly:

```
pip install pandas
```

## Usage
There are two possible flags that can be used:

```
usage: catalog-to-csv.py [-h] -c CATALOG [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -c CATALOG, --catalog CATALOG
                        converts the provided json catalog to a csv file

optional arguments:
  -o OUTPUT, --output OUTPUT
                        the name of the file to save the processed catalog to
```

### Example

The below example uses the dummy catalog in [examples/webserver.example.com.json](examples/webserver.example.com.json) to create a processed CSV file called `processed_webserver.example.com.csv`

```
python catalog-to-csv.py --catalog examples/webserver.example.com.json --output processed_wbserver.example.com.csv
```

If `--output` is not provided, the processed catalog gets saved to `catalog_processed.csv`.
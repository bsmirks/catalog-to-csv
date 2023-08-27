import argparse
import json
import pandas as pd


def get_json_catalog(json_catalog):
    """
    Load the provided JSON catalog
    :param json_catalog: the path to the JSON catalog file
    :return: the JSON catalog as a dictionary
    """
    try:
        with open(json_catalog, "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"File {json_catalog} not found")
        exit(1)
    except json.JSONDecodeError:
        print(f"File {json_catalog} is not a valid JSON file")
        exit(1)


def json_to_df(resources):
    """
    Convert the JSON catalog into a Pandas DataFrame
    :param resources: the `resources` key from the catalog
    :return: a Pandas DataFrame containing the extracted catalog
    """
    flattened_resources = []
    for resource in resources:
        flattened_resource = {
            "Resource Type": resource["type"],
            "Title": resource["title"],
            "Tags": resource["tags"],
            **resource.get("parameters", {})
        }
        flattened_resources.append(flattened_resource)

    extracted_catalog_dataframe = pd.DataFrame(flattened_resources)
    return extracted_catalog_dataframe


def save_to_csv(dataframe, output_file):
    """
    Save the provided DataFrame to a CSV file
    :param dataframe: the DataFrame to save
    """
    dataframe.to_csv(output_file, index=False)


def main():
    # substantiate command line arguments
    parser = argparse.ArgumentParser()
    parser.add_help = True
    parser.add_argument(
        "-c",
        "--catalog",
        required=True,
        help="converts the provided catalog to a csv file"
        )
    optional = parser.add_argument_group("optional arguments")
    optional.add_argument(
        "-o",
        "--output",
        default="catalog_processed.csv",
        help="the name of the file to save the processed catalog to",
        )
    args = parser.parse_args()

    # load the json catalog and convert it to dataframe
    json_catalog = get_json_catalog(args.catalog)
    resources = json_catalog["resources"]
    df_resources = json_to_df(resources)

    # save the dataframe to csv
    output_file = args.output
    save_to_csv(df_resources, output_file)


if __name__ == "__main__":
    main()

import pandas as pd
import os
from datetime import datetime

def create_timestamp() -> str:
  # helper function to create a unique timestamp
  dt = str(datetime.now())
  return dt.replace("-", "_").replace(":", "_").replace(" ", "_")

def run(input_csv, name_column="none", property_columns=[]):
    df = pd.read_csv(input_csv)
    column_name_map = {item.lower(): item for item in df.columns}
    assert "smiles" in column_name_map, "Input CSV file does not contain a SMILES column"

    # get smiles and names to prepare .smi file
    smiles = df[column_name_map["smiles"]].tolist()
    if name_column == "none" or name_column.lower() not in column_name_map:
        names = [f"molecule_{i}" for i in range(len(df))]
    else:
        names = df[column_name_map[name_column.lower()]].tolist()

    # make sure names are unique
    if len(set(names)) != len(names):
        raise RuntimeError("Names are not unique in the input CSV file")
    
    # write .smi file into a working directory
    workdir = create_timestamp()
    os.makedirs(workdir, exist_ok=True)
    with open(f"{workdir}/input.smi", "w") as f:
        for name, smile in zip(names, smiles):
            f.write(f"{smile}\t{name}\n")

    # prepare the property file
    if len(property_columns) == 0:
        property_columns = [item for item in df.columns if item.lower() not in ["smiles", name_column.lower()]]
    properties = pd.DataFrame()
    properties["ID"] = names

    for prop in property_columns:
        if prop.lower() not in column_name_map:
            print(f"Warning! Skipping property {prop} as it is not found in the input CSV file")
        elif not pd.api.types.is_numeric_dtype(df[column_name_map[prop.lower()]]):
            print(f"Warning! Skipping property {prop} as it is not numeric")
        else:
            properties[prop] = df[column_name_map[prop.lower()]]


    properties.to_csv(f"{workdir}/properties.csv", index=False, sep="\t")

    # run database building
    os.system(f"mmpdb fragment {workdir}/input.smi -o {workdir}/data.fragdb")
    print("Database created")
    os.system(f"mmpdb index {workdir}/data.fragdb --properties {workdir}/properties.csv -o data.mmpdb")

    print(f"Database created as data.mmpdb")

if __name__ == "__main__":
    run("../EGFR_unique.csv", name_column="MolRegNo", property_columns=["cLogP", "total surface area", "pValue"])
# Create a matched molecular pair database (MMPDB) from a CSV table for SAR analysis (Informatics)

## Description
This tool creates a matched molecular pair database from a CSV file. The database can be used to perform matched molecular pair analysis to identify structural changes that lead to changes in compound properties. The input CSV file should have a name column that should be unique for each compound, and a SMILES column.

## Input
* input_csv - A CSV file containing the SAR data
* name_column - The column name in the CSV file that contains the compound names
* property_columns - A list of column names in the CSV file that contain the properties of the compounds you want to analyze

## Output
 A .mmpdb database file that can be used to perform matched molecular pair analysis


# Predict property difference using a matched molecular pair database (Informatics)

## Description
Uses a precompiled matched molecular pair database to predict the property difference between a molecule and a reference molecule. The database should be in the .mmpdb format. The property name should be one of the properties used to compile the database. 

## Input
* database - A precompiled .mmpdb database used for making prediction for property differences
* predict_smiles - SMILES for the molecule to predict the property difference
* reference_smiles - SMILES for the reference molecule
* property_name - The name of the property to predict difference

## Output
 Predicted property difference and standard deviations



# Generate new molecules using a matched molecular pair database (Informatics)
## Description
Using the transformation rules defined in the matched molecular pair database, this tool generates new molecules by applying transformations to the input molecule. 

## Input
* database - A precompiled .mmpdb database that contains the transformation rules
* input_smiles - A SMILES for a molecule based on which new molecules will be generated

## Output
 A csv file containing the generated molecules and their properties


# Setup (for all the tools)
## docker
WORKDIR /opt
RUN wget https://github.com/rdkit/mmpdb/archive/refs/tags/v3.1.tar.gz
RUN tar -xvf v3.1.tar.gz
WORKDIR /opt/mmpdb-3.1
RUN pip install -e .

## requirements
rdkit
pandas
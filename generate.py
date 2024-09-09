import os

def run(database, input_smiles):
    command = f"mmpdb generate --smiles '{input_smiles}' {database} > results.tsv"
    os.system(command)

    # convert tsv to csv
    with open("results.tsv", "r") as f:
        lines = f.readlines()

    with open("results.csv", "w") as f:
        for line in lines:
            f.write(line.replace("\t", ","))


if __name__ == "__main__":
    run("data.mmpdb", "Clc1cccc(Oc(ccc(Nc2ncnc3c2[nH]cc3)c2)c2Cl)c1")
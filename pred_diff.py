import os

def run(database, predict_smiles, reference_smiles, property_name):
    command = f"mmpdb predict --smiles '{predict_smiles}' --reference '{reference_smiles}' {database} --property '{property_name}' > results.txt"
    os.system(command)

    # get the output
    with open("results.txt", "r") as f:
        output = f.read()

    # print the output
    print(output)

if __name__ == "__main__":
    run("data.mmpdb", "C(#N)c1cc(Oc2c(Cl)cc(Nc3c4[nH]ccc4ncn3)cc2)ccc1", "Clc1cccc(Oc(ccc(Nc2ncnc3c2[nH]cc3)c2)c2Cl)c1", "p value")
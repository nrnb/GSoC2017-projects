# this file defines some globe variables used for web interface

# file paths, below is some import files' path

VAR_PATH_PROTEIN_ID_DATABASE = "./DoMoPred/Protein/Db/map_sgd.txt"  # this file is all the ids for the system will work
VAR_PATH_PWMS = "./data/pwm_dir/"  

# this dict defines the map of features name and feature code
# features' name are in index.html , their codes are in run_protein.py
VAR_FEATURES = {
    "cellular_location":"A",
    "biological_process":"B",
    "molecular_function":"C",
    "gene_expression":"D",
    "sequence_signature":"E",
    "protein_expression":"F"
}

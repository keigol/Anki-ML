# Downloads subset of dataset from FSRS-Anki-20k
# The script downloads 1.csv, 2.csv.... num_files.csv
# and stores it in base_dir/datasets--open-spaced-repetition--FSRS-Anki-20k/snapshots
# one can then manually copy and paste the csvs to desired location (dataset directory)

# Pre-req your hugging face token as HF_TOKEN environmental variable
# Also access FSRS-Anki-20k using your hugging face account on the web interface at least once
# (to agree to the EULA)

import os

from huggingface_hub import hf_hub_download, HfFolder

Hftoken = os.environ.get("HF_TOKEN")
HfFolder.save_token(Hftoken)

dataset_name = "open-spaced-repetition/FSRS-Anki-20k"
subset_folder = "dataset/1"
num_files = 50

base_dir = os.path.join(os.getcwd(), 'datasets')

for i in range(1, num_files + 1):
    filename = f"{subset_folder}/{i}.csv"
    try:
        filepath = hf_hub_download(dataset_name, filename, repo_type='dataset', cache_dir=base_dir)
        print(f"Downloaded {filename} to {filepath}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
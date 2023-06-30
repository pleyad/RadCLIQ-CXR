import csv
from pathlib import Path
from tqdm import tqdm

PREDICTIONS_PATH = Path("predictions")
PREP_PRED_PATH = Path("predictions_prep")

PREP_PRED_PATH.mkdir(exist_ok=True)

paths = list(PREDICTIONS_PATH.glob("*.csv"))

for path in tqdm(paths):
    with path.open() as in_file:
        reader = csv.DictReader(in_file, delimiter=";")
        with (PREP_PRED_PATH / path.name).open("w") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["study_id", "report"])
            writer.writeheader()
            for row in reader:
                study_id = row["id"]
                report = row["report"]
                writer.writerow({"study_id": study_id, "report": report})

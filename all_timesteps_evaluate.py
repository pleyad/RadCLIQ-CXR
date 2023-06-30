from CXRMetric.run_eval import calc_metric
import os
from pathlib import Path

DATADIR = Path("predictions2_prep")

# Run on cuda 1
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

for i in range(100, 2500, 100):
    gt_reports = DATADIR / f"gold_global_step{i}.csv"
    predicted_reports = DATADIR / f"predictions_global_step{i}.csv"
    out_file = f"metrics2/{i}_metrics.csv"

    calc_metric(str(gt_reports), str(predicted_reports), out_file)

import config
from CXRMetric.run_eval import calc_metric
import os

gt_reports = config.GT_REPORTS
predicted_reports = config.PREDICTED_REPORTS
out_file = config.OUT_FILE

# Run on cuda 1
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

if __name__ == "__main__":
    calc_metric(gt_reports, predicted_reports, out_file)

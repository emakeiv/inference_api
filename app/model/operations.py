from joblib import load
from pathlib import Path

import numpy as np
__version__ = "0.1.0"

BASER_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASER_DIR}/rfr_base_model.joblib", "rb") as f:
      model = load(f) 


def predict(input):
      x = np.array(input).reshape(1, len(input))
      print(x)
      predictions = model.predict(x)
      return predictions
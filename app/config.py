"""Central configuration for the CV platform.

Keeping settings in one place means v0.0.3 (model selection) is a small
change here, not a hunt across the codebase.
"""
from pathlib import Path

# The pretrained model to serve. Any image-classification model on the
# Hugging Face Hub works here — swap this string to change models.
MODEL_NAME = "google/vit-base-patch16-224"

# How many top predictions to return.
TOP_K = 3

# Where to store things. Resolves relative to the project root.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
UPLOADS_DIR = PROJECT_ROOT / "data" / "uploads"
MODELS_DIR = PROJECT_ROOT / "models"

# Where prediction history is stored (SQLite file).
DB_PATH = PROJECT_ROOT / "data" / "predictions.db"
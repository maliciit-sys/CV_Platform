"""Model loading and prediction — the 'brain'.

This module knows nothing about the UI. It exposes one job: take an image,
return predictions. That boundary is what lets v0.0.4 split this into a
standalone API later without touching the prediction logic.
"""
from transformers import pipeline

from app import config

# Load the model once, at import time, not on every request.
# The first run downloads the weights (cached afterwards in ~/.cache).
_classifier = pipeline("image-classification", model=config.MODEL_NAME)


def predict(image):
    """Run classification on a PIL image.

    Returns a dict of {label: confidence} for the top-K predictions,
    which is the shape Gradio's Label component expects.
    """
    results = _classifier(image, top_k=config.TOP_K)
    return {item["label"]: float(item["score"]) for item in results}
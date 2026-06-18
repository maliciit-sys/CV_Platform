"""Persistence layer — saving and retrieving prediction history.

This module owns all database access. The UI (main.py) and the model
(inference.py) know nothing about how data is stored. That boundary is what
lets you swap SQLite for a real database later without touching the rest.
"""
import json
import sqlite3
import uuid
from datetime import datetime

from app import config


def _connect():
    # A fresh connection per call keeps things thread-safe under Gradio.
    return sqlite3.connect(config.DB_PATH)


def init_db():
    """Create the table if it doesn't exist. Safe to call on every startup."""
    config.UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
    with _connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS predictions (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at  TEXT NOT NULL,
                image_path  TEXT NOT NULL,
                top_label   TEXT NOT NULL,
                top_score   REAL NOT NULL,
                all_scores  TEXT NOT NULL
            )
            """
        )


def save_prediction(image, predictions):
    """Persist an uploaded image and its predictions.

    image: a PIL image.  predictions: dict of {label: score}.
    """
    # Save the image with a unique, time-stamped name.
    filename = f"{datetime.now():%Y%m%d_%H%M%S}_{uuid.uuid4().hex[:8]}.png"
    image_path = config.UPLOADS_DIR / filename
    image.save(image_path)

    # Top prediction = highest score.
    top_label, top_score = max(predictions.items(), key=lambda kv: kv[1])

    with _connect() as conn:
        conn.execute(
            "INSERT INTO predictions "
            "(created_at, image_path, top_label, top_score, all_scores) "
            "VALUES (?, ?, ?, ?, ?)",
            (
                datetime.now().isoformat(timespec="seconds"),
                str(image_path),
                top_label,
                float(top_score),
                json.dumps(predictions),
            ),
        )


def get_history(limit=50):
    """Return recent predictions as rows for the history table."""
    with _connect() as conn:
        rows = conn.execute(
            "SELECT created_at, top_label, top_score FROM predictions "
            "ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [[ts, label, f"{score:.1%}"] for ts, label, score in rows]
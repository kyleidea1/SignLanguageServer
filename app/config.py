import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / 'uploads'
PROCESSED_FOLDER = BASE_DIR / 'processed'
FRAMES_FOLDER = BASE_DIR / 'frames'

def ensure_dir(directory):
    directory = Path(directory)
    if not directory.exists():
        directory.mkdir(parents=True, exist_ok=True)

def configure_app(app):
    ensure_dir(UPLOAD_FOLDER)
    ensure_dir(PROCESSED_FOLDER)
    ensure_dir(FRAMES_FOLDER)
    ensure_dir(FRAMES_FOLDER / '0')

    app.config['UPLOAD_FOLDER'] = str(UPLOAD_FOLDER)
    app.config['PROCESSED_FOLDER'] = str(PROCESSED_FOLDER)
    app.config['FRAMES_FOLDER'] = str(FRAMES_FOLDER)
    app.config['FRAMES_SUBFOLDER'] = str(FRAMES_FOLDER / '0')
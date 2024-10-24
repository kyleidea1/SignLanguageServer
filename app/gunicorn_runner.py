import sys
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def run_gunicorn(app):
    print(f"Upload folder: {app.config['UPLOAD_FOLDER']}")
    print(f"Processed folder: {app.config['PROCESSED_FOLDER']}")
    print(f"Frames folder: {app.config['FRAMES_FOLDER']}")

    gunicorn_command = [
        'gunicorn',
        '--bind', '0.0.0.0:5001',
        '--chdir', str(BASE_DIR),
        'main:application'
    ]

    try:
        subprocess.run(gunicorn_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to start gunicorn: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print("gunicorn not found. Make sure it's installed and in your PATH.", file=sys.stderr)
        sys.exit(1)
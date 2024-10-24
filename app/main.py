import os
from pathlib import Path
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from routes import register_routes
from config import configure_app

# 환경 변수 로드
load_dotenv()

# 앱 생성 및 설정
app = Flask(__name__)
configure_app(app)
CORS(app)

# 라우트 등록
register_routes(app)

# WSGI application
application = app

if __name__ == '__main__':
    from gunicorn_runner import run_gunicorn
    run_gunicorn(app)
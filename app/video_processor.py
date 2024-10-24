import os
import shutil
import subprocess
from pathlib import Path
import ffmpeg
from openai_helper import ask_chatgpt
from dummy_pytorch_model import process_frames
from config import UPLOAD_FOLDER, PROCESSED_FOLDER, FRAMES_FOLDER, ensure_dir

def cleanup_directories():
    """작업 디렉토리들을 초기화합니다."""
    for directory in [UPLOAD_FOLDER, FRAMES_FOLDER, PROCESSED_FOLDER]:
        dir_path = str(directory)  # Path 객체를 문자열로 변환
        if os.path.exists(dir_path):
            try:
                # 디렉토리 내 모든 파일과 하위 디렉토리 삭제
                for filename in os.listdir(dir_path):
                    file_path = os.path.join(dir_path, filename)
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
            except Exception as e:
                print(f"Error while cleaning directory {dir_path}: {e}")
        
        # 디렉토리가 없으면 새로 생성
        ensure_dir(directory)
    
    # frames/0 디렉토리 특별 처리
    frames_subfolder = FRAMES_FOLDER / '0'
    ensure_dir(frames_subfolder)
    
    # 정리 완료 후 확인 로그
    print("Directories cleaned up:")
    print(f"UPLOAD_FOLDER contents: {os.listdir(str(UPLOAD_FOLDER))}")
    print(f"FRAMES_FOLDER contents: {os.listdir(str(FRAMES_FOLDER))}")
    print(f"PROCESSED_FOLDER contents: {os.listdir(str(PROCESSED_FOLDER))}")

def process_video_file(video_file):
    try:
        cleanup_directories()
        # 1. 비디오 파일 임시 저장
        video_path = UPLOAD_FOLDER / video_file.filename
        video_file.save(str(video_path))
        
        # 2. 프레임 추출
        subfolder = FRAMES_FOLDER / '0'
        output_pattern = str(subfolder / f'frame_%04d.jpg')
        command = f"ffmpeg -i {video_path} -vf fps=30 {output_pattern}"
        subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        
        # 3. 프레임 처리 및 텍스트 추출
        output_text_file = PROCESSED_FOLDER / f"{video_file.filename.split('.')[0]}_output.txt"
        mixed_words = process_frames(str(subfolder), str(output_text_file))
        
        # 4. ChatGPT를 통한 자연스러운 문장 생성
        words = mixed_words.split()
        natural_sentence = ask_chatgpt(words)
        
        # 5. 텍스트 파일 내용 읽기
        text_content = ""
        if output_text_file.exists():
            with open(output_text_file, 'r', encoding='utf-8') as f:
                text_content = f.read()
        
        # 6. 모든 임시 파일 및 디렉토리 정리
        cleanup_directories()
        
        return {
            'message': 'Video processed successfully',
            'natural_sentence': natural_sentence or "자연스러운 문장을 생성할 수 없습니다."
        }
        
    except Exception as e:
        cleanup_directories()
        return {
            'message': str(e),  # 에러 메시지
            'natural_sentence': None
        }
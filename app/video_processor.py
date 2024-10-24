import os
import shutil
import subprocess
from pathlib import Path
import ffmpeg
from openai_helper import ask_chatgpt
from dummy_pytorch_model import process_frames
from config import UPLOAD_FOLDER, PROCESSED_FOLDER, FRAMES_FOLDER, ensure_dir

def ensure_frames_subfolder():
    subfolder = FRAMES_FOLDER / '0'
    ensure_dir(subfolder)
    return subfolder

def split_video_to_frames(video_path):
    subfolder = FRAMES_FOLDER / '0'
    if subfolder.exists():
        shutil.rmtree(subfolder)
    ensure_dir(subfolder)
    print(f"Initialized subfolder: {subfolder}")
    print(f"Splitting video to frames in: {subfolder}")
    output_pattern = str(subfolder / f'frame_%04d.jpg')
    print(f"Output pattern: {output_pattern}")
    
    command = f"ffmpeg -i {video_path} -vf fps=30 {output_pattern}"
    print(f"Executing command: {command}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("ffmpeg stdout:", result.stdout)
        print("ffmpeg stderr:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        print("ffmpeg stdout:", e.stdout)
        print("ffmpeg stderr:", e.stderr)
    
    print(f"Frames after splitting: {list(subfolder.glob('*.jpg'))}")

def process_video_file(video_file):
    video_path = UPLOAD_FOLDER / video_file.filename
    video_file.save(str(video_path))
    print(f"Saved video file to: {video_path}")

    print(f"Frames before splitting: {list((FRAMES_FOLDER / '0').glob('*.jpg'))}")
    split_video_to_frames(str(video_path))
    print(f"Frames after splitting: {list((FRAMES_FOLDER / '0').glob('*.jpg'))}")

    output_text_file = PROCESSED_FOLDER / f"{video_file.filename.split('.')[0]}_output.txt"
    subfolder = ensure_frames_subfolder()
    print(f"Processing frames from: {subfolder}")
    print(f"Frames before processing: {list(subfolder.glob('*.jpg'))}")
    mixed_words = process_frames(str(subfolder), str(output_text_file))
    print(f"Frames after processing: {list(subfolder.glob('*.jpg'))}")

    words = mixed_words.split()
    natural_sentence = ask_chatgpt(words)

    print(f"Mixed words: {mixed_words}")
    print(f"Natural sentence: {natural_sentence}")

    return {
        'message': 'Video processed successfully',
        'mixed_words': mixed_words or "단어를 추출할 수 없습니다.",
        'natural_sentence': natural_sentence or "자연스러운 문장을 생성할 수 없습니다."
    }
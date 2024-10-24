from flask import request, jsonify
from video_processor import process_video_file

def register_routes(app):
    @app.route("/", methods=["GET"])
    def index():
        return jsonify({'success': 'hihi'}), 200

    @app.route('/process_video', methods=['POST'])
    def process_video():
        if 'video' not in request.files:
            return jsonify({'error': 'No video file in the request'}), 400

        video_file = request.files['video']
        if video_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if video_file:
            result = process_video_file(video_file)
            return jsonify(result), 200

        return jsonify({'error': 'Failed to process video'}), 500
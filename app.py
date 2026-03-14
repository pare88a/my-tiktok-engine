from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Engine is Live!"

@app.route('/api/download', methods=['GET'])
def get_video():
    url = request.args.get('url')
    if not url: return jsonify({"error": "Link missing"}), 400
    if "youtube" in url or "youtu.be" in url:
        return jsonify({"error": "YouTube is blocked"}), 403
    try:
        ydl_opts = {'format': 'best', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return jsonify({"success": True, "download_link": info.get('url')})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()

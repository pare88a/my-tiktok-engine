from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)

@app.route('/api/download', methods=['GET'])
def download():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"success": False, "error": "No URL"})
    
    try:
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'no_warnings': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            return jsonify({
                "success": True, 
                "download_link": info.get('url'),
                "title": info.get('title')
            })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

# Vercel Runtime
app = app

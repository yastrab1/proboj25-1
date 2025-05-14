import os
import tempfile

import librosa
import yt_dlp


# Step 1: Download audio to a temp file
def downloadYTMusic(url):
    with tempfile.NamedTemporaryFile(suffix='.m4a', delete=False) as tmp_file:
        temp_audio_path = tmp_file.name

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': temp_audio_path,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Step 2: Load audio to numpy array
    y, sr = librosa.load(temp_audio_path, sr=None)

    # Cleanup
    os.remove(temp_audio_path)

    return y, sr

def extractBeats(audio_path):
    y, sr = librosa.load(audio_path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    return librosa.frames_to_time(beat_frames, sr=sr)

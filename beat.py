import os
import random
import tempfile

import librosa
import yt_dlp


# Step 1: Download audio to a temp file
def downloadYTMusic(url):
    import tempfile
    tempDir = tempfile.gettempdir()
    pathName = random.randint(0,1000000)
    temp_audio_path = tempDir + f"/{pathName}.%(ext)s"
    ydl_opts = {
        'outtmpl': temp_audio_path,
        'format': 'bestaudio/best',
        'quiet': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


    return tempDir+f"/{pathName}.mp3"

def extractBeats(path):
    print(path)
    y,sr = librosa.load(path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    return librosa.frames_to_time(beat_frames, sr=sr),tempo

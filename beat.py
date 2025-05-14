import librosa

# Load the audio file
filename = './songs/Brano Mojsej- Pijeme fernet cez internet (Official Video) [SsRH4wZrzrg].mp3'  # Replace with your file path
y, sr = librosa.load(filename)

# Estimate tempo (BPM)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

print(f"Estimated BPM: {tempo}")

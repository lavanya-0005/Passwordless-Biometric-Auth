# ===== IMPORTS (MUST BE AT TOP) =====
import librosa
import numpy as np
import pickle
import os
import sounddevice as sd

# ===== PATH SETUP =====
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data", "voice_features")

os.makedirs(DATA_DIR, exist_ok=True)
# =====================

def voice_login():
    duration = 3  # seconds
    sr = 22050

    print("Recording voice...")
    audio = sd.rec(int(duration * sr), samplerate=sr, channels=1)
    sd.wait()

    audio = audio.flatten()

    # Safety checks
    if audio.size == 0:
        print("Empty audio")
        return False

    audio = np.nan_to_num(audio)

    if not np.isfinite(audio).all():
        print("Invalid audio values")
        return False

    # Feature extraction
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    features = np.mean(mfcc.T, axis=0)

    # No registered voices yet
    if len(os.listdir(DATA_DIR)) == 0:
        print("No registered voice found")
        return False

    # Compare with stored voices
    for file in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, file)
        with open(file_path, "rb") as f:
            stored = pickle.load(f)

        if np.linalg.norm(stored - features) < 50:
            return True

    return False
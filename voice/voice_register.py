import os
import json
import sqlite3
import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import numpy as np

os.makedirs("recordings", exist_ok=True)


def register_voice(username):

    username = username.strip()

    if username == "":
        print("Username cannot be empty.")
        return False

    sample_rate = 44100
    duration = 5

    print(f"Recording voice for {username}...")
    print("Speak now...")
    print(sd.query_devices())
    print("Default Device:", sd.default.device)

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    filename = f"recordings/{username}.wav"

    write(filename, sample_rate, recording)

    audio, sr = librosa.load(filename, sr=None)

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=13
    )

    features = np.mean(
        mfcc.T,
        axis=0
    ).tolist()

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO users
        (username, voice_features)
        VALUES (?, ?)
        """,
        (
            username,
            json.dumps(features)
        )
    )

    conn.commit()
    conn.close()

    print("Voice registered successfully.")

    return True

import json
import sqlite3
import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def voice_login(username):

    username = username.strip()

    if username == "":
        print("Username cannot be empty.")
        return False

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT voice_features FROM users WHERE username=?",
        (username,)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        print("User not found.")
        return False

    stored_features = np.array(
        json.loads(row[0])
    ).reshape(1, -1)

    sample_rate = 44100
    duration = 5

    print(f"Recording login voice for {username}...")
    print("Speak now...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32"
    )

    sd.wait()

    filename = "recordings/login.wav"

    write(filename, sample_rate, recording)

    audio, sr = librosa.load(filename, sr=None)

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=13
    )

    login_features = np.mean(
        mfcc.T,
        axis=0
    ).reshape(1, -1)

    similarity = cosine_similarity(
        login_features,
        stored_features
    )[0][0]

    print(f"Similarity Score: {similarity}")

    if similarity >= 0.85:
        print("Login Successful")
        return True

    print("Login Failed")
    return False
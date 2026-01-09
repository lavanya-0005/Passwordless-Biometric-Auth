import librosa, numpy as np, sounddevice as sd
import pickle

def register_voice(username):
    audio = sd.rec(int(3 * 22050), samplerate=22050, channels=1)
    sd.wait()


    mfcc = librosa.feature.mfcc(y=audio.flatten(), sr=22050)
    features = np.mean(mfcc, axis=1)

    with open(f"data/voice_features/{username}.pkl", "wb") as f:
        pickle.dump(features, f)
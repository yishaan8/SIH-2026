import librosa
import numpy as np


TARGET_SAMPLE_RATE = 16000


def preprocess_audio(audio_path: str):

    # load audio as mono and resample to 16 kHz
    audio, sample_rate = librosa.load(
        audio_path,
        sr=TARGET_SAMPLE_RATE,
        mono=True
    )

    if len(audio) == 0:
        raise ValueError("Audio file is empty.")

    # trim leading and trailing silence
    audio, _ = librosa.effects.trim(
        audio,
        top_db=30
    )

    if len(audio) == 0:
        raise ValueError(
            "No usable audio found after silence removal."
        )

    # Normalize amplitude
    max_amplitude = np.max(np.abs(audio))

    if max_amplitude > 0:
        audio = audio / max_amplitude

    return audio, TARGET_SAMPLE_RATE
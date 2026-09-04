import whisper


print("Loading Whisper model...")

model = whisper.load_model("base")

print("Whisper loaded successfully!")


def transcribe_audio(audio_path: str):

    result = model.transcribe(
        audio_path,
        fp16=False
    )

    return result["text"].strip()


if __name__ == "__main__":

    audio_path = "data/test.wav"

    transcript = transcribe_audio(audio_path)

    print("Transcription Result")
    print("==============================")
    print(transcript)
    print("==============================")
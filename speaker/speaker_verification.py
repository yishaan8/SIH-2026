from speechbrain.inference.speaker import SpeakerRecognition


print("Loading speaker verification model...")

verification = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="pretrained_models/spkrec-ecapa-voxceleb"
)

print("Model loaded successfully!")


def compare_speakers(reference_audio, test_audio):

    score, prediction = verification.verify_files(
        reference_audio,
        test_audio
    )

    return float(score), bool(prediction)


if __name__ == "__main__":

    reference_audio = "data/reference.wav"
    test_audio = "data/test.wav"

    score, prediction = compare_speakers(
        reference_audio,
        test_audio
    )

    print("\n==============================")
    print("Speaker Verification Result")
    print("==============================")
    print(f"Similarity Score : {score:.4f}")
    print(f"Speaker Match    : {prediction}")
    print("==============================")
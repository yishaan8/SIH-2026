import torch
from transformers import AutoFeatureExtractor, AutoModelForAudioClassification

from preprocess import preprocess_audio


MODEL_NAME = "Vansh180/deepfake-audio-wav2vec2"


print("Loading audio feature extractor...")

feature_extractor = AutoFeatureExtractor.from_pretrained(MODEL_NAME)


print("Loading deepfake audio model...")

model = AutoModelForAudioClassification.from_pretrained(MODEL_NAME)

model.eval()

print("Model loaded successfully!")


def detect_deepfake(audio_path: str):

    # Step 1: Preprocess audio
    audio, sample_rate = preprocess_audio(audio_path)

    # Step 2: Convert audio into model input
    inputs = feature_extractor(
        audio,
        sampling_rate=sample_rate,
        return_tensors="pt"
    )

    # Step 3: Run AI inference
    with torch.no_grad():

        outputs = model(**inputs)

        probabilities = torch.softmax(
            outputs.logits,
            dim=-1
        )[0]

    # Step 4: Read model labels
    id2label = model.config.id2label

    print("\nModel probabilities:")

    for index, probability in enumerate(probabilities):

        label = id2label[index]

        print(
            label,
            ":",
            round(float(probability), 4)
        )

    # Step 5: Get fake probability
    fake_probability = 0.0

    for index, probability in enumerate(probabilities):

        label = id2label[index].lower()

        if label == "fake":
            fake_probability = float(probability)

    return fake_probability


if __name__ == "__main__":

    audio_path = "test_audio/test.wav"

    probability = detect_deepfake(audio_path)

    print()
    print("================================")
    print("Deepfake Audio Detection Result")
    print("================================")
    print(
        "Deepfake Probability:",
        round(probability, 4)
    )
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from speaker.speaker_verification import compare_speakers
from conversation.speech_to_text import transcribe_audio
from conversation.fraud_detector import detect_fraud_signals

from speaker.speaker_verification import compare_speakers
from conversation.speech_to_text import transcribe_audio
from conversation.fraud_detector import detect_fraud_signals


REFERENCE_AUDIO = "data/reference.wav"
TEST_AUDIO = "data/test.wav"


def analyze_call(reference_audio, test_audio):

    
    speaker_score, speaker_match = compare_speakers(
        reference_audio,
        test_audio
    )

   
    transcript = transcribe_audio(test_audio)

   
    fraud_signals = detect_fraud_signals(transcript)

    return {
        "speakerSimilarity": speaker_score,
        "speakerMatch": speaker_match,
        "transcript": transcript,
        "fraudSignals": fraud_signals
    }


if __name__ == "__main__":

    result = analyze_call(
        REFERENCE_AUDIO,
        TEST_AUDIO
    )

    print("Call Analysis Result")
    print("================================")

    print(f"Speaker Similarity : {result['speakerSimilarity']:.4f}")
    print(f"Speaker Match      : {result['speakerMatch']}")

    print("\nTranscript:")
    print(result["transcript"])

    print("\nFraud Signals:")

    for key, value in result["fraudSignals"].items():
        print(f"  {key}: {value}")

    print("================================")
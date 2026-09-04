import os
import sys

from fastapi import FastAPI, UploadFile, File


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.append(PROJECT_ROOT)

from conversation.m2_pipeline import analyze_call


app = FastAPI(
    title="VoiceGuard M2 AI Service",
    description="Speaker verification and conversation fraud analysis"
)


@app.post("/ai/analyze")
async def analyze(
    reference_audio: UploadFile = File(...),
    test_audio: UploadFile = File(...)
):

    reference_path = os.path.join(
        "data",
        "api_reference.wav"
    )

    test_path = os.path.join(
        "data",
        "api_test.wav"
    )

    
    with open(reference_path, "wb") as f:
        f.write(await reference_audio.read())

    with open(test_path, "wb") as f:
        f.write(await test_audio.read())

  
    result = analyze_call(
        reference_path,
        test_path
    )

    
    os.remove(reference_path)
    os.remove(test_path)

    return result
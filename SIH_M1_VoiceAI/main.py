from fastapi import FastAPI, UploadFile, File
import tempfile
import os

from detector import detect_deepfake


app = FastAPI(
    title="SIH M1 Voice Deepfake Detection API"
)


@app.get("/")
def root():
    return {
        "service": "Voice Deepfake Detection",
        "status": "running"
    }


@app.post("/detect")
async def detect_audio(file: UploadFile = File(...)):

    temp_file = tempfile.NamedTemporaryFile(   #temporary file to store uploaded audio
        delete=False,
        suffix=".wav"
    )

    try:

        # Save uploaded audio
        contents = await file.read()

        temp_file.write(contents)
        temp_file.close()

        # Run AI detection
        probability = detect_deepfake(
            temp_file.name
        )

        return {
            "filename": file.filename,
            "deepfakeProbability": round(
                probability,
                4
            )
        }

    finally:

        if os.path.exists(temp_file.name):
            os.remove(temp_file.name)
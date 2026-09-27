"""Speech-to-text adapter for SnapLearn Edge.

Production target:
- Qualcomm AI Hub Whisper-Small-Quantized or Whisper-Base
- ONNX Runtime / Qualcomm execution provider on Snapdragon X-class Windows PCs

The repository intentionally does not redistribute model binaries.
"""
from pathlib import Path


def transcribe_audio(audio_path: str | Path) -> str:
    path = Path(audio_path)
    if not path.exists():
        raise FileNotFoundError(path)

    # Integration point for Qualcomm AI Hub exported Whisper model.
    # The challenge prototype keeps model weights outside the repository.
    return (
        "[Prototype transcript placeholder] Audio received successfully. "
        "Install/export a Qualcomm AI Hub Whisper model and connect the ONNX/QNN "
        "execution session in src/transcribe.py for on-device transcription."
    )

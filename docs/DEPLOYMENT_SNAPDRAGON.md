# Snapdragon Deployment Guide

## Target
Windows 11 on a Snapdragon-powered HP PC using Snapdragon X-class silicon.

## 1. Create the Python environment
```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 2. Obtain compatible AI models
Use Qualcomm AI Hub / Qualcomm AI Hub Workbench to obtain or compile:
- **Whisper-Small-Quantized** or **Whisper-Base** for speech recognition.
- **Llama-v3.2-3B-Instruct** for local text generation and Q&A.

Do not commit model weights to this repository unless their individual licenses and redistribution terms explicitly permit it.

## 3. Connect speech inference
Place exported assets under `models/whisper/` and replace the placeholder in `src/transcribe.py` with the ONNX Runtime / Qualcomm execution-provider session.

## 4. Connect LLM inference
Place the Qualcomm-compatible package under `models/llama32_3b/` and replace the placeholder in `src/summarize.py` with GenieX / QAIRT inference.

## 5. Run the application
```powershell
streamlit run app.py
```

## 6. Validate on target hardware
Record:
- time to transcript;
- time to first generated token;
- tokens per second;
- peak memory;
- battery/power observations;
- CPU-only vs NPU-accelerated comparison where possible.

Those measured values should be added to the final submission only after actual device testing.

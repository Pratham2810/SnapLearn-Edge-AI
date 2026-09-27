# ⚡ SnapLearn Edge

**A privacy-first, on-device AI lecture and meeting copilot designed for Snapdragon-powered HP PCs.**

SnapLearn Edge converts recorded lectures, meetings and voice notes into transcripts, structured notes, action items, revision questions and contextual Q&A. The core deployment concept is to run speech recognition and text generation locally on Snapdragon X-class Windows PCs using models available through Qualcomm AI Hub, reducing reliance on cloud inference.

> **Challenge positioning:** newly created AI use case intended to be optimized for Snapdragon-powered HP PCs, with Qualcomm AI Hub/open-source model integration.

![SnapLearn Edge](assets/hero.png)

## Why this matters
Students and knowledge workers increasingly rely on AI to process lectures and meetings, but cloud-first workflows can introduce privacy concerns, connectivity dependence, latency and recurring inference cost. SnapLearn Edge is designed around an **offline-first edge AI workflow**: sensitive audio and derived knowledge can remain on the PC.

## Core user flow
1. Upload or capture lecture/meeting audio.
2. Transcribe locally with a Qualcomm AI Hub Whisper model.
3. Generate structured smart notes with an on-device LLM.
4. Ask grounded questions from the session context.
5. Export results for revision, documentation or follow-up.

## Proposed Snapdragon AI stack
- **Speech recognition:** Whisper-Small-Quantized / Whisper-Base from Qualcomm AI Hub.
- **Local reasoning & generation:** Llama-v3.2-3B-Instruct from Qualcomm AI Hub.
- **Target platform:** Windows 11 on Snapdragon-powered HP PCs.
- **Acceleration path:** Qualcomm NPU through AI Hub-compatible runtimes such as ONNX Runtime/QNN for ASR and GenieX/QAIRT for the LLM deployment path.

## Repository structure
```text
SnapLearn-Edge-AI/
├── app.py
├── src/
│   ├── config.py
│   ├── transcribe.py
│   └── summarize.py
├── docs/
│   ├── Project_Description.pdf
│   ├── Project_Description.docx
│   ├── Pitch_Deck.pdf
│   ├── Pitch_Deck.pptx
│   ├── TECHNICAL_ARCHITECTURE.md
│   ├── DEPLOYMENT_SNAPDRAGON.md
│   ├── CHALLENGE_MAPPING.md
│   └── MODELS.md
├── models/
│   └── README.md
├── assets/
│   └── hero.png
├── examples/
│   └── sample_transcript.txt
├── requirements.txt
└── LICENSE
```

## Run the prototype UI
```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

The prototype demonstrates the product workflow and model-adapter boundaries without redistributing third-party model binaries. See [`docs/DEPLOYMENT_SNAPDRAGON.md`](docs/DEPLOYMENT_SNAPDRAGON.md) for the target-device integration path.

## Challenge evaluation coverage
**Technical Implementation** — modular ASR + LLM pipeline, device-targeted adapter design, model/runtime separation.

**Application Use Case & Innovation** — a private AI study/meeting copilot that can work locally rather than requiring every recording to leave the device.

**Deployment & Accessibility** — simple Windows/Python setup, evaluator-friendly UI, documented Snapdragon integration path.

**Presentation & Documentation** — proposal PDF/DOCX, pitch deck PDF/PPTX, architecture, deployment and model documentation.

## Submission artifacts
- [Project Description PDF](docs/Project_Description.pdf)
- [Project Description DOCX](docs/Project_Description.docx)
- [Pitch Deck PDF](docs/Pitch_Deck.pdf)
- [Pitch Deck PPTX](docs/Pitch_Deck.pptx)
- [Challenge Mapping](docs/CHALLENGE_MAPPING.md)
- [Snapdragon Deployment Guide](docs/DEPLOYMENT_SNAPDRAGON.md)

## Current implementation status
This repository is a challenge-ready prototype/scaffold. The UI and application flow are present; model binaries are deliberately excluded. Hardware-specific NPU inference must be connected and benchmarked on the target Snapdragon-powered HP PC before claiming measured latency, throughput or power figures.

## Author
**Pratham Priyanshu Mohanty**

## License
Project source code: MIT License. Third-party AI models remain subject to their own licenses and platform terms.

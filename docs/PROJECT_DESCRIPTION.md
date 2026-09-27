# SnapLearn Edge — Project Description

**SnapLearn Edge** is a privacy-first AI application concept for students and knowledge workers. It turns lecture, meeting and voice-note audio into a transcript, structured notes, action items, revision questions and contextual Q&A.

The product is designed around an **offline-first architecture for Snapdragon-powered HP PCs**. Instead of making cloud inference a requirement, the target implementation keeps speech recognition and text generation on the device wherever possible.

## Problem

Cloud-first transcription and generative-AI tools can require users to upload sensitive recordings, depend on stable internet connectivity, introduce latency and create recurring inference cost. Those constraints are particularly relevant for classroom lectures, internal meetings and personal notes.

## Proposed solution

The user uploads or captures audio. SnapLearn Edge transcribes it, structures the transcript into useful notes, identifies decisions and action items, generates revision questions and supports Q&A grounded in the session context.

## AI and Snapdragon plan

- **Speech-to-text:** Qualcomm AI Hub Whisper-Small-Quantized or Whisper-Base.
- **Local reasoning / generation:** Llama 3.2 3B Instruct.
- **Target platform:** Windows 11 on Snapdragon-powered HP PCs.
- **Deployment principle:** keep the UI separate from model-adapter code so Qualcomm-compatible runtimes and NPU execution can be integrated without redesigning the application.

## Why the use case is innovative

The differentiator is not simply summarising audio. SnapLearn Edge is designed as a **private edge-AI knowledge companion**: one workflow that can operate with reduced cloud dependence, preserve sensitive context on the PC and remain useful even when connectivity is limited.

## Deployment and accessibility

The repository provides a simple Streamlit interface, a Python setup path, external model folders, technical architecture notes and a Snapdragon deployment guide. Third-party model binaries are intentionally excluded from source control.

## Current prototype status

The UI and application flow are implemented as a challenge prototype/scaffold. Model-adapter integration points are present and documented. Hardware-specific NPU inference and benchmark measurements must still be validated on the target Snapdragon-powered HP PC before latency, throughput or power claims are made.

## Evaluation alignment

The repository is organised around the challenge criteria: **Technical Implementation, Application Use Case & Innovation, Deployment & Accessibility, and Presentation & Documentation**.

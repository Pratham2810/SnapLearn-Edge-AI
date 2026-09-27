# Technical Architecture

## Objective
SnapLearn Edge is a privacy-first lecture and meeting copilot designed to keep audio, transcripts, notes and question-answering on the user's Snapdragon-powered HP PC wherever possible.

## Processing pipeline
1. **Audio capture / upload** — lecture, meeting or personal voice note.
2. **On-device ASR** — Qualcomm AI Hub Whisper-Small-Quantized or Whisper-Base.
3. **Transcript chunking** — timestamps and logical segments are prepared locally.
4. **On-device LLM** — Llama-v3.2-3B-Instruct converts transcript chunks into structured notes, action items, revision questions and grounded Q&A.
5. **Local storage/export** — Markdown/PDF export without requiring cloud upload.

## Snapdragon optimization path
- Target OS: Windows 11+
- Target class: Snapdragon X Elite / X Plus HP PCs
- Speech runtime: ONNX Runtime with Qualcomm acceleration / QNN-compatible deployment path
- LLM runtime: Qualcomm GenieX / QAIRT, depending on exported package
- Quantization: use the Qualcomm AI Hub optimized model variants to reduce memory and power cost

## Why edge execution matters
- lower privacy exposure for sensitive lectures and meetings;
- useful without reliable Internet connectivity;
- avoids recurring cloud inference cost;
- enables continuous productivity workflows while keeping latency predictable.

## Prototype status
The repository contains a functional Streamlit interface and clearly defined model-adapter boundaries. Model binaries are not redistributed. Hardware-specific inference must be connected after exporting/downloading the corresponding Qualcomm AI Hub assets and testing on the target Snapdragon-powered HP PC.

# Challenge Evaluation Mapping

## 1. Technical Implementation
- Modular on-device AI pipeline: audio → ASR → transcript → LLM → notes/Q&A.
- Qualcomm AI Hub model integration points are explicitly separated from the UI.
- Designed for Windows 11 Snapdragon-powered HP PCs and NPU-accelerated inference.
- Model binaries remain external to the repo to respect licensing and simplify device-specific deployment.

## 2. Application Use Case & Innovation
- Converts lectures and meetings into private transcripts, concise notes, action items, revision questions and contextual Q&A.
- Emphasizes **offline-first, privacy-first learning**, rather than sending every recording to a cloud service.
- Useful to students, educators, analysts, consultants and knowledge workers.

## 3. Deployment & Accessibility
- Simple local Streamlit interface.
- Runs from a standard Python environment.
- Deployment guide explains the Snapdragon model-integration path.
- Accessible workflow: upload audio → generate notes → ask questions → export.

## 4. Presentation & Documentation
- Project description PDF/DOCX included.
- 2-core-slide pitch deck included as PDF/PPTX.
- Architecture, deployment, model and challenge-mapping documents included.
- README provides evaluator-friendly navigation.

## Eligibility alignment
SnapLearn Edge is proposed as a newly created solution intended to be optimized for Snapdragon-powered HP PCs using AI models available through Qualcomm AI Hub/open-source ecosystems.

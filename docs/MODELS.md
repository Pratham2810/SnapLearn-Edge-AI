# Model Plan

| Component | Proposed model | Role | Snapdragon rationale |
|---|---|---|---|
| Speech-to-text | Whisper-Small-Quantized | Lecture/meeting transcription | Qualcomm AI Hub provides an optimized quantized Whisper variant for Snapdragon X-class compute devices. |
| Speech-to-text fallback | Whisper-Base | Lower-footprint transcription | Qualcomm AI Hub lists Windows/on-device Whisper support and Snapdragon X-class targets. |
| Text generation | Llama-v3.2-3B-Instruct | Summaries, notes, Q&A, action items | Qualcomm AI Hub lists a quantized on-device variant for Snapdragon X Elite/X Plus/X2 Elite compute devices. |

## Important
Performance numbers in this repository are not claimed as measurements from an HP Snapdragon PC. Final benchmark claims should be added only after target-device validation.

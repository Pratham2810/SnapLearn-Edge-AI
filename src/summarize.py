"""Local study-note and Q&A generation adapter.

Production target:
- Qualcomm AI Hub Llama-v3.2-3B-Instruct (quantized)
- GenieX / QAIRT on Snapdragon X-class Windows PCs
"""


def build_study_notes(transcript: str) -> str:
    clean = " ".join(transcript.split())
    return f"""# Smart Notes\n\n## Session summary\n{clean}\n\n## Key takeaways\n- Important ideas are extracted locally from the transcript.\n- User data can remain on-device.\n- The production backend is designed for a Snapdragon NPU-optimized LLM.\n\n## Suggested revision prompts\n1. Explain the most important concept in simple terms.\n2. Create five exam-style questions from this session.\n3. Identify definitions, formulas, decisions, or action items.\n"""


def answer_question(question: str, transcript: str) -> str:
    return (
        f"Prototype local-Q&A response for: '{question}'.\n\n"
        "In the Snapdragon build, this function passes the transcript context and "
        "question to the on-device Llama 3.2 3B Instruct backend."
    )

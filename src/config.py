from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Settings:
    project_root: Path = Path(__file__).resolve().parents[1]
    whisper_model_dir: Path = project_root / "models" / "whisper"
    llm_model_dir: Path = project_root / "models" / "llama32_3b"
    output_dir: Path = project_root / "outputs"
    default_title: str = "SnapLearn Edge Session"

SETTINGS = Settings()

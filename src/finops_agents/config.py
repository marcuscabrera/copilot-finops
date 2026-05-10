from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    openai_model: str
    openai_base_url: str | None
    temperature: float
    max_tokens: int


def load_settings() -> Settings:
    return Settings(
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        openai_base_url=os.getenv("OPENAI_BASE_URL") or None,
        temperature=float(os.getenv("FINOPS_TEMPERATURE", "0.2")),
        max_tokens=int(os.getenv("FINOPS_MAX_TOKENS", "1200")),
    )

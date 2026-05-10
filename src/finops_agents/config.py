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
    temperature_value = os.getenv("FINOPS_TEMPERATURE", "0.2")
    max_tokens_value = os.getenv("FINOPS_MAX_TOKENS", "1200")
    try:
        temperature = float(temperature_value)
    except ValueError as exc:
        raise ValueError(
            f"FINOPS_TEMPERATURE inválido: '{temperature_value}'. Use um número decimal (float)."
        ) from exc
    try:
        max_tokens = int(max_tokens_value)
    except ValueError as exc:
        raise ValueError(
            f"FINOPS_MAX_TOKENS inválido: '{max_tokens_value}'. Use um número inteiro."
        ) from exc

    return Settings(
        openai_model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        openai_base_url=os.getenv("OPENAI_BASE_URL") or None,
        temperature=temperature,
        max_tokens=max_tokens,
    )

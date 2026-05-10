from __future__ import annotations

import os
from dataclasses import dataclass
from enum import Enum


class LLMProvider(str, Enum):
    """Provedores de LLM suportados via LiteLLM."""
    OPENAI = "openai"
    OLLAMA = "ollama"
    LMSTUDIO = "lmstudio"
    OPENROUTER = "openrouter"
    OPENCODE_ZEN = "opencode_zen"
    GOOGLE_GEMINI_API = "google_gemini_api"
    GOOGLE_GEMINI_OAUTH = "google_gemini_oauth"


@dataclass(frozen=True)
class Settings:
    llm_provider: LLMProvider
    model: str
    base_url: str | None
    api_key: str | None
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

    provider_str = os.getenv("LLM_PROVIDER", "openai").lower()
    try:
        llm_provider = LLMProvider(provider_str)
    except ValueError as exc:
        valid_providers = ", ".join(p.value for p in LLMProvider)
        raise ValueError(
            f"LLM_PROVIDER inválido: '{provider_str}'. Valores válidos: {valid_providers}"
        ) from exc

    model_map = {
        LLMProvider.OPENAI: os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        LLMProvider.OLLAMA: os.getenv("OLLAMA_MODEL", "llama3.1:8b"),
        LLMProvider.LMSTUDIO: os.getenv("LMSTUDIO_MODEL", "local-model"),
        LLMProvider.OPENROUTER: os.getenv("OPENROUTER_MODEL", "meta-llama/llama-3.1-8b-instruct"),
        LLMProvider.OPENCODE_ZEN: os.getenv("OPENCODE_ZEN_MODEL", "qwen-coder-plus"),
        LLMProvider.GOOGLE_GEMINI_API: os.getenv("GEMINI_MODEL", "gemini-1.5-flash"),
        LLMProvider.GOOGLE_GEMINI_OAUTH: os.getenv("GEMINI_MODEL", "gemini-1.5-flash"),
    }
    model = model_map[llm_provider]

    base_url_map = {
        LLMProvider.OPENAI: os.getenv("OPENAI_BASE_URL"),
        LLMProvider.OLLAMA: os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        LLMProvider.LMSTUDIO: os.getenv("LMSTUDIO_BASE_URL", "http://localhost:1234/v1"),
        LLMProvider.OPENROUTER: os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
        LLMProvider.OPENCODE_ZEN: os.getenv("OPENCODE_ZEN_BASE_URL"),
        LLMProvider.GOOGLE_GEMINI_API: None,
        LLMProvider.GOOGLE_GEMINI_OAUTH: None,
    }
    base_url = base_url_map.get(llm_provider)

    api_key_map = {
        LLMProvider.OPENAI: os.getenv("OPENAI_API_KEY"),
        LLMProvider.OLLAMA: os.getenv("OLLAMA_API_KEY", "ollama"),
        LLMProvider.LMSTUDIO: os.getenv("LMSTUDIO_API_KEY", "lm-studio"),
        LLMProvider.OPENROUTER: os.getenv("OPENROUTER_API_KEY"),
        LLMProvider.OPENCODE_ZEN: os.getenv("OPENCODE_ZEN_API_KEY"),
        LLMProvider.GOOGLE_GEMINI_API: os.getenv("GOOGLE_API_KEY"),
        LLMProvider.GOOGLE_GEMINI_OAUTH: None,
    }
    api_key = api_key_map.get(llm_provider)

    return Settings(
        llm_provider=llm_provider,
        model=model,
        base_url=base_url or None,
        api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens,
    )

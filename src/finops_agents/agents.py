from __future__ import annotations

from dataclasses import dataclass

from litellm import completion

from .config import LLMProvider, load_settings
from .knowledge import build_context
from .router import Provider, detect_provider


_PROMPTS = {
    Provider.AZURE: """
Você é um agente FinOps especializado em Azure/Microsoft.
Responda em português, de forma consultiva e acionável.
Sempre organize em: Contexto, Componentes de custo, Riscos/Caveats, Ações recomendadas, Próximos passos.
""".strip(),
    Provider.HUAWEI: """
Você é um agente FinOps especializado em Huawei Cloud.
Responda em português, de forma consultiva e acionável.
Sempre organize em: Contexto, Componentes de custo, Riscos/Caveats, Ações recomendadas, Próximos passos.
""".strip(),
    Provider.COMPARISON: """
Você é um agente FinOps de comparação Azure vs Huawei Cloud.
Responda em português com análise comparativa, suposições explícitas e limites da comparação.
Sempre organize em: Contexto, Componentes de custo, Riscos/Caveats, Ações recomendadas, Próximos passos.
""".strip(),
}


@dataclass(frozen=True)
class AgentResponse:
    provider: Provider
    answer: str


class FinOpsAgentSystem:
    def __init__(self) -> None:
        self._settings = load_settings()

    def _build_model_name(self) -> str:
        """Constrói o nome do modelo no formato esperado pelo LiteLLM."""
        settings = self._settings
        provider = settings.llm_provider

        if provider == LLMProvider.OPENAI:
            return f"openai/{settings.model}"
        elif provider == LLMProvider.OLLAMA:
            return f"ollama/{settings.model}"
        elif provider == LLMProvider.LMSTUDIO:
            return f"lm-studio/{settings.model}"
        elif provider == LLMProvider.OPENROUTER:
            return f"openrouter/{settings.model}"
        elif provider == LLMProvider.OPENCODE_ZEN:
            return f"openai/{settings.model}"
        elif provider == LLMProvider.GOOGLE_GEMINI_API:
            return f"gemini/{settings.model}"
        elif provider == LLMProvider.GOOGLE_GEMINI_OAUTH:
            return f"gemini/{settings.model}"
        else:
            return f"openai/{settings.model}"

    def _call_llm(self, messages: list[dict]) -> str:
        """Chama o LLM via LiteLLM."""
        settings = self._settings
        model_name = self._build_model_name()

        kwargs = {
            "model": model_name,
            "messages": messages,
            "temperature": settings.temperature,
            "max_tokens": settings.max_tokens,
        }

        if settings.base_url:
            kwargs["api_base"] = settings.base_url

        if settings.api_key:
            kwargs["api_key"] = settings.api_key

        response = completion(**kwargs)
        return response.choices[0].message.content

    def answer(self, question: str) -> AgentResponse:
        provider = detect_provider(question)
        context = build_context(provider)

        messages = [
            {"role": "system", "content": _PROMPTS[provider]},
            {"role": "system", "content": context},
            {
                "role": "user",
                "content": (
                    f"Pergunta do usuário: {question}\n"
                    "Inclua links oficiais relevantes na resposta quando aplicável."
                ),
            },
        ]

        answer = self._call_llm(messages)
        return AgentResponse(provider=provider, answer=answer)

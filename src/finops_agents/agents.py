from __future__ import annotations

from dataclasses import dataclass

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from .config import load_settings
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
        settings = load_settings()
        self._llm = ChatOpenAI(
            model=settings.openai_model,
            temperature=settings.temperature,
            max_tokens=settings.max_tokens,
            base_url=settings.openai_base_url,
        )

    def answer(self, question: str) -> AgentResponse:
        provider = detect_provider(question)
        context = build_context(provider)

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", _PROMPTS[provider]),
                ("system", "{context}"),
                (
                    "human",
                    "Pergunta do usuário: {question}\n"
                    "Inclua links oficiais relevantes na resposta quando aplicável.",
                ),
            ]
        )

        chain = prompt | self._llm | StrOutputParser()
        answer = chain.invoke({"context": context, "question": question})
        return AgentResponse(provider=provider, answer=answer)

"""FinOps Agents - Sistema de agentes FinOps com suporte multi-LLM via LiteLLM.

Este pacote fornece um sistema de agentes especializados em FinOps para:
- Azure/Microsoft
- Huawei Cloud
- Comparativo Azure vs Huawei

Suporta múltiplos provedores LLM (locais e SaaS) através do LiteLLM:
- Ollama (local)
- LM Studio (local)
- OpenRouter (SaaS)
- Opencode Zen (SaaS)
- Google Gemini API (SaaS)
- Google Gemini OAuth (SaaS)
- OpenAI (SaaS)
"""

from .agents import AgentResponse, FinOpsAgentSystem
from .config import LLMProvider, Settings, load_settings
from .router import Provider, detect_provider

__all__ = [
    "AgentResponse",
    "FinOpsAgentSystem",
    "LLMProvider",
    "Settings",
    "load_settings",
    "Provider",
    "detect_provider",
]

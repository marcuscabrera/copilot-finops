# FinOps Agents — Python + LangChain + LiteLLM

Projeto migrado de **Copilot Studio** para uma arquitetura de **agentes em Python com LangChain e LiteLLM**.

## O que este projeto faz

O sistema responde perguntas FinOps com roteamento automático para agentes especializados em:

- **Azure / Microsoft**
- **Huawei Cloud**
- **Comparativo Azure vs Huawei**

As respostas seguem padrão consultivo (contexto, custos, riscos, ações, próximos passos) e usam como base:

- Fontes oficiais dos provedores
- Artefatos locais de governança/aceitação FinOps já existentes no repositório

## Arquitetura

```
src/finops_agents/
├── agents.py       # Orquestrador e agentes especializados (LiteLLM)
├── router.py       # Roteamento de perguntas por provedor
├── knowledge.py    # Contexto com fontes oficiais + docs locais
├── config.py       # Configuração multi-LLM via variáveis de ambiente
└── cli.py          # Interface de linha de comando

tests/
└── test_router.py  # Testes de roteamento
```

## Provedores LLM Suportados

### Locais
- **Ollama** - Modelos locais rodando via Ollama
- **LM Studio** - Modelos locais rodando via LM Studio

### SaaS
- **OpenAI** - Modelos da OpenAI (GPT-4, GPT-4o-mini, etc.)
- **OpenRouter** - Acesso a múltiplos modelos via OpenRouter
- **Opencode Zen** - Plataforma Opencode Zen
- **Google Gemini API** - Modelos Gemini via API Key
- **Google Gemini OAuth** - Modelos Gemini via autenticação OAuth

## Requisitos

- Python 3.11+
- Chave de API do provedor escolhido (ou servidor local rodando)

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Configuração

Edite o arquivo `.env` conforme o provedor desejado:

### OpenAI (padrão)
```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=sua-chave-aqui
OPENAI_MODEL=gpt-4o-mini
```

### Ollama (Local)
```bash
LLM_PROVIDER=ollama
OLLAMA_MODEL=llama3.1:8b
OLLAMA_BASE_URL=http://localhost:11434
```

### LM Studio (Local)
```bash
LLM_PROVIDER=lmstudio
LMSTUDIO_MODEL=local-model
LMSTUDIO_BASE_URL=http://localhost:1234/v1
```

### OpenRouter (SaaS)
```bash
LLM_PROVIDER=openrouter
OPENROUTER_MODEL=meta-llama/llama-3.1-8b-instruct
OPENROUTER_API_KEY=sua-chave-aqui
```

### Opencode Zen (SaaS)
```bash
LLM_PROVIDER=opencode_zen
OPENCODE_ZEN_MODEL=qwen-coder-plus
OPENCODE_ZEN_API_KEY=sua-chave-aqui
```

### Google Gemini API
```bash
LLM_PROVIDER=google_gemini_api
GEMINI_MODEL=gemini-1.5-flash
GOOGLE_API_KEY=sua-chave-aqui
```

### Google Gemini OAuth
```bash
LLM_PROVIDER=google_gemini_oauth
GEMINI_MODEL=gemini-1.5-flash
# Autenticação OAuth é gerenciada automaticamente
```

### Variáveis gerais
```bash
FINOPS_TEMPERATURE=0.2
FINOPS_MAX_TOKENS=1200
```

## Uso

Modo pergunta única:

```bash
PYTHONPATH=src python -m finops_agents.cli -q "Compare Azure e Huawei para workload 24x7"
```

Modo interativo:

```bash
PYTHONPATH=src python -m finops_agents.cli
```

## Testes

```bash
PYTHONPATH=src pytest
```

## Observações de migração

- Os arquivos em `FinOps Agent/` permanecem como referência histórica do projeto original em Copilot Studio.
- A execução principal agora é totalmente em Python + LangChain + LiteLLM.
- O suporte multi-LLM permite usar modelos locais (Ollama, LM Studio) ou SaaS (OpenAI, Gemini, OpenRouter, etc.).

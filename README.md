# FinOps Agents — Python + LangChain

Projeto migrado de **Copilot Studio** para uma arquitetura de **agentes em Python com LangChain**.

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
├── agents.py       # Orquestrador e agentes especializados
├── router.py       # Roteamento de perguntas por provedor
├── knowledge.py    # Contexto com fontes oficiais + docs locais
├── config.py       # Configuração por variáveis de ambiente
└── cli.py          # Interface de linha de comando

tests/
└── test_router.py  # Testes de roteamento
```

## Requisitos

- Python 3.11+
- Chave de API compatível com OpenAI (`OPENAI_API_KEY`)

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Configuração

Variáveis principais em `.env`:

- `OPENAI_API_KEY`
- `OPENAI_MODEL` (padrão: `gpt-4o-mini`)
- `OPENAI_BASE_URL` (opcional para endpoint compatível)
- `FINOPS_TEMPERATURE`
- `FINOPS_MAX_TOKENS`

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
- A execução principal agora é totalmente em Python + LangChain.

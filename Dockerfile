# Imagem base Python otimizada para produção
FROM python:3.11-slim-bookworm

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências do sistema necessárias
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia primeiro o requirements.txt para aproveitar cache do Docker
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copia o código da aplicação
COPY src/ ./src/
COPY huawei-cloud-finops-coverage-catalog.md .
COPY huawei-cloud-finops-governance.md .
COPY huawei-cloud-finops-acceptance-prompts.md .
COPY .env.example .env.example

# Cria volume para persistência de dados (logs, cache, etc.)
VOLUME ["/app/data"]

# Cria usuário não-root para segurança
RUN useradd --create-home --shell /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser

# Comando padrão para executar a aplicação em modo interativo
CMD ["python", "-m", "finops_agents.cli"]

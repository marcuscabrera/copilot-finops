# Guia Completo de Setup Docker - FinOps Agents

Este guia detalha como configurar e executar o projeto **FinOps Agents** em ambiente Docker com Docker Compose, incluindo banco de dados PostgreSQL para persistência de dados.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- **Docker** (versão 20.10 ou superior)
- **Docker Compose** (versão 2.0 ou superior)
- **Git** (para clonar o repositório)

### Verificando as instalações

```bash
# Verificar versão do Docker
docker --version

# Verificar versão do Docker Compose
docker compose version

# Verificar se o Docker está rodando
docker info
```

---

## 🚀 Passo a Passo de Setup

### 1. Clonar o Repositório (se aplicável)

```bash
git clone <url-do-repositorio>
cd finops-agents
```

### 2. Estrutura de Arquivos Docker

O projeto contém os seguintes arquivos relacionados ao Docker:

```
/workspace/
├── Dockerfile                    # Instruções para build da imagem da aplicação
├── docker-compose.yml            # Configuração dos serviços Docker
├── .env.template                 # Template de variáveis de ambiente
├── .env.example                  # Exemplo mínimo de variáveis de ambiente
└── docker/
    ├── db/
    │   └── init.sql              # Script de inicialização do banco de dados
    ├── backup.sh                 # Script de backup do banco de dados
    └── restore.sh                # Script de restore do banco de dados
```

### 3. Configurar Variáveis de Ambiente

#### 3.1. Criar arquivo `.env`

Copie o template e configure suas variáveis:

```bash
cp .env.template .env
```

#### 3.2. Editar o arquivo `.env`

Abra o arquivo `.env` e configure:

```bash
# CONFIGURAÇÕES DA API OPENAI (OBRIGATÓRIO)
OPENAI_API_KEY=sua_chave_api_aqui
OPENAI_MODEL=gpt-4o-mini
OPENAI_BASE_URL=

# CONFIGURAÇÕES DO FINOPS AGENTS
FINOPS_TEMPERATURE=0.2
FINOPS_MAX_TOKENS=1200

# CONFIGURAÇÕES DO BANCO DE DADOS (OPCIONAL)
POSTGRES_USER=finops_user
POSTGRES_PASSWORD=mude_esta_senha_para_algo_seguro
POSTGRES_DB=finops_db
```

> ⚠️ **IMPORTANTE**: 
> - A `OPENAI_API_KEY` é **obrigatória** para a aplicação funcionar
> - Altere a senha do PostgreSQL para algo seguro em produção
> - **NUNCA** commit o arquivo `.env` no Git (ele já está no `.gitignore`)

---

## 🔨 Construção das Imagens Docker

### Opção 1: Build Automático (Recomendado)

O Docker Compose pode construir as imagens automaticamente:

```bash
# Construir e iniciar todos os serviços
docker compose up --build
```

### Opção 2: Build Manual

Se preferir construir separadamente:

```bash
# Construir apenas a imagem da aplicação
docker build -t finops-agents-app:latest .

# Verificar a imagem criada
docker images | grep finops-agents
```

### Explicação do Dockerfile

O `Dockerfile` contém as seguintes instruções:

1. **Base Image**: Usa Python 3.11 slim para menor tamanho
2. **Variáveis de Ambiente**: Configura Python para execução otimizada
3. **Dependências do Sistema**: Instala curl para healthchecks
4. **Dependências Python**: Instala pacotes do requirements.txt com cache
5. **Código da Aplicação**: Copia o código fonte e documentos
6. **Volume**: Cria volume para dados persistentes
7. **Segurança**: Executa como usuário não-root

---

## ▶️ Iniciando o Ambiente

### Iniciar em Modo Foreground (com logs visíveis)

```bash
docker compose up
```

- Pressione `Ctrl+C` para parar
- Os logs são exibidos em tempo real

### Iniciar em Modo Background (Detached)

```bash
# Iniciar todos os serviços em segundo plano
docker compose up -d

# Ver status dos serviços
docker compose ps
```

### Iniciar Apenas a Aplicação (sem banco de dados)

```bash
# Se não precisar do banco de dados inicialmente
docker compose up -d finops-app
```

### Iniciar Apenas o Banco de Dados

```bash
docker compose up -d finops-db
```

---

## ✅ Verificando se os Serviços estão Funcionando

### 1. Verificar Status dos Containers

```bash
# Lista todos os containers com status
docker compose ps

# Ou usar docker ps diretamente
docker ps --filter "name=finops"
```

**Saída esperada:**
```
NAME                  STATUS                   PORTS
finops-agents-app     Up (healthy)             
finops-agents-db      Up (healthy)             0.0.0.0:5432->5432/tcp
```

### 2. Verificar Logs

```bash
# Logs de todos os serviços
docker compose logs

# Logs de um serviço específico
docker compose logs finops-app
docker compose logs finops-db

# Logs em tempo real (follow)
docker compose logs -f finops-app

# Últimas 50 linhas
docker compose logs --tail=50 finops-app
```

### 3. Testar Conexão com Banco de Dados

```bash
# Acessar o container do banco de dados
docker exec -it finops-agents-db psql -U finops_user -d finops_db

# No prompt do PostgreSQL, execute:
\dt          # Listar tabelas
SELECT version();  # Ver versão do PostgreSQL
\q           # Sair
```

### 4. Testar a Aplicação

```bash
# Acessar o container da aplicação
docker exec -it finops-agents-app python -m finops_agents.cli --question "Quais são os custos do Azure?"
```

---

## 🔧 Acessando a Aplicação

### Modo Interativo

```bash
# Executar a CLI dentro do container
docker exec -it finops-agents-app python -m finops_agents.cli
```

### Executar uma Pergunta Única

```bash
docker exec -it finops-agents-app \
    python -m finops_agents.cli --question "Compare os custos entre Azure e Huawei Cloud"
```

### Desenvolvimento Local com Hot Reload

Para desenvolvimento, você pode montar o código localmente:

1. Edite `docker-compose.yml` e descomente a linha:
```yaml
volumes:
  - finops_app_data:/app/data
  - ./src:/app/src:ro  # Descomente esta linha
```

2. Reinicie o serviço:
```bash
docker compose up -d finops-app
```

---

## 🔐 Configuração Segura de Variáveis de Ambiente

### Boas Práticas

1. **Nunca commit credenciais no Git**
   ```bash
   # O arquivo .env já está no .gitignore
   git status  # Verifique que .env não aparece
   ```

2. **Use valores diferentes por ambiente**
   ```bash
   # Desenvolvimento
   cp .env.template .env.dev
   
   # Produção
   cp .env.template .env.prod
   ```

3. **Em Produção, use Docker Secrets ou variáveis do sistema**

   **Opção A: Docker Secrets (Docker Swarm)**
   ```yaml
   services:
     finops-app:
       secrets:
         - openai_api_key
   
   secrets:
     openai_api_key:
       external: true
   ```

   **Opção B: Variáveis de Ambiente do Host**
   ```bash
   # No servidor de produção
   export OPENAI_API_KEY="sk-..."
   docker compose up -d
   ```

   **Opção C: .env separado em produção**
   ```bash
   # No servidor
   nano .env  # Configure manualmente
   chmod 600 .env  # Restringir permissões
   ```

4. **Valide as variáveis antes de iniciar**
   ```bash
   # Verificar se OPENAI_API_KEY está configurada
   grep "^OPENAI_API_KEY=" .env | grep -v "sua_chave_api_aqui"
   ```

---

## 🛑 Parar e Remover o Ambiente

### Parar os Serviços

```bash
# Parar todos os serviços (mantém volumes e dados)
docker compose stop

# Ou enviar sinal SIGTERM
docker compose down
```

### Parar e Remover Containers e Redes

```bash
# Remove containers e redes, mas mantém volumes (dados persistem)
docker compose down

# Verificar
docker ps -a | grep finops  # Não deve mostrar nada
```

### Remover TUDO (incluindo volumes/dados)

⚠️ **ATENÇÃO**: Isso apagará todos os dados do banco de dados!

```bash
# Remove containers, redes E volumes
docker compose down -v

# Ou especificar explicitamente
docker compose down --volumes
```

### Remover Imagens Também

```bash
# Down completo + remover imagens
docker compose down -v --rmi all

# Ou apenas imagens locais (não as pulladas)
docker compose down -v --rmi local
```

### Limpeza Completa do Sistema

```bash
# Parar tudo
docker compose down -v --rmi all

# Remover volumes órfãos
docker volume prune -f

# Remover networks órfãs
docker network prune -f

# Remover imagens não utilizadas
docker image prune -a -f
```

---

## 💾 Backup e Restore do Banco de Dados

### Realizar Backup

```bash
# Navegue até o diretório docker
cd docker

# Executar backup (nome automático com timestamp)
./backup.sh

# Ou especificar nome personalizado
./backup.sh backup_manual_2024

# O backup será salvo em: docker/backups/
```

**Exemplo de saída:**
```
==========================================
Backup do Banco de Dados FinOps Agents
==========================================
Container: finops-agents-db
Database: finops_db
Arquivo: backup_20240115_143022.sql.gz

✓ Backup realizado: 24K
```

### Listar Backups Disponíveis

```bash
ls -lh docker/backups/
```

### Restaurar Backup

```bash
# Navegue até o diretório docker
cd docker

# Executar restore
./restore.sh backups/backup_20240115_143022.sql.gz
```

**Processo de restore:**
1. O script verifica se o container está rodando
2. Solicita confirmação (dados atuais serão substituídos)
3. Executa o restore usando `psql`
4. Confirma conclusão

### Backup Automatizado (Cron)

Para backups automáticos diários:

```bash
# Editar crontab
crontab -e

# Adicionar linha para backup diário às 2 AM
0 2 * * * cd /workspace/docker && ./backup.sh >> /var/log/finops-backup.log 2>&1
```

### Backup Remoto

```bash
# Copiar backup para outro servidor
scp docker/backups/backup_*.sql.gz user@server:/backups/finops/

# Ou usar rsync para sincronização
rsync -avz docker/backups/ user@server:/backups/finops/
```

---

## 🐛 Troubleshooting

### Problema: Container não inicia

```bash
# Verificar logs de erro
docker compose logs finops-app

# Verificar se há erros de build
docker compose build --no-cache
```

### Problema: Erro de conexão com OpenAI

```bash
# Verificar se OPENAI_API_KEY está configurada
docker compose config | grep OPENAI_API_KEY

# Testar conectividade
docker exec finops-agents-app curl -I https://api.openai.com
```

### Problema: Banco de dados não aceita conexões

```bash
# Verificar healthcheck
docker compose ps finops-db

# Verificar logs do PostgreSQL
docker compose logs finops-db | tail -50

# Testar conexão manual
docker exec -it finops-agents-db pg_isready -U finops_user
```

### Problema: Permissão negada em volumes

```bash
# Resetar permissões dos volumes
docker compose down -v
docker compose up -d
```

### Problema: Porta 5432 já em uso

```bash
# Verificar o que está usando a porta
lsof -i :5432

# Ou mudar a porta no docker-compose.yml
ports:
  - "5433:5432"  # Usa porta 5433 externa
```

### Rebuild Forçado

```bash
# Reconstruir sem cache
docker compose build --no-cache

# Reconstruir um serviço específico
docker compose build --no-cache finops-app
```

---

## 📊 Monitoramento

### Ver Uso de Recursos

```bash
# Uso de CPU e memória em tempo real
docker stats finops-agents-app finops-agents-db

# Uma única captura
docker stats --no-stream
```

### Ver Tamanho das Imagens

```bash
docker images | grep finops
```

### Ver Tamanho dos Volumes

```bash
docker system df -v | grep finops
```

---

## 📝 Comandos Úteis

```bash
# Acessar shell do container da aplicação
docker exec -it finops-agents-app bash

# Acessar shell do container do banco de dados
docker exec -it finops-agents-db sh

# Reiniciar um serviço
docker compose restart finops-app

# Recrear um serviço
docker compose up -d --force-recreate finops-app

# Ver configuração completa
docker compose config

# Validar docker-compose.yml
docker compose config --quiet
```

---

## 🔒 Considerações de Segurança

1. **Senhas Fortes**: Use senhas complexas para o PostgreSQL
2. **Network Isolada**: Os serviços usam rede interna isolada
3. **Usuário Não-Root**: A aplicação roda como usuário `appuser`
4. **Volumes Named**: Volumes nomeados previnem conflitos
5. **Healthchecks**: Verificam integridade dos serviços
6. **.gitignore**: Credenciais não são commitadas

---

## 📚 Referências

- [Documentação Docker](https://docs.docker.com/)
- [Documentação Docker Compose](https://docs.docker.com/compose/)
- [PostgreSQL Docker Hub](https://hub.docker.com/_/postgres)
- [Python Docker Best Practices](https://pythonspeed.com/articles/base-images-python-dockerimages/)

---

## 🆘 Suporte

Em caso de problemas:

1. Verifique os logs: `docker compose logs -f`
2. Consulte a seção de Troubleshooting
3. Abra uma issue no repositório
4. Verifique a documentação oficial do Docker

---

**Versão do Guia**: 1.0  
**Última Atualização**: 2024

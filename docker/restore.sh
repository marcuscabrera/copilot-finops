#!/bin/bash
# Script de restore do banco de dados PostgreSQL
set -e

DB_CONTAINER="finops-agents-db"
DB_USER="${POSTGRES_USER:-finops_user}"
DB_NAME="${POSTGRES_DB:-finops_db}"
BACKUP_FILE="${1}"

echo "=========================================="
echo "Restore do Banco de Dados FinOps Agents"
echo "=========================================="

if [ -z "${BACKUP_FILE}" ]; then
    echo "ERRO: Especifique o arquivo de backup"
    echo "Uso: $0 <arquivo_backup.sql.gz>"
    exit 1
fi

if [ ! -f "${BACKUP_FILE}" ]; then
    echo "ERRO: Arquivo não encontrado: ${BACKUP_FILE}"
    exit 1
fi

if ! docker ps --format '{{.Names}}' | grep -q "^${DB_CONTAINER}$"; then
    echo "ERRO: Container não está em execução."
    exit 1
fi

echo "Arquivo: ${BACKUP_FILE}"
echo ""
echo "ATENÇÃO: Todos os dados atuais serão substituídos!"
read -p "Continuar? (s/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Ss]$ ]]; then
    echo "Operação cancelada."
    exit 0
fi

echo "Iniciando restore..."
gunzip -c "${BACKUP_FILE}" | docker exec -i "${DB_CONTAINER}" \
    psql -U "${DB_USER}" -d "${DB_NAME}"

echo "✓ Restore realizado com sucesso!"

#!/bin/bash
# Script de backup do banco de dados PostgreSQL
set -e

DB_CONTAINER="finops-agents-db"
DB_USER="${POSTGRES_USER:-finops_user}"
DB_NAME="${POSTGRES_DB:-finops_db}"
BACKUP_DIR="./backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_NAME="${1:-backup_${TIMESTAMP}}"

mkdir -p "${BACKUP_DIR}"

echo "=========================================="
echo "Backup do Banco de Dados FinOps Agents"
echo "=========================================="
echo "Container: ${DB_CONTAINER}"
echo "Database: ${DB_NAME}"
echo "Arquivo: ${BACKUP_NAME}.sql.gz"
echo ""

if ! docker ps --format '{{.Names}}' | grep -q "^${DB_CONTAINER}$"; then
    echo "ERRO: Container não está em execução."
    exit 1
fi

docker exec -t "${DB_CONTAINER}" \
    pg_dump -U "${DB_USER}" -d "${DB_NAME}" --format=plain --no-owner --no-privileges | \
    gzip > "${BACKUP_DIR}/${BACKUP_NAME}.sql.gz"

if [ -f "${BACKUP_DIR}/${BACKUP_NAME}.sql.gz" ]; then
    BACKUP_SIZE=$(du -h "${BACKUP_DIR}/${BACKUP_NAME}.sql.gz" | cut -f1)
    echo "✓ Backup realizado: ${BACKUP_SIZE}"
else
    echo "✗ ERRO: Falha no backup"
    exit 1
fi

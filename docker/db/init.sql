-- Script de inicialização do banco de dados PostgreSQL
-- Este script é executado automaticamente quando o container do PostgreSQL é iniciado pela primeira vez

-- Criação de tabelas para futuras extensões do projeto FinOps Agents
-- Exemplo: histórico de consultas, cache de respostas, métricas de uso, etc.

-- Tabela para armazenar histórico de consultas (opcional - para futuras funcionalidades)
CREATE TABLE IF NOT EXISTS query_history (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    provider VARCHAR(50) NOT NULL,
    answer TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB DEFAULT '{}'::jsonb
);

-- Tabela para armazenar cache de respostas (opcional - para otimização)
CREATE TABLE IF NOT EXISTS answer_cache (
    id SERIAL PRIMARY KEY,
    question_hash VARCHAR(64) UNIQUE NOT NULL,
    provider VARCHAR(50) NOT NULL,
    answer TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP WITH TIME ZONE,
    hit_count INTEGER DEFAULT 0
);

-- Tabela para métricas de uso (opcional - para analytics)
CREATE TABLE IF NOT EXISTS usage_metrics (
    id SERIAL PRIMARY KEY,
    event_type VARCHAR(50) NOT NULL,
    provider VARCHAR(50),
    tokens_used INTEGER DEFAULT 0,
    response_time_ms INTEGER,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB DEFAULT '{}'::jsonb
);

-- Índices para otimização de consultas
CREATE INDEX IF NOT EXISTS idx_query_history_created_at ON query_history(created_at);
CREATE INDEX IF NOT EXISTS idx_query_history_provider ON query_history(provider);
CREATE INDEX IF NOT EXISTS idx_answer_cache_expires_at ON answer_cache(expires_at);
CREATE INDEX IF NOT EXISTS idx_usage_metrics_created_at ON usage_metrics(created_at);
CREATE INDEX IF NOT EXISTS idx_usage_metrics_event_type ON usage_metrics(event_type);

-- Comentário nas tabelas
COMMENT ON TABLE query_history IS 'Histórico de consultas feitas ao FinOps Agents';
COMMENT ON TABLE answer_cache IS 'Cache de respostas para otimização de performance';
COMMENT ON TABLE usage_metrics IS 'Métricas de uso do sistema para analytics e monitoring';

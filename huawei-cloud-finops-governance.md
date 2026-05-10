# Governança Contínua — Cobertura Huawei Cloud no FinOps Agent

## Processo de atualização periódica

1. **Cadência mensal**
   - Revisar alterações de pricing e catálogo de serviços Huawei Cloud.
   - Verificar se links de conhecimento continuam válidos e indexáveis.
2. **Cadência trimestral**
   - Repriorizar matriz de cobertura (P1/P2/P3) com base em impacto financeiro real.
   - Atualizar equivalências Azure vs Huawei para novos serviços.
3. **Cadência sob demanda**
   - Atualizar imediatamente quando houver mudança crítica de preço, política comercial ou descontinuação de serviço.

## Indicadores de qualidade (KPIs)

- Cobertura funcional Huawei (% de funções-alvo atendidas)
- Taxa de resposta útil
- Taxa de aderência a fonte oficial
- Tempo médio para atualizar base após mudança de pricing
- Quantidade de lacunas abertas e fechadas por ciclo

## Roadmap de expansão

### Fase 1 (imediata)
- Consolidar cobertura de IAM, VPC, ECS, OBS, RDS, CCE, CDN, WAF, Billing, Monitoramento e Governança.
- Garantir respostas estruturadas no padrão FinOps.

### Fase 2 (curto prazo)
- Aprimorar comparativos Azure vs Huawei por tipo de workload.
- Incluir playbooks específicos para forecast, orçamento e anomalias.

### Fase 3 (médio prazo)
- Expandir para serviços especializados (data lake, analytics avançado, segurança avançada).
- Evoluir benchmarks por unidade econômica (custo por transação, custo por usuário, custo por ambiente).

## Checklist de revisão para nova função Huawei

- [ ] Fonte oficial Huawei adicionada em `FinOps Agent/knowledge/`
- [ ] Função mapeada na matriz FinOps x Serviços
- [ ] Equivalência Azure documentada (quando aplicável)
- [ ] Prompt de aceitação criado e validado
- [ ] Instruções do agente atualizadas (se necessário)
- [ ] Roteamento/fallback ajustado para novo escopo
- [ ] Evidência de validação registrada


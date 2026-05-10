# Suíte de Prompts de Aceitação — Huawei Cloud FinOps

## Critérios de qualidade

- **Taxa de resposta útil**: % de respostas acionáveis sem necessidade de nova pergunta.
- **Aderência à fonte oficial**: % de respostas com referência explícita a documentação oficial Huawei/Microsoft quando aplicável.
- **Precisão de recomendação**: qualidade técnica das recomendações FinOps por cenário.
- **Lacunas de cobertura**: temas em que o agente não responde com confiança e precisa de novas fontes.

## Prompts por domínio

### Compute
1. "Como fazer rightsizing de ECS para reduzir custo mensal sem afetar SLA?"
2. "Quando vale usar compromisso/reserva em ECS versus pagamento sob demanda?"
3. "Compare custo operacional de ECS com Azure VM para workload 24x7."

### Storage
4. "Quais políticas de lifecycle no OBS reduzem custo para dados frios?"
5. "Como estimar custo total do OBS considerando requests e egress?"
6. "Compare OBS e Azure Blob para retenção de logs por 12 meses."

### Network
7. "Quais são os principais drivers de custo em VPC e tráfego de saída?"
8. "Como reduzir custo de CDN mantendo performance global?"
9. "Compare custos de rede entre Huawei VPC e Azure VNet para arquitetura hub-and-spoke."

### Security
10. "Como otimizar custo de WAF sem reduzir proteção?"
11. "Que boas práticas de IAM evitam custos indiretos e retrabalho operacional?"
12. "Compare estratégia de proteção WAF Huawei vs Azure WAF."

### Data/AI
13. "Como planejar orçamento mensal para workloads de IA no Huawei Cloud?"
14. "Quais componentes de custo devo monitorar em pipelines de dados e IA?"
15. "Compare custo de inferência entre serviços de IA Huawei e Azure AI."

### Management/Billing
16. "Como implantar showback/chargeback no Huawei Cloud por centro de custo?"
17. "Como configurar orçamento, alertas e forecast para contas Huawei?"
18. "Compare modelo de governança de custos Huawei Billing vs Azure Cost Management."

### Anomalias e governança
19. "Monte um playbook para resposta a anomalia de custo em Huawei Cloud."
20. "Quais KPIs mínimos FinOps devo acompanhar semanalmente em ambiente Huawei?"

## Template de avaliação por prompt

Para cada prompt, avaliar:
1. Respondeu ao contexto solicitado?
2. Listou componentes de custo relevantes?
3. Indicou riscos/caveats?
4. Trouxe ações recomendadas e próximos passos?
5. Incluiu nota de variação regional/contratual?
6. Citou fonte oficial (ou sinalizou ausência)?


# Catálogo Oficial de Cobertura Huawei Cloud (FinOps Agent)

## 1) Escopo de cobertura e priorização FinOps

### Prioridade P1 (alto impacto financeiro imediato)
- Billing e Cost Governance
- ECS (Elastic Cloud Server)
- OBS (Object Storage Service)
- RDS (Relational Database Service)
- VPC (Virtual Private Cloud)

### Prioridade P2 (otimização e escala)
- CCE (Cloud Container Engine)
- CDN
- WAF
- IAM (governança e acesso com impacto indireto de custo)
- Monitoramento/observabilidade

### Prioridade P3 (maturidade FinOps avançada)
- Forecast avançado e anomalias
- Chargeback/showback por unidade de negócio
- Benchmarking Azure vs Huawei por workload

## 2) Matriz FinOps x Serviços Huawei

| Serviço Huawei | Modelo de cobrança | Drivers de custo principais | Métricas FinOps | Limites/atenções | Oportunidades de otimização | Equivalência Azure (quando existir) |
|---|---|---|---|---|---|---|
| IAM | Sem custo direto relevante em muitos cenários; impacto indireto | Número de identidades, políticas, uso de credenciais com serviços pagos | Cobertura de MFA, políticas por função, contas órfãs | Configurações inadequadas aumentam risco operacional e custos indiretos | Princípio de menor privilégio, revisão periódica de acessos | Microsoft Entra ID (com nuances de licenciamento) |
| VPC | Recursos de rede e tráfego | Egress, gateways, IPs públicos, NAT, tráfego inter-zona | Custo por GB, custo por workload, taxa de egress | Custos de tráfego podem escalar rapidamente | Reduzir egress, otimizar arquitetura de rede, revisar NAT/IP público | Azure Virtual Network + NAT Gateway |
| ECS | Compute sob demanda/reservado (conforme oferta) | vCPU, memória, disco, tempo ligado, sistema operacional | Utilização CPU/RAM, custo por hora, custo por ambiente | Superdimensionamento e baixa utilização | Rightsizing, desligamento programado, uso de compromisso/reserva quando aplicável | Azure Virtual Machines |
| OBS | Armazenamento por volume + requisições + transferência | GB armazenado, classe de storage, requests, egress | Custo por GB-mês, taxa de acesso por classe, egress por bucket | Mudança de classe e retenção inadequada elevam custo | Lifecycle policies, otimização de classes, compressão e retenção | Azure Blob Storage |
| RDS | Instância + storage + backup + I/O (depende da oferta) | Tamanho da instância, storage provisionado, backups, tráfego | Custo por banco, consumo de storage, uso de backup | Ambientes de teste sem governança e retenção excessiva | Rightsizing de instância, política de backup, desligamento de não produção | Azure SQL Database / Azure Database for MySQL/PostgreSQL |
| CCE | Plano de controle + nós + storage + rede | Número/tipo de nós, autoscaling, tráfego, volumes | Custo por cluster, custo por namespace/time, utilização por nó | Cluster ocioso e overprovisioning | Autoscaling eficiente, densidade de pods, limpeza de recursos não usados | Azure Kubernetes Service (AKS) |
| CDN | Tráfego e requests (modelo conforme SKU/região) | Volume entregue, região, cache hit ratio | Custo por TB, hit ratio, custo por endpoint | Baixo cache hit aumenta custo de origem + CDN | Ajuste de cache, compressão, tuning de regras | Azure CDN / Front Door (cenário equivalente) |
| WAF | Política/instância + tráfego protegido | Volume de requisições, regras ativas, nível de proteção | Custo por app protegido, eventos bloqueados, custo por requisição | Regras excessivas podem impactar performance e custo | Ajustar políticas por risco, limpeza de regras obsoletas | Azure Web Application Firewall |
| Billing/Cost Mgmt | Faturamento e gestão financeira da nuvem | Estrutura de contas, centro de custo, tags, períodos de faturamento | Acurácia de alocação, cobertura de tags, variação mensal | Falta de governança dificulta previsibilidade | Estruturar chargeback/showback, políticas de tagging, orçamento e alertas | Azure Cost Management + Billing |
| Monitoramento | Cobrança por métricas, logs, retenção e consultas | Ingestão de logs, retenção, dashboards, alertas | Custo por GB de logs, retenção média, ruído de alertas | Retenção longa sem política e coleta excessiva | Redução de cardinalidade, retenção por criticidade, filtros de coleta | Azure Monitor / Log Analytics |

## 3) Checklist de cobertura por função Huawei

- [x] IAM
- [x] VPC
- [x] ECS
- [x] OBS
- [x] RDS
- [x] CCE
- [x] CDN
- [x] WAF
- [x] Billing
- [x] Monitoramento
- [x] Governança


from finops_agents.router import Provider, detect_provider


def test_detect_huawei() -> None:
    assert detect_provider("Como otimizar custo no Huawei Cloud ECS?") == Provider.HUAWEI


def test_detect_azure() -> None:
    assert detect_provider("Como reduzir custos no Azure Cost Management?") == Provider.AZURE


def test_detect_comparison() -> None:
    assert detect_provider("Compare Azure e Huawei para workload de IA") == Provider.COMPARISON

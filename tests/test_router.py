from finops_agents.router import Provider, detect_provider


def test_detect_huawei() -> None:
    assert detect_provider("Como otimizar custo no Huawei Cloud ECS?") == Provider.HUAWEI


def test_detect_azure() -> None:
    assert detect_provider("Como reduzir custos no Azure Cost Management?") == Provider.AZURE


def test_detect_comparison() -> None:
    assert detect_provider("Compare Azure e Huawei para workload de IA") == Provider.COMPARISON


def test_default_to_azure_when_no_provider_found() -> None:
    assert detect_provider("Como reduzir desperdício de custos na nuvem?") == Provider.AZURE


def test_detect_comparison_keyword_without_provider_names() -> None:
    assert detect_provider("Preciso de uma análise multi-cloud de custos") == Provider.COMPARISON

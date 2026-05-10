from finops_agents.router import Provider, detect_provider


def test_detect_huawei() -> None:
    assert detect_provider("Como otimizar custo no Huawei Cloud ECS?") == Provider.HUAWEI


def test_detect_azure() -> None:
    assert detect_provider("Como reduzir custos no Azure Cost Management?") == Provider.AZURE


def test_detect_huawei_case_insensitive() -> None:
    assert detect_provider("Como reduzir custos no HuAwEi Cloud?") == Provider.HUAWEI


def test_detect_comparison() -> None:
    assert detect_provider("Compare Azure e Huawei para workload de IA") == Provider.COMPARISON


def test_default_to_azure_when_no_provider_found() -> None:
    assert detect_provider("Como reduzir desperdício de custos na nuvem?") == Provider.AZURE


def test_detect_comparison_keyword_without_provider_names() -> None:
    assert detect_provider("Preciso de uma análise multi-cloud de custos") == Provider.COMPARISON


def test_default_to_azure_for_empty_input() -> None:
    assert detect_provider("") == Provider.AZURE


def test_default_to_azure_for_whitespace_input() -> None:
    assert detect_provider("   ") == Provider.AZURE


def test_detect_azure_from_url_context() -> None:
    assert detect_provider("Veja https://learn.microsoft.com/azure/cost-management-billing/") == Provider.AZURE


def test_detect_huawei_from_url_context() -> None:
    assert detect_provider("Confira https://www.huaweicloud.com/intl/en-us/pricing.html") == Provider.HUAWEI

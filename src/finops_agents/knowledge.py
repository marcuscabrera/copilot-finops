from __future__ import annotations

from pathlib import Path

from .router import Provider

_REPO_ROOT = Path(__file__).resolve().parents[2]
_LOCAL_DOCS = [
    _REPO_ROOT / "huawei-cloud-finops-coverage-catalog.md",
    _REPO_ROOT / "huawei-cloud-finops-governance.md",
    _REPO_ROOT / "huawei-cloud-finops-acceptance-prompts.md",
]

_OFFICIAL_SOURCES = {
    Provider.AZURE: [
        "https://learn.microsoft.com/azure/cost-management-billing/finops/",
        "https://learn.microsoft.com/azure/cost-management-billing/",
        "https://learn.microsoft.com/microsoft-365/",
        "https://learn.microsoft.com/azure/ai-foundry/",
        "https://learn.microsoft.com/fabric/",
    ],
    Provider.HUAWEI: [
        "https://www.huaweicloud.com/intl/en-us/product/ecs.html",
        "https://www.huaweicloud.com/intl/en-us/product/obs.html",
        "https://www.huaweicloud.com/intl/en-us/product/vpc.html",
        "https://www.huaweicloud.com/intl/en-us/product/waf.html",
        "https://www.huaweicloud.com/intl/en-us/pricing.html",
    ],
    Provider.COMPARISON: [
        "https://learn.microsoft.com/azure/cost-management-billing/",
        "https://www.huaweicloud.com/intl/en-us/pricing.html",
    ],
}


def load_local_knowledge() -> str:
    chunks: list[str] = []
    missing_files: list[str] = []
    for path in _LOCAL_DOCS:
        if not path.exists():
            missing_files.append(path.name)
            continue
        try:
            chunks.append(f"# Fonte local: {path.name}\n" + path.read_text(encoding="utf-8"))
        except OSError as exc:
            raise RuntimeError(
                f"Falha ao carregar a fonte de conhecimento local: {path} ({exc}). "
                "Verifique permissões, integridade e codificação do arquivo."
            ) from exc
    if missing_files:
        chunks.append(
            "# Aviso\n"
            "As seguintes fontes locais não foram encontradas e não entrarão no contexto: "
            + ", ".join(missing_files)
        )
    return "\n\n".join(chunks)


def build_context(provider: Provider) -> str:
    if provider not in _OFFICIAL_SOURCES:
        raise ValueError(f"Provider não suportado para contexto: {provider}")
    source_list = "\n".join(f"- {url}" for url in _OFFICIAL_SOURCES[provider])
    local_knowledge = load_local_knowledge()
    return (
        "Use apenas informações fundamentadas nas fontes oficiais abaixo e sinalize limites quando faltar evidência.\n"
        f"\nFontes oficiais preferenciais:\n{source_list}\n\n"
        f"Conhecimento local do projeto (apoio):\n{local_knowledge}\n"
    )

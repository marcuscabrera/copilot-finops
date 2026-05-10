from __future__ import annotations

from enum import Enum
import re


class Provider(str, Enum):
    AZURE = "azure"
    HUAWEI = "huawei"
    COMPARISON = "comparison"


_AZURE_PATTERN = re.compile(
    r"\b(azure|microsoft\s*365|m365|fabric|foundry|copilot\s+for\s+microsoft\s*365|m365\s+copilot)\b",
    re.IGNORECASE,
)
_HUAWEI_PATTERN = re.compile(r"\b(huawei|huaweicloud)\b", re.IGNORECASE)
_COMPARISON_PATTERN = re.compile(
    r"\b(vs|versus|compare|comparar|comparison|comparativo|cross[-\s]?cloud|multi[-\s]?cloud)\b",
    re.IGNORECASE,
)


def detect_provider(query: str) -> Provider:
    has_azure = bool(_AZURE_PATTERN.search(query))
    has_huawei = bool(_HUAWEI_PATTERN.search(query))

    if (has_azure and has_huawei) or _COMPARISON_PATTERN.search(query):
        return Provider.COMPARISON
    if has_huawei:
        return Provider.HUAWEI
    return Provider.AZURE

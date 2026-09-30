"""
공통 스키마 — 어느 업무(SOP, OPL, 주간보고 ...)든 똑같이 쓰는 응답 모양과 시각 표기.
업무별 요청/응답 모양은 각 업무 폴더의 schemas.py 에 둡니다 (예: app/sop/schemas.py).

시각(datetime) 은 전부 UTC 로, 끝에 Z 를 붙여 내보냅니다 (예: 2026-09-11T02:30:00.123456Z).
  DB 세션의 timezone 설정이 무엇이든(회사 DB 가 KST 여도) 응답은 항상 같은 모양이 되게 하려는 것입니다.
"""

from datetime import datetime, timezone
from typing import Annotated

from pydantic import BaseModel, PlainSerializer


def to_utc_z(value: datetime) -> str:
    """datetime 을 "UTC 기준 ISO 8601, 끝에 Z" 문자열로 바꿉니다. 시간대 정보가 없으면 UTC 로 간주합니다."""
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


# datetime 대신 이 타입을 쓰면 JSON 으로 내보낼 때 to_utc_z 가 자동 적용됩니다.
UtcDatetime = Annotated[datetime, PlainSerializer(to_utc_z, return_type=str, when_used="json")]


class HealthResponse(BaseModel):
    ok: bool
    db: str   # "up" 또는 "down"

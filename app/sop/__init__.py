"""
sop — SOP Studio 업무. API(sops / versions / locks), 저장 JSON 검사·순서도 추출(derive), SOP 간 참조(refs),
요청/응답 모양(schemas), 라우터 공용 도우미(common). DB 표는 sql/sop/ (sop_ 로 시작).

main.py 는 여기의 router 하나만 붙입니다:  app.include_router(sop_router, prefix="/api", ...)
"""

from fastapi import APIRouter

from app.sop import locks, sops, versions

router = APIRouter()
router.include_router(sops.router)
router.include_router(versions.router)
router.include_router(locks.router)

# 프로젝트 폴더의 .env 를 환경변수로 올립니다 (내 PC · 컨테이너 모두 — Dockerfile 이 .env 를 이미지에 복사).
# app 안의 어떤 파일을 import 하든 가장 먼저 실행됩니다.
#   - .env 가 없으면 아무 일도 안 합니다 (config.py 기본값 사용).
#   - 이미 있는 환경변수(deployment.yaml 의 env 등)는 덮어쓰지 않습니다.
import os

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"))

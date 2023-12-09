@echo off

REM 현재 디렉토리로 이동
cd /d "%~dp0"

REM 패키지 설치
pip install -r requirements.txt

REM Python 인터프리터를 사용하여 preprocessing.py 파일 실행
python preprocessing.py

REM 일시 정지
pause
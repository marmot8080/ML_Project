@echo off

REM 현재 디렉토리로 이동
cd /d "%~dp0"

REM Python 인터프리터를 사용하여 MachineLearning.py 파일 실행
python MachineLearning.py

REM 일시 정지
pause
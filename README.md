# ML_Project

### 프로젝트 설명
* Actor의 popularity 평균, Director의 popularity 평균, budget 세가지를 요소로 다중 선형회귀분석을 활용하여 rate 예측 모델 훈련 후 MSE(평균제곱오차) 측정

### 데이터셋 출처
* 아래 링크에서 movies_metadata.csv를 다운로드 받고 TMDB API를 활용하여 데이터 수집
* (https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset/data)

### 데이터셋 구축
* movies_metadata.csv를 assets/ 에 복사, assets/TMDB_API_Tokken.txt 파일을 생성한 뒤 자신의 TMDB api 토큰을 복사해 저장 후 build.bat 파일 실행 시 데이터셋 구축 가능
* 구축되어있는 데이터셋 다운로드 (https://drive.google.com/file/d/12ow3GeRPiY1Sw61NYCOfrLVeVUxKQw12/view?usp=sharing)

### 프로그램 실행
* 사전 데이터 분석에 활용한 그래프를 확인하기 위해서는 graph.bat 실행
* 모델을 훈련한 뒤 측정한 MSE(평균제곱오차) 값을 확인하기 위해서는 train.bat 실행

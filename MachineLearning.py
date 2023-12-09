import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

csv_path = "./assets/"
csv_name = "movie_data.csv"

# csv파일을 데이터프레임으로 변환
movie_data = pd.read_csv(csv_path + csv_name, header=None)

# 열 이름 행 제거
movie_data = movie_data.loc[1:, :]

# 열 이름 설정
movie_data.columns = ['movie_id', 'genre', 'actors_popularity', 'directors_popularity', 'budget', 'rate']

# genre가 Drama인 데이터만 추출
train_data = movie_data.groupby('genre').get_group('Drama')

# budget를 int형으로 설정
train_data['budget'] = train_data.loc[:, 'budget'].astype(int)

# actors_popularity, directors_popularity, rate를 float형으로 설정
train_data[['actors_popularity', 'directors_popularity', 'budget', 'rate']] = movie_data.loc[:, ['actors_popularity', 'directors_popularity', 'budget', 'rate']].astype(float)

# actors_popularity, directors_popularity, budget을 통해 rate를 예측하는 다중 선형회귀분석
x_data = train_data.loc[:, ['actors_popularity', 'directors_popularity', 'budget']]
target = train_data.loc[:, ['rate']]

# 상수항 추가
x_train_data = sm.add_constant(x_data, has_constant = "add")

# 다중 선형 회귀 모델
model = sm.OLS(target, x_train_data).fit()

# 모델의 잔차 시각화
# model.resid.plot(label = "model")
# plt.show()
# plt.close()

# 상수항 추가
x_test_data = sm.add_constant(x_data, has_constant='add')

# 여러 데이터에 대한 예측값 계산
predicted_rates = model.predict(x_test_data)

# 예측값과 실제값의 차이 제곱하여 누적
real_rate = target.loc[:, 'rate']
error_sum = np.sum((real_rate - predicted_rates) ** 2)

# 평균제곱오차(Mean Squared Error, MSE) 계산
mse = error_sum / len(real_rate)

# 평균제곱오차 출력
print("평균제곱오차(MSE):", mse)
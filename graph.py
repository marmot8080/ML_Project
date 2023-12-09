import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_path = "./assets/"
csv_name = "movie_data.csv"

# csv파일을 데이터프레임으로 변환
df = pd.read_csv(csv_path + csv_name, header=None)

# 열 이름 행 제거
df = df.loc[1:]

# 열 이름 설정
df.columns = ['movie_id', 'genre', 'actors_average', 'directors_average', 'budget', 'rate']

# budget를 int형으로 설정
df['budget'] = df['budget'].astype(int)

# actors_average, directors_average, rate를 float형으로 설정
df[['actors_average', 'directors_average', 'budget', 'rate']] = df[['actors_average', 'directors_average', 'budget', 'rate']].astype(float)


# 장르별 budget 평균 (막대 그래프)
def budget_average_by_genre():
    # genre, budget 데이터 추출
    df_budget = df.loc[:, ['genre', 'budget']]

    # 장르별 budget 평균
    plot_budget = df_budget.groupby('genre').mean()

    # 그래프 설정
    plt.style.use('ggplot')

    plot_budget.plot(kind='bar', width=0.5, figsize=(10, 8))

    plt.title('budget average by genre')
    plt.ylabel('budget average')
    plt.xlabel('genre')

    plt.show()
    plt.close()

# 장르별 영화 개수 (막대 그래프)
def movie_count_by_genre():
    # 장르별 영화 개수
    plot_count = df.groupby('genre').size()

    # 그래프 설정
    plt.style.use('ggplot')

    plot_count.plot(kind='bar', width=0.5, figsize=(10, 8))

    plt.title('movies count by genre')
    plt.ylabel('movies count')
    plt.xlabel('genre')

    plt.show()
    plt.close()

# 각 요소 간 상관관계 그래프
def every_pair_plot():
    # Drama 대상으로 분석
    df_Drama = df.groupby('genre').get_group('Drama')

    sns.pairplot(df_Drama)
    plt.show()
    plt.close()

if __name__ == "__main__":
    budget_average_by_genre()
    movie_count_by_genre()
    every_pair_plot()
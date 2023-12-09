import pandas as pd
import requests
import json

csv_path = './assets/'
movie_data_csv_name = 'movie_data.csv'
metadata_csv_name = 'movies_metadata.csv'

def movie_data_manufacture():
    # movie_metadata.csv 읽어오기
    metadata = pd.read_csv(csv_path + metadata_csv_name)

    data = pd.DataFrame(columns=['movie_id', 'genres', 'budget', 'rate'])
    data['movie_id'] = metadata.iloc[:, 5]
    data['genres'] = metadata.iloc[:, 3]
    data['budget'] = metadata.iloc[:, 2]
    data['rate'] = metadata.iloc[:, 22]

    # 각 열 별 유효하지 않은 값을 가지는 행 삭제
    idx = data[data['budget'] == '0'].index
    data.drop(idx , inplace=True)

    idx = data[data['rate'] == 0.0].index
    data.drop(idx , inplace=True)

    idx = data[data['genres'] == '[]'].index
    data.drop(idx , inplace=True)

    non_numeric_indices = data[pd.to_numeric(data['movie_id'], errors='coerce').isnull()].index
    data = data.drop(non_numeric_indices)

    non_numeric_indices = data[pd.to_numeric(data['budget'], errors='coerce').isnull()].index
    data = data.drop(non_numeric_indices)

    non_numeric_indices = data[pd.to_numeric(data['rate'], errors='coerce').isnull()].index
    data = data.drop(non_numeric_indices)

    data.to_csv(csv_path + movie_data_csv_name, index=False)


def TMDB_API_call():
    # TMDB API 토큰 파일에 저장된 토큰 읽어오기
    with open('./assets/TMDB_API_Tokken.txt', 'r') as tokken_file:
        API_Tokken = tokken_file.read()

    # movie_metadata.csv 읽어오기
    movies_data = pd.read_csv(csv_path + movie_data_csv_name)

    # ID를 int형으로 설정
    movies_data['movie_id'] = movies_data['movie_id'].astype(int)

    # movie_data 데이터 프레임 생성
    movie_data = pd.DataFrame(columns=['movie_id', 'genre', 'actors_popularity', 'directors_popularity', 'budget', 'rate'])

    for i in range(0, len(movies_data)):
        movie_id = movies_data.loc[i, 'movie_id']

        if(i % 100 == 0):
            print(i, '/', len(movies_data))

        url = "https://api.themoviedb.org/3/movie/{}/credits?language=en".format(movie_id)

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer {}".format(API_Tokken)
        }

        response = requests.get(url, headers=headers)
        data = response.json()
        
        # error 반환 시의 처리
        if 'status_code' in data:
            continue
        
        data = data['cast']

        actors_popularity = 0
        actors_count = 0
        directors_popularity = 0
        directors_count = 0
        for i in range(1, len(data)):
            if data[i]['known_for_department'] == 'Acting':
                # actor popularity 합산
                actors_popularity += data[i]['popularity']
                actors_count += 1
            elif data[i]['known_for_department'] == 'Directing':
                # director popularity 합산
                directors_popularity += data[i]['popularity']
                directors_count += 1
        
        # actor나 director가 없을 경우 학습 데이터에서 제외
        if(actors_count == 0 or directors_count == 0):
            continue

        genres_text = movies_data.loc[i, 'genres']
        genres_text = genres_text.replace("'", '"')
        genres = json.loads(genres_text)
        for genre in genres:
            row = {
                'movie_id': movie_id,
                'genre': genre['name'],
                'actors_popularity': actors_popularity / actors_count,
                'directors_popularity': directors_popularity / directors_count,
                'budget': movies_data.loc[i, 'budget'],
                'rate': movies_data.loc[i, 'rate']
            }
            movie_data.loc[len(movie_data)] = row

    # API 요청 결과 데이터프레임 저장
    movie_data.to_csv(csv_path + movie_data_csv_name, index=False)
    print("수집을 완료했습니다.")

if __name__ == "__main__":
    movie_data_manufacture()
    TMDB_API_call()
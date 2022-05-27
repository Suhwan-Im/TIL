import requests
from pprint import pprint
import json

# 누적 인기 영화
def movie_popular(page):
    # URL 및 요청변수 설정
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    page = int(page)
    params = {
        'api_key': '7065898125e3c5540c241eebabdd426e',
        'language': 'ko-KR',
        'page': page,
        'region': 'KR',
        }
    
    # 결과를 받아서 json형식의 data변수로 저장
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()

    movie_popular_list = []
    for i in range(len(data.get('results'))):
        movie_JSON = {}
        id = data.get('results')[i]['id']
        title = data.get('results')[i]['title']
        overview = data.get('results')[i]['overview']
        release_date = data.get('results')[i]['release_date']
        poster_path = data.get('results')[i]['poster_path']
        genre_ids = data.get('results')[i]['genre_ids']
        vote_average = data.get('results')[i]['vote_average']

        
        # movie_JSON['model'] = 'rates.movierate'
        # movie_JSON['title'] = title
        # movie_JSON['overview'] = overview
        # movie_JSON['release_date'] = release_date
        # movie_JSON['poster_path'] = poster_path
        # movie_JSON['genre_ids'] = genre_ids
        # movie_JSON['vote_average'] = vote_average

        # 세부 항목들을 'fields'로 감싸는 방법
        movie_JSON['model'] = 'rates.movierate'
        fields = {}
        fields['title'] = title
        fields['overview'] = overview
        fields['release_date'] = release_date
        fields['poster_path'] = poster_path
        fields['genre_ids'] = genre_ids
        fields['vote_average'] = vote_average
        movie_JSON['fields'] = fields

        movie_popular_list.append(movie_JSON)
    
    return movie_popular_list


# 영화 리스트 출력
if __name__ == '__main__':
    movie_list = []
    for i in range(1,4):
        if i < 3:
            movie_list.extend(movie_popular(i))
        else:
            movie_list.extend(movie_popular(i)[:10])
    
    # JSON 리스트에 PK값도 넣어주기
    for j in range(len(movie_list)):
        movie_list[j]['pk'] = j + 1

    pprint(movie_list)
    print(len(movie_list))

    with open('movie_list.json', 'w', encoding='utf8') as jsonfile:
        json.dump(movie_list, jsonfile, indent=4, sort_keys=True, ensure_ascii=False)

# python manage.py loaddata
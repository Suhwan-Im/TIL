import requests
from pprint import pprint

# 현재 상영중인 영화
# def movie_now_playing(page):
#     # URL 및 요청변수 설정
#     BASE_URL = 'https://api.themoviedb.org/3'
#     path = '/movie/now_playing'
#     page = int(page)
#     params = {
#         'api_key': '7065898125e3c5540c241eebabdd426e',
#         'language': 'ko-KR',
#         'page': page,
#         'region': 'KR',
#         }
    
#     # 결과를 받아서 json형식의 data변수로 저장
#     response = requests.get(BASE_URL+path, params=params)
#     data = response.json()

#     movie_now_playing_list = []
#     for i in range(len(data.get('results'))):
#         movie_now_playing_list.append(data.get('results')[i]['title'])
    
#     return movie_now_playing_list

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
        title = data.get('results')[i]['title']
        overview = data.get('results')[i]['overview']
        release_date = data.get('results')[i]['release_date']
        poster_path = data.get('results')[i]['poster_path']
        genre_ids = data.get('results')[i]['genre_ids']
        vote_average = data.get('results')[i]['vote_average']

        movie_popular_list.append([title, overview, release_date, poster_path, genre_ids, vote_average])
    
    return movie_popular_list


# 영화 리스트 출력
if __name__ == '__main__':
    movie_list = []
    for i in range(1,2):
        movie_list.extend(movie_popular(i))

    # print(len(movie_list))
    # pprint(movie_list)

like = 878#, 14]
dislike = 16

suggest_list = []
for i in range(len(movie_list)):
    if (dislike not in movie_list[i][4]) and (like in movie_list[i][4]): # <- 선호 및 비선호 장르가 int 타입인 경우
    #if (dislike not in movie_list[i][4]) and (all(elem in movie_list[i][4]  for elem in like)): # <-- 선호 장르가 list 타입인 경우
        suggest_list.append(movie_list[i])

pprint(suggest_list)
print(len(suggest_list))
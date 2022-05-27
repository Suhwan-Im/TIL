import requests
from pprint import pprint

def weather(reg):
    # URL 및 요청변수 설정
    BASE_URL = 'https://api.openweathermap.org'
    path = '/data/2.5/weather'
    region = str(reg)
    params = {'q': region, 'appid': '##API_KEY##'}
    
    # 결과를 받아서 json형식의 data변수로 저장
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    # 날씨 데이터 반환
    name = data.get('name')
    weather = data.get('weather')
    main = weather[0].get('main')
    return [name, main]

# 날씨 데이터 출력
print(f"서울: {weather('Seoul')}")
print(f"대전: {weather('Daejeon')}")
print(f"대구: {weather('Daegu')}")
print(f"부산: {weather('Busan')}")
print(f"구미: {weather('Gumi')}")
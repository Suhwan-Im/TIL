# SWEA #1206 - View



### #1차 - 220205

```python
# (10개의 테스트 케이스)
for cycle in range(10):
    ### 입력
    N = int(input())
    list_building = list(map(int, input().split()))
    
    
    ### 계산
    # N x 255 범위의 0 리스트 만들기
    list_area = []
    for i in range(N):
        list_area.append([0] * 255)
    
    # 빌딩자리를 1로 채우기
    for i in range(N):
        for j in range(list_building[i]):
            list_area[i][j] = 1
    
    # 양옆 두칸이 0인 집 모두 찾아서 개수 누적
    cnt = 0
    for i in range(2, N-2):
        for j in range(list_building[i]):
            if list_area[i-2][j] == 0 and list_area[i-1][j] == 0 and list_area[i+1][j] == 0 and list_area[i+2][j] == 0:
                cnt += 1
            else:
                pass
    
    ### 출력
    print(f"#{cycle+1} {cnt}")
```

- 제출 / 맞음

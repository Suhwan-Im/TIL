# SWEA #1208 - Flatten



### #1차 - 220205

```python
# (10개의 테스트 케이스)
for cycle in range(10):
    ### 입력
    N = int(input())
    list_box = list(map(int, input().split()))
    
    ### 계산
    for i in range(N):
        list_box[list_box.index(max(list_box))] -= 1
        list_box[list_box.index(min(list_box))] += 1
    
    diff = max(list_box) - min(list_box)
    
    ### 출력
    print(f"#{cycle+1} {diff}")
```

- 제출 / 맞음

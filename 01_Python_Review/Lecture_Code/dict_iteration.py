d = {10: 'a', 20: 'b', 30: 'c'}

# 1. key만 출력
# for문으로 딕셔너리를 순회하면 key만 나옴
for key in d:
    print(key, d[key])

# 2. key와 value 함께 출력
# items()를 쓰면 key와 value를 함께 꺼낼 수 있음
for key, val in d.items():
    print(key, val)

# 3. 인덱스와 함께 출력
# enumerate(d)는 인덱스와 key를 반환
for i, key in enumerate(d):
    print(i, key, d[key])

# 4. 인덱스, key, value 모두 출력
# enumerate(d.items())는 인덱스와 (key, value) 쌍을 반환
for i, (key, val) in enumerate(d.items()):
    print(i, key, val)
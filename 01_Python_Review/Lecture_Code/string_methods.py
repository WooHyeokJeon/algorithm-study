s = "This is the class of Python programming!"

# 1. 문자열의 시작과 끝 문자 확인
print(s.startswith('t')) #결과가 Flase가 나오는 이유: startswith()는 대소문자를 구별하기 때문
print(s.startswith('T'))
print(f"{s.endswith('!')}\n")

# 2. 특정 문자의 개수 세기
print(s.count('i'))
print(f"{s.count('t')}\n")

# 3. 특정 문자의 위치 찾기
print(s.index('i')) #index()는 처음 나오는 문자의 위치를 반환
print(s.index('i', 3)) #3번째 위치 이후에서 처음 나오는 'i'의 인덱스 위치 출력
print(f"{s.index('class')}\n") #문자열도 찾을 수 있음 (문자열의 시작 위치 반환)

# print(f"{s.index('JeonWooHyeok')}\n")
#   -> 위 코드처럼 찾지 못하는 걸 index 인자로 넘기면 [ValueError: substring not found] 발생

# 4. 특정 문자나 문자열 찾기
print(s.find('class'))
print(s.find('Python'))
print(f"{s.find('JeonWooHyeok')}\n")
# -> 위 코드처럼 find는 찾지 못한 경우 ValueError를 발생시키지 않고 -1을 리턴해줌

# 5. 대문자/소문자 변환
print(s.upper())
print(s.lower())
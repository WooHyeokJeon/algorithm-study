set1 = {1, 2, 3}
set2 = {2, 4, 5}

# 1. 원소 추가
# add() - 원소 하나를 추가
set1.add(4)
print(set1)

# update() - 다른 집합의 원소들을 모두 추가
set1.update(set2)
print(set1)

# 2. 원소 제거
# pop() - 임의의 원소 하나를 제거하고 반환 (어떤 원소가 나올지 정해져 있지 않음)
print(set1.pop())
print(set1)

# discard() - 원소를 제거, 없는 원소를 제거해도 에러 없음
set1.discard(3)
print(set1)
set1.discard(3)   # 이미 없는 원소이지만 에러 없음
print(set1)

# remove() - 원소를 제거, 없는 원소를 제거하면 KeyError 발생
"""
set1.remove(3)    # KeyError 발생
"""
set1.remove(2)
print(set1)

# 3. 복사 및 초기화
# copy() - 집합을 복사
set2 = set1.copy()
print(set2)

# clear() - 모든 원소 제거
set1.clear()
print(set1)
mylist = [["co", 1, "Q"], ["bar", 0, "Z"], ["after", 3, "X"], ["data", 2, "Y"]]

# 1. 기본 정렬
# sorted() - 정렬된 새 리스트를 반환 (원본 mylist는 그대로)
# 리스트 안의 리스트는 첫 번째 원소를 기준으로 정렬됨
print(sorted(mylist))
# [['after', 3, 'X'], ['bar', 0, 'Z'], ['co', 1, 'Q'], ['data', 2, 'Y']]

# 2. 내림차순 정렬
# reverse=True - 큰 순서대로 정렬
print(sorted(mylist, reverse=True))
# [['data', 2, 'Y'], ['co', 1, 'Q'], ['bar', 0, 'Z'], ['after', 3, 'X']]

# 3. 두 번째 원소(인덱스 1) 기준 정렬
# key=lambda x: x[1] - 각 리스트의 두 번째 원소를 기준으로 정렬
print(sorted(mylist, key=lambda x: x[1]))
# [['bar', 0, 'Z'], ['co', 1, 'Q'], ['data', 2, 'Y'], ['after', 3, 'X']]

# 4. 첫 번째 원소 길이 기준 정렬
# key=lambda x: len(x[0]) - 첫 번째 원소의 글자 수를 기준으로 정렬
print(sorted(mylist, key=lambda x: len(x[0])))
# [['co', 1, 'Q'], ['bar', 0, 'Z'], ['data', 2, 'Y'], ['after', 3, 'X']]
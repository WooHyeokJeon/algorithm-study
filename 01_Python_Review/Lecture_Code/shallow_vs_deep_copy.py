import copy

# 1. 리스트 얕은 복사와 깊은 복사
# copy() - 바깥 리스트만 복사 (안쪽 리스트는 공유)
# deepcopy() - 안쪽 리스트까지 모두 복사
o = [1, [2, 3], 4]
s = copy.copy(o)
d = copy.deepcopy(o)

o[1][0] = 200
print(o)   # [1, [200, 3], 4]
print(s)   # [1, [200, 3], 4] (안쪽 리스트를 공유하므로 같이 바뀜)
print(d)   # [1, [2, 3], 4]   (완전히 독립된 복사본)

# 2. 딕셔너리 얕은 복사와 깊은 복사
# 딕셔너리도 안쪽 리스트는 얕은 복사에서 공유됨
o = {'a': 1, 'b': [2, 3]}
s = copy.copy(o)
d = copy.deepcopy(o)

o['b'].append(100)
print(o)   # {'a': 1, 'b': [2, 3, 100]}
print(s)   # {'a': 1, 'b': [2, 3, 100]} (안쪽 리스트 공유)
print(d)   # {'a': 1, 'b': [2, 3]}      (독립된 복사본)

# 3. 사용자 정의 클래스에서의 복사
# 클래스 객체도 얕은 복사는 내부 객체를 공유함
class MyClass:
    def __init__(self, value):
        self.value = value

o = MyClass([1, 2, 3])
s = copy.copy(o)
d = copy.deepcopy(o)

o.value.append(100)
print(o.value)   # [1, 2, 3, 100]
print(s.value)   # [1, 2, 3, 100] (내부 리스트 공유)
print(d.value)   # [1, 2, 3]      (독립된 복사본)
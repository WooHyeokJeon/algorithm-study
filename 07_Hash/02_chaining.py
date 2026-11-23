# 1. 체이닝 해시 테이블 클래스
class ChainingHashTable:
    def __init__(self, m):
        self.m = m
        self.table = [[] for _ in range(m)]

    # 2. 해시 함수 (나눗셈 방법)
    def h(self, x):
        return x % self.m

    # 3. 삽입 (체인 맨 앞에 추가)
    def insert(self, x):
        self.table[self.h(x)].insert(0, x)

    # 4. 검색
    def search(self, x):
        for y in self.table[self.h(x)]:
            if y == x:
                return True
        return False

    # 5. 삭제
    def delete(self, x):
        chain = self.table[self.h(x)]
        if x in chain:
            chain.remove(x)


# 6. 테스트
if __name__ == "__main__":
    t = ChainingHashTable(13)
    for x in [39, 40, 94, 43, 44, 70, 3, 42, 55, 86, 47, 74, 76, 13]:
        t.insert(x)

    print(t.table[0])   # [13, 39]
    print(t.table[3])   # [55, 42, 3, 94]
    print(t.search(42))   # True
    print(t.search(99))   # False

    t.delete(42)
    print(t.table[3])   # [55, 3, 94]
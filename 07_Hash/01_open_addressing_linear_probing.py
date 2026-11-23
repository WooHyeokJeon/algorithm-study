# 1. 삭제 표시
DELETED = "DELETED"


# 2. 개방 주소 방법 해시 테이블 클래스
class OpenAddressingHashTable:
    def __init__(self, m):
        self.m = m
        self.table = [None] * m

    # 3. 해시 함수 (나눗셈 방법)
    def h(self, x):
        return x % self.m

    # 4. 선형 조사 (h_i(x) = (h(x) + i) mod m)
    def probe(self, x, i):
        return (self.h(x) + i) % self.m

    # 5. 삽입
    def insert(self, x):
        for i in range(self.m):
            j = self.probe(x, i)
            if self.table[j] is None or self.table[j] == DELETED:
                self.table[j] = x
                return j
        print("테이블 오버플로우")

    # 6. 검색
    def search(self, x):
        for i in range(self.m):
            j = self.probe(x, i)
            if self.table[j] == x:
                return j
            if self.table[j] is None:
                return None
        return None

    # 7. 삭제
    def delete(self, x):
        j = self.search(x)
        if j is not None:
            self.table[j] = DELETED


# 8. 테스트
if __name__ == "__main__":
    t = OpenAddressingHashTable(13)
    for x in [25, 13, 16, 15, 7, 28, 31, 20, 1, 38]:
        t.insert(x)

    print(t.search(38))   # 6
    print(t.search(20))   # 8
    print(t.search(99))   # None

    t.delete(1)
    print(t.table[1])   # DELETED
    print(t.search(38))   # 6
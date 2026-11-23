# 1. 불일치 문자 테이블
def make_bct(pattern):
    bct = [-1] * 256

    for i in range(len(pattern)):
        bct[ord(pattern[i])] = i

    return bct


# 2. 테스트
if __name__ == "__main__":
    bct = make_bct("ABAAB")

    print(bct[ord("A")])   # 3
    print(bct[ord("B")])   # 4
    print(bct[ord("C")])   # -1
# 1. KMP 실패 테이블
def make_kmp_table(pattern):
    m = len(pattern)
    border = [-1] * (m + 1)
    i = 0
    j = -1

    while i < m:
        while j >= 0 and pattern[i] != pattern[j]:
            j = border[j]

        i += 1
        j += 1
        border[i] = j

    return border


# 2. 테스트
if __name__ == "__main__":
    print(make_kmp_table("BAABAB"))   # [-1, 0, 0, 0, 1, 2, 1]
    print(make_kmp_table("BAABABAA"))   # [-1, 0, 0, 0, 1, 2, 1, 2, 3]
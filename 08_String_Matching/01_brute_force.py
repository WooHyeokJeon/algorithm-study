# 1. 브루트포스 탐색
def brute_force(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            return i

    return -1


# 2. 테스트
if __name__ == "__main__":
    text = "boboycatsoaropt"

    print(brute_force(text, "soar"))   # 8
    print(brute_force(text, "dog"))   # -1
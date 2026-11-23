import importlib

table_file = importlib.import_module("02_kmp_table")


# 1. KMP 탐색
def kmp_search(pattern, border, text):
    m = 0
    i = 0
    t_len = len(text)
    p_len = len(pattern)

    while m + i < t_len:
        if pattern[i] == text[m + i]:
            if i == p_len - 1:
                return m

            i += 1
        else:
            if border[i] > -1:
                m = m + i - border[i]
                i = border[i]
            else:
                i = 0
                m += 1

    return -1


# 2. 테스트
if __name__ == "__main__":
    pattern = "BAABAB"
    border = table_file.make_kmp_table(pattern)

    print(kmp_search(pattern, border, "BAABAABAB"))   # 3
    print(kmp_search(pattern, border, "BAABA"))   # -1
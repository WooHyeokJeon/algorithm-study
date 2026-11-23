import importlib

bct_file = importlib.import_module("04_bad_character_table")
gst_file = importlib.import_module("05_good_suffix_table")


# 1. Boyer-Moore 탐색
def boyer_moore_search(pattern, text, bct, gst):
    m = len(pattern)
    n = len(text)
    i = 0

    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i+j]:
            j -= 1

        if j < 0:
            return i

        i += max(gst[j], j - bct[ord(text[i+j])])

    return -1


# 2. 테스트
if __name__ == "__main__":
    pattern = "GCAGAGAG"
    m = len(pattern)

    bct = bct_file.make_bct(pattern)
    suffix = [0] * m
    gst = [0] * m
    gst_file.build_gst(pattern, suffix, gst)

    print(boyer_moore_search(pattern, "BAAABGCAGAGAG", bct, gst))   # 5
    print(boyer_moore_search(pattern, "BAAAB", bct, gst))   # -1
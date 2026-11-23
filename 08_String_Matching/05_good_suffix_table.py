# 1. suffix 배열과 GST 계산
def build_gst(pattern, suffix, gst):
    m = len(pattern)

    # 1-1. suffix 배열
    suffix[m-1] = m
    g = m - 1

    for i in range(m-2, -1, -1):
        if i > g and suffix[i+m-1-f] < i-g:
            suffix[i] = suffix[i+m-1-f]
        else:
            if i < g:
                g = i
            f = i
            while g >= 0 and pattern[g] == pattern[g+m-1-f]:
                g -= 1
            suffix[i] = f - g

    # 1-2. GST 초기값
    for i in range(m):
        gst[i] = m

    # 1-3. case1 접두-접미 완전 일치
    j = 0
    for i in range(m-1, -1, -1):
        if suffix[i] == i + 1:
            while j < m - 1 - i:
                if gst[j] == m:
                    gst[j] = m - 1 - i
                j += 1

    # 1-4. case2 접미-접미 일치
    for i in range(0, m-1):
        gst[m-1-suffix[i]] = m - 1 - i


# 2. 테스트
if __name__ == "__main__":
    pattern = "ABCAB"
    suffix = [0] * len(pattern)
    gst = [0] * len(pattern)
    build_gst(pattern, suffix, gst)

    print(suffix)   # [0, 2, 0, 0, 5]
    print(gst)   # [3, 3, 3, 5, 1]

    pattern = "GCAGAGAG"
    suffix = [0] * len(pattern)
    gst = [0] * len(pattern)
    build_gst(pattern, suffix, gst)

    print(suffix)   # [1, 0, 0, 2, 0, 4, 0, 8]
    print(gst)   # [7, 7, 7, 2, 7, 4, 7, 1]
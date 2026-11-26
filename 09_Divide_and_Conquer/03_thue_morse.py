# 1. 투에-모스 문자열 (재귀)
def thue_morse(idx):
    if idx == 0:
        return 0

    if idx == 1:
        return 1

    if idx % 2 == 0:
        return thue_morse(idx // 2)
    else:
        return 1 - thue_morse(idx // 2)


# 2. 테스트
if __name__ == "__main__":
    print(thue_morse(5))   # 0
    print(thue_morse(7))   # 1
    print(thue_morse(8))   # 1
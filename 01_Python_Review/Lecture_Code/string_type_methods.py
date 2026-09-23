# 1. 문자열을 구성하는 것들 확인
# isalnum() - 영문자 + 숫자만 포함하면 True 반환
print("123abc".isalnum())

# isalpha() - 영문자만 포함하고 있으면 True 반환
print("123abc".isalpha())
print(f"{'abc'.isalpha()}\n")

# 2. 대소문자 변환
print("abc".islower())
print("abc".isupper())
print(f"{'ABC'.isupper()}\n")

# 3. 숫자 타입 확인
# isdecimal() - 10진수 숫자만 True 반환 (분수나 로마숫자는 Flase)
print("123".isdecimal())
print(f"{'12.3'.isdecimal()}\n")
# 비슷한 메소드로, isnumeric() - 숫자 형태를 전부 True로 반환 (분수나 로마숫자도 True)


# 4. 변수명으로 사용 가능한지 확인
# isidentifier() - 변수명 규칙에 맞으면 True 반환
print("myVariable".isidentifier())
print("my-var".isidentifier()) # 변수명에 하이픈은 넣을 수 없어 Flase 반환
print("123var".isidentifier()) # 숫자로 변수명을 시작할 수 없어서 Flase 반환
print(f"{'_var'.isidentifier()}\n")

#5. 출력 가능한지 확인
# isprintable() - 눈에 보이는 문자만 True 반환, 제어 문자는 Flase 반환
print("Hello".isprintable())
print("Hello\n".isprintable()) # \n은 출력 결과가 눈에 보이지 않아 Flase 반환
print("   ".isprintable())

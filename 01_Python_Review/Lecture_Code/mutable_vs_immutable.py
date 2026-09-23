# 아래 코드(5번째 줄 ~ 11번째 줄) 실행하면 오류
# 실행 시켜보면, "TypeError: 'tuple' object does not support item assignment"라는 에러 메시지가 출력.
# 이유는? Immutable 객체 특성 때문에. 아래 생성한 tuple은 대표적은 Immutable
"""
tuple1 = (0, 1, 2, 3)
tuple1[0] = 4
print(tuple1)

message = "Welcome to Python!"
message[0] = 'p'
print(message)
"""

#---------------------------------------------

# 아래 코드(17번째 줄 ~ 21번째 줄) 실행하면 성공
# 실행 시켜보면, ([300, 4, 5], 'myname')라는 결과가 출력 됨.
# 이유는? tup[0]은 리스트[3, 4, 5]여서. 리스트는 대표적인 Mutable
tup = ([3, 4, 5], 'myname')
tup[0][0] = 300
print(tup)

# 아래 코드(27번째 줄 ~ 28번째 줄) 실행하면 오류
# 실행 시켜보면, TypeError: 'str' object does not support item assignment라는 에러 메시지가 출력.
# 이유는? tup[1][0]은 존재하지만, tup[1]이 'myname'이라는 문자열인데, String도 Immutable이기 때문.
"""
tup[1][0] = 'M'
print(tup)
"""

#---------------------------------------------
# 최종 정리: Mutable VS Immutable
#
# Immutable (불변 - 값 자체를 수정 불가):
#   - int, float, bool: 값 자체는 절대 변하지 않음
#       헷갈리면 안되는게, 변수는 언제든 새로운 값을 가리킬 수 있음.
#           ex) x = 5; x=10 (가능)
#               하지만 "5"라는 값 자체는 영원히 "5"
#   - Tuple: 생성 후 요소 수정 불가
#       하지만, Tuple 안에 List가 있으면 List 부분은 수정 가능
#   - String: 생성 후 문자 수정 불가
#
# Mutable (가변 - 값 자체를 수정 가능):
#   - List: 요소 수정, 추가, 삭제 가능
#   - Dict: 키-값 수정, 추가, 삭제 가능
#   - Set: 요소 추가, 삭제 가능
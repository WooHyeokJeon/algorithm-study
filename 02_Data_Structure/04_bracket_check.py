# 1. 괄호 짝 정의
# pairs - 닫는 괄호를 키로, 짝이 되는 여는 괄호를 값으로 저장
pairs = {')': '(', ']': '[', '}': '{'}

# 2. 괄호 검사
# check_brackets() - 여는 괄호는 스택에 쌓고, 닫는 괄호가 나오면 가장 최근 여는 괄호와 짝이 맞는지 확인
def check_brackets(text):
    stack = []

    for ch in text:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack:
                return False
            if stack.pop() != pairs[ch]:
                return False

    # 스택이 비어 있어야 모든 괄호가 짝을 이룸
    return not stack

# 3. 테스트
print(check_brackets("{ A[(i+1)] = 0; }"))     # True
print(check_brackets("if ((i==0) && (j==0)"))   # False (닫는 괄호 부족)
print(check_brackets("A[(i+1])=0;"))            # False (짝이 맞지 않음)
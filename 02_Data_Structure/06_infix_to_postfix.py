import re

# 1. 연산자 정의
# OPERATORS - 계산에 쓰이는 연산자 목록
OPERATORS = ['+', '-', '*', '/', '^']

# 2. 연산자 우선순위
# precedence() - 연산자의 우선순위를 숫자로 반환 (값이 클수록 먼저 계산)
def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0

# 3. 수식을 토큰으로 나누기
# tokenize() - 숫자(소수 포함)와 연산자, 괄호를 하나씩 분리
def tokenize(exp):
    return re.findall(r'\d+\.?\d*|[()+\-*/^]', exp)

# 4. 중위 표기식 → 후위 표기식 변환
# infix_to_postfix() - 피연산자는 바로 출력하고, 연산자는 스택에 두었다가 우선순위에 따라 출력
def infix_to_postfix(exp):
    stack = []
    output = []

    for token in tokenize(exp):
        if token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()   # '(' 제거

        elif token in OPERATORS:
            # ^는 오른쪽 결합이므로 우선순위가 같아도 pop하지 않음
            while stack and stack[-1] != '(' and (
                precedence(stack[-1]) > precedence(token) or
                (precedence(stack[-1]) == precedence(token) and token != '^')
            ):
                output.append(stack.pop())
            stack.append(token)

        else:
            output.append(token)   # 피연산자

    while stack:
        output.append(stack.pop())

    return ' '.join(output)

# 5. 후위 표기식 계산
# eval_postfix() - 숫자는 스택에 push, 연산자를 만나면 피연산자 2개를 pop해서 계산 후 다시 push
def eval_postfix(exp):
    stack = []

    for token in exp.split():
        if token in OPERATORS:
            op2 = stack.pop()
            op1 = stack.pop()

            if token == '+':
                stack.append(op1 + op2)
            elif token == '-':
                stack.append(op1 - op2)
            elif token == '*':
                stack.append(op1 * op2)
            elif token == '/':
                stack.append(op1 / op2)
            elif token == '^':
                stack.append(op1 ** op2)
        else:
            stack.append(float(token))

    return stack.pop()

# 6. 테스트
print(infix_to_postfix("1 - 3 * 2"))      # 1 3 2 * -
print(infix_to_postfix("2 ^ 3 ^ 2"))      # 2 3 2 ^ ^
print(eval_postfix("2 3 2 ^ ^"))          # 512.0

exp = "3.5+5*(2^3-40.11)^(2+1*2.0)-8.5"
postfix = infix_to_postfix(exp)
print(postfix)
print(eval_postfix(postfix))
# 1. 후위 표기식 계산
# eval_postfix() - 숫자는 스택에 push하고, 연산자를 만나면 피연산자 2개를 pop해서 계산한 뒤 다시 push
def eval_postfix(exp):
    stack = []

    for token in exp.split():
        if token not in '+-*/':
            stack.append(int(token))
        else:
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

    return stack.pop()

# 2. 테스트
print(eval_postfix("8 2 / 3 - 3 2 * +"))   # 1.0 (8/2=4, 4-3=1, 3*2=6, 1+6=7 이 아니라 아래 주석 참고)
print(eval_postfix("1 3 2 * -"))           # -5
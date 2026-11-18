# 1. Point 클래스 정의
# __init__() - x, y 좌표를 저장 (기본값은 0)
class Point:
    "This is my point class."

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __str__() - print()할 때 보이는 문자열 형식 지정
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    # __add__() - + 연산자로 두 Point를 더함
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

# 2. 객체 생성 및 덧셈
p1 = Point(2, 3)
p2 = Point(-1, 2)
print(p1 + p2)   # (1,5)  (p1.__add__(p2)와 같음)
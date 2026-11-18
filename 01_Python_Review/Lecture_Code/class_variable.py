# 1. 클래스 변수 정의
# a는 클래스 변수라서 클래스 자체에 저장됨
class MyClass:
    "This is my first class"
    a = 10

    def func(self):
        print('Hello')

# 2. 클래스 변수 출력 및 수정
# 클래스 이름으로 바로 접근 가능
print(MyClass.a)     # 10
MyClass.a = 200
print(MyClass.a)     # 200

# 3. 인스턴스를 통한 접근
# ob는 MyClass의 인스턴스
ob = MyClass()
ob.func()            # Hello

# 4. 인스턴스 변수 생성
# ob.a = 500은 클래스 변수 a를 바꾸는 것이 아니라
# ob에만 새로 a라는 인스턴스 변수를 만드는 것
ob.a = 500
print(MyClass.a, ob.a)   # 200 500
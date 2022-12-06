class MyClass(object):
    def method_a(self):
        pass

    def method_b(self):
        print("Method B")

c = MyClass()

# method 내부에 아무 처리가 없다면 에러가 발생한다.
# 이를 방지하기 위해 pass를 넣으면 아무것도 하지 않고 에러발생도 방지할 수 있다.
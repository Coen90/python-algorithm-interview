"""
Loop의 반복 동작을 제어하는 루틴
제너레이터만 생성하여 필요할 때 언제든 숫자를 만들어낼 수 있다.
yield 구문을 사용하면 제너레이터 리턴 받음
중간값을 리턴하고 종료되지 않으며 맨 끝까지 실행됨
"""
def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

print(get_natural_number()) # <generator object get_natural_number at 0x000002BB46184DC0>

g = get_natural_number()
for _ in range(0, 100):
    print(next(g))

def generator():
    yield 1
    yield 'string'
    yield True
g2 = generator()
print(next(g2)) # 1
print(next(g2)) # string
print(next(g2)) # True
a = list()

b = []

# python의 list 에는 여러 타입의 자료형을 단일 리스트에 저장 가능하다.

a.append(1)
a.append(2)
a.append("안녕")
a.append(True)

print(a)
print(a[3])

# slicing a:b -> index a 부터 b 이전까지
print(a[1:3])

print(a[:len(a)])
print(a[2:])

try:
    print(a[5])
except IndexError:
    print("인덱스를 초과합니다.")

# list 값 삭제
del a[1]
print(a)
a.remove(True)
print(a)

try:
    a.remove('True')
except ValueError:
    print("list에 존재하지 않는 값입니다.")

a = 1
b = True
print(a == b)
print(a is b)

print(id(a), id(b))

# python의 리스트는 객체로 되어있는 모든 자료형을 포인터로 연결한다.
# python은 모든 것이 객체이며 파이선의 리스트는 각 객체에 대한 포인터 목록을 관리하는 형태로 구현되어있다.
# 사실상 연결리스트에 대한 포인터 목록을 배열 형태로 관리하는것.
11
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
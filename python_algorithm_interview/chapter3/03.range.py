import sys

list_range = list(range(5))
print(list_range) # [0, 1, 2, 3, 4]

print(range(5)) # range(0, 5)

print(type(range(5))) # <class 'range'>

for i in range(5):
    print(i, end=' ') # i 다음 end가 옴, end 없으면 \ln
print()
print()
print()
# range() 는 range 클래스 리턴. for문에서 사용할 경우 내부적으로 제너레이터의 next()를 호출하듯 매번 다음 숫자를 생성
# range() 한수는 제너레이터 range 클래스를 리턴하는형태!

a = [n for n in range(1000000)]
b = range(1000000)

print(len(a)) # 1000000
print(len(b)) # 1000000

print(len(a) == len(b)) # True

# 하지만 a에는 이미 생성된 값이 담겨있고, b는 생성해야 한다는 조건만 존재.
# print(a) # real 0 to 1000000 List
print(type(a)) # <class 'list'>
print(b) # range(0, 1000000)
print(type(b)) # <class 'range'>

print(sys.getsizeof(a)) # 8448728
print(sys.getsizeof(b)) # 48 # 생성조건만 가지고 있기 때문

print(a[999]) # 999
print(b[999]) # 999
# 열거형. 여러 자료형(list, set, tuple 등) 을 인덱스를 포함한 enuermate 객체로 리턴
a = [1, 2, 3, 2, 45, 2, 5]
print(a) # [1, 2, 3, 2, 45, 2, 5]

print(enumerate(a)) # <enumerate object at 0x000001DA5AF2E5C0>
print(list(enumerate(a))) # [(0, 1), (1, 2), (2, 3), (3, 2), (4, 45), (5, 2), (6, 5)]

b = ['a1', 'b2', 'c3']

for i in range(len(b)): # 0 a1, 1 b2, 2 c3,
    print(i, b[i], end=', ')

print()

i = 0
for v in b: # 0 a1, 1 b2, 2 c3,
    print(i, v, end=', ')
    i += 1

print()

for i, v in enumerate(b): # 0 a1, 1 b2, 2 c3,
    print(i, v, end=', ')
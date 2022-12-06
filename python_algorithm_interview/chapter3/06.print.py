a = 'A1'
b = 'B2'

print(a, b) # A1 B2

print(a, b, sep=' ') # A1 B2
print(a, b, sep=',') # A1,B2
print(a, b, sep='|') # A1|B2

# print()는 항상 줄바꿈 자바의 System.out.println()과 같음
print(a, end=' ') # 이렇게하면 줄바꿈 대신 end를 사용함.
print(b)

# 리스트 출력시에는 join()을 사용한다
list_test = ['A', 'B']
print(list_test) # ['A', 'B']
print(' '.join(list_test)) # A B

# 중괄호를 사용하여 대입 가능하다. index 생략 가능
idx = 1
fruit = 'Apple'
print('{0}: {1}'.format(idx + 1, fruit)) # 2: Apple
print('{}: {}'.format(idx + 1, fruit)) # 2: Apple
print(f'{idx + 1}: {fruit}') # 2: Apple
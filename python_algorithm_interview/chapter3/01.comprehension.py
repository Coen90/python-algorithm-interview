# When List Comprehension
list_comprehension = [n * 2 for n in range(1, 10 + 1) if n % 2 == 1]

print(list_comprehension)

# When Not List Comprehension
a = []
for n in range(1, 10 + 1):
    if n % 2 == 1:
        a.append(n * 2)
print(a)

original = {"key1": "value1", "key22": "value2", "key33": "value3", "key4": "value4", "key5": "value5", "key6": "value6"}
# When Dictionary Comprehension
dic_com = {key: value for key, value in original.items() if len(key) == 4}
print("dic_com", dic_com)

# When Not Dictionary Comprehension
dic_not_com = {}
for key, value in original.items():
    if len(key) == 4:
        dic_not_com[key] = value
print("dic_not_com", dic_not_com)
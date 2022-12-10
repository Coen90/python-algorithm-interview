# defaultdict, Counter, OrderedDict
from collections import defaultdict, Counter, OrderedDict

base_dict = {"현태": 1000, "이시카와": 1500, "크리스챤": 1600, "현태": 1400}
#
# print(collections.defaultdict(base_dict))

default_dict_test = defaultdict(int)
default_dict_test["A"] += 1

default_dict_test["A"] = 1
default_dict_test["B"] = "data"

print(default_dict_test)

default_dict_test = base_dict

print(default_dict_test)

print(defaultdict(int))

counter_test = [1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5]

counter_obj = Counter(counter_test)
print(counter_obj.most_common(2))

OrderedDict({"apple": 4, "banana": 3, "mango": 6})
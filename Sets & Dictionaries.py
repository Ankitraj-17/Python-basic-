## 1.Input two sets and print union, intersection, and difference.
# s1 = set(input().split())
# s2 = set(input().split())
# print(s1 | s2)
# print(s1 & s2)
# print(s1 - s2)


## 2.Create a dictionary of 5 students marks and print topper.
# marks = {}
# for _ in range(5):
#     name = input()
#     mark = int(input())
#     marks[name] = mark
# topper = max(marks, key=marks.get)
# print(topper, marks[topper])


## 3.Word frequency counter from a paragraph (use dict).
# para = input().split()
# freq = {}
# for word in para:
#     freq[word] = freq.get(word, 0) + 1
# print(freq)


## 4.Remove a key-value pair from a dictionary.
# d = {'a': 1, 'b': 2, 'c': 3}
# key = input()
# d.pop(key, None)
# print(d)


## 5.Convert two lists (keys, values) into a dictionary.
# keys = input().split()
# values = input().split()
# d = dict(zip(keys, values))
# print(d)


## 6.Reverse a dictionary (swap keys & values).
# d = {'a': 1, 'b': 2, 'c': 3}
# reversed_d = {v: k for k, v in d.items()}
# print(reversed_d)


## 7.Find common values between two dictionaries.
# d1 = {'a': 1, 'b': 2, 'c': 3}
# d2 = {'b': 2, 'd': 4, 'c': 3}
# common = set(d1.values()) & set(d2.values())
# print(common)


## 8.Count how many unique values exist across dictionary items.
# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
# print(len(set(d.values())))


## 9.Input a list and print all unique elements using a set.
# lst = [int(x) for x in input().split()]
# print(set(lst))



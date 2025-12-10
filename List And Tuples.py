## 1.Input 10 numbers into a list and print the second largest.
# nums = [int(x) for x in input().split()][:10]
# u = sorted(set(nums), reverse=True)
# print(u[1] if len(u) > 1 else u[0])

## 2.Remove duplicates from a list without using set().
# nums = [int(x) for x in input().split()]
# unique = []
# for x in nums:
#     if x not in unique:
#         unique.append(x)
# print(unique)
# nums = [int(x) for x in input().split()]
# unique = []
# for x in nums:
#     if x not in unique:
#         unique.append(x)
# print(unique)


## 3.Count how many times each item appears in a list.
# nums = [int(x) for x in input().split()]
# counts = {}
# for x in nums:
#     counts[x] = counts.get(x, 0) + 1
# print(counts)
# nums = [int(x) for x in input().split()]
# counts = {}
# for x in nums:
#     counts[x] = counts.get(x, 0) + 1
# print(counts)


## 4.Merge two lists and sort them.
# l1 = [int(x) for x in input().split()]
# l2 = [int(x) for x in input().split()]
# print(sorted(l1 + l2))


## 5.Convert a list to tuple and tuple back to list.
# nums = [int(x) for x in input().split()]
# t = tuple(nums)
# lst = list(t)
# print(t)
# print(lst)

## 6.Find the sum of all elements in a list without using sum().
# nums = [int(x) for x in input().split()]
# total = 0
# for x in nums:
#     total += x
# print(total)


## 7.Reverse a list using slicing.
# nums = [int(x) for x in input().split()]
# print(nums[::-1])

## 8.Given a tuple of numbers, print all numbers greater than 50.
# t = tuple(int(x) for x in input().split())
# print([x for x in t if x > 50])


## 9.Find the index of a value in a tuple (handle value not present).
# t = tuple(int(x) for x in input().split())
# v = int(input())
# try:
#     print(t.index(v))
# except ValueError:
#     print(-1)


## 10.Multiply all elements of a list.
# nums = [int(x) for x in input().split()]
# prod = 1
# for x in nums:
#     prod *= x
# print(prod)



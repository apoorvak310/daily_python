#1. Flatten

# nums = [1, [2, 3], [4, [5, 6]], 7]
# output = []
# def flatten(x):
#     for i in x:
#         if type(i) == list:
#             flatten(i)
#         else:
#             output.append(i)
#     return output
# res = flatten(nums)
# print(res)

#2. sum of [1, [2, [3, 4]], [5, [6, [7]]]]

# nums = [1, [2, [3, 4]], [5, [6, [7]]]]
# output = []
# def flatten(l):
#     for i in l:
#         if type(i) == list:
#             flatten(i)
#         else:
#             output.append(i)
#     return output

# def list_sum(lst):
#     return sum(lst)

# x = flatten(nums)
# s = list_sum(x)
# print(s)

#3. 2 decorators to sort a list in ascending and descending order
# def sort_rev(x):
#     rev = x[::-1]
#     return rev

# def ascending(fun):
#     def inner1():
#         x = fun()
#         s = sorted(x)
#         return s
#     return inner1

# def descending(fun):
#     def inner2():
#         y = fun() #list display
#         x = sort_rev(y)
#         return x
#     return inner2

# @ascending
# def list_display():
#     a = [2, 4, 8, 5, 3]
#     return a
# res = list_display()
# print(res)

# @descending
# def list_display():
#     a = [2, 4, 8, 5, 3]
#     return a
# r = list_display()
# print(r)

#4. divide a number into 4 parts using generator
# n = 103
# def divide4(num):
#     i = 1
#     s = 0
#     while i <= 4:
#         if i <= 3:
#             s += num//4
#             yield num//4
#         i += 1
#     yield num-s
# for i in divide4(n):
#     print(i)
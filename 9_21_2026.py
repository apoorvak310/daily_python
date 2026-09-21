# # Given a list of integers, display the elements whose indexes are both prime numbers and Fibonacci numbers.
# def isfibo(n):
#     if n == 0 or n == 1:
#         return n
#     limit = n
#     a = 0
#     b = 1
#     c = a+b
#     while c <= limit:
#         c = a+b
#         if c == n:
#             return n
#         a = b
#         b = c
#     return False

# def prime(n):
#     for i in range(2, (n//2)+1):
#         if n % i == 0:
#             return False
#     return n

# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in range(len(nums)):
#     if prime(i):
#         if isfibo(i):
#             print(nums[i])

#2. Write a function max_after_removal(n, digit) that removes one occurrence of the given digit from the number and returns the maximum possible number. If the digit occurs multiple times, try removing it from each occurrence and find which removal produces t
def max_after_removal(n,digit):
    new = str(n)
    res = ""
    for ch in new:
        if ch != digit:
            res += ch
    return res
num = 154325
res = max_after_removal(num,5)
print(res)
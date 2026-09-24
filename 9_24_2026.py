# def check_number(n):
#     res = 0
#     while res < n:
#         res += 2
#         yield res
# for i in check_number(48):
#     print(i)

s1 = {10,20,30,40,50}
s2 = {20,30,60,70}
s3 = {30,40,80,90}

a = s1.intersection(s2)
b = s2.intersection(s3)
c = s3.intersection(s1)
res1 = a.union(b)
print(c.union(res1))
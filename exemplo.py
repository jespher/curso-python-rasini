# a = [1, 2, 3]

a = (1, 2, 3)

# a2 = []
#
# for i in a1:
#     a2.append(i * 2)
#
# print(a2)

m = map(lambda i: i * 2, a)
print(list(m))

print(tuple(map(lambda i: i ** 2, a)))

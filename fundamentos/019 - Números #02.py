from decimal import Decimal, getcontext

# print(1.1 + 2.2)

print(Decimal(1) / Decimal(7))
getcontext().prec = 8
print(Decimal(1) / Decimal(7))

print(Decimal.max(Decimal(1), Decimal(7)))

print(Decimal(1.1) + Decimal(2.2))
getcontext().prec = 6
print(Decimal(1.1) + Decimal(2.2))

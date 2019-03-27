# métodos mágicos

a = '123'

b = ' de Oliveira 4'

c = 'Jefferson'

d = ' Luis Rasini'

print(a + b)  # primeira opção
print(a.__add__(b))  # segunda opção
print(str.__add__(a, b))  # terceira opção

print(c + d)  # primeira opção
print(c.__add__(d))  # segunda opção
print(str.__add__(c, d))  # terceira opção

print(len(a))
print(a.__len__())
print(b.__len__())
print(a.__len__() + b.__len__())

print('1' in a)
print(a.__contains__('1'))

print('4' in b)
print(b.__contains__('4'))

print(' ' in b)
print(b.__contains__(' '))

print(' ' in a)
print(a.__contains__(' '))
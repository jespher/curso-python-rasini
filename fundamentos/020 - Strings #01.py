# Tipo String

# print(dir(str))

nome = 'Jefferson Luis'
print(nome[1])

mda = "Marca D'água"
print(mda)

dda = 'Dias D\'Ávila'
dda2 = "Dias D'Ávila"
print(dda)
print(dda2)

print(dda == dda2)
print(dda != dda2)

text = 'Texto entre apostrofos pode ter "aspas". Entendeu?? '
print(text)

text2 = "Texto entre apostrofos pode ter \"aspas\". Entendeu?? "
print(text2)

print(text == text2)

# texto de multiplas linhas
doc = """Podemos acreditar que tudo que a vida nos oferecerá no futuro é repetir o que fizemos ontem e hoje. Mas, 
se prestarmos atenção, vamos nos dar conta de que nenhum dia é igual a outro. Cada manhã traz uma benção escondida; 
uma benção que só serve para esse dia e que não se pode guardar nem desaproveitar.
Se não usamos este milagre hoje, ele vai se perder."""

print(doc)

doc2 = '''Podemos acreditar que tudo que a vida nos oferecerá no futuro é repetir o que fizemos ontem e hoje. Mas, 
se prestarmos atenção, vamos nos dar conta de que nenhum dia é igual a outro. Cada manhã traz uma benção escondida; 
uma benção que só serve para esse dia e que não se pode guardar nem desaproveitar.
Se não usamos este milagre hoje, ele vai se perder.'''

print(doc2)

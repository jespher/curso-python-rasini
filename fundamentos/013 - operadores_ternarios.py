# Operadores ternarios - 013 - operadores_ternarios.py

esta_chovendo = False

situacao1 = 'Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo]  # 'secas' = False / 'molhadas' = True

situacao2 = 'Hoje estou com as roupas ' + ('molhadas.' if esta_chovendo else 'secas.')

print(situacao1)
print(situacao2)

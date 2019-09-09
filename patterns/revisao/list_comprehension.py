'''
    Conceitos: Iterator e List Comprehension
    Permite criar novas listas a partir de listas existentes
    fazendo filtros ou modificações nos elementos originais
'''
NUMBERS = [1, 2, 3, 4, 5]

MOD = [n for n in NUMBERS if n % 2 == 0]

print(MOD)

MATRIX = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(MATRIX)

ROWS = [row for row in MATRIX]

print(ROWS)

ELEMENTS = [n for row in MATRIX for n in row]

print(ELEMENTS)

SQUARES = [n**2 for row in MATRIX for n in row]

print(SQUARES)

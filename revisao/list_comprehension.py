'''
    Conceitos: Iterator e List Comprehension
    Permite criar novas listas a partir de listas existentes
    fazendo filtros ou modificações nos elementos originais
'''
numbers = [1, 2, 3, 4, 5]

mod = [n for n in numbers if n % 2 == 0]

print(mod)

matrix = [[1,2,3], [4,5,6], [7,8,9]]

print(matrix)

rows = [row for row in matrix]

print(rows)

elements = [n for row in matrix for n in row]

print(elements)

squares = [n**2 for row in matrix for n in row]

print(squares)
import random

with open("input.txt", 'r') as a:
    dimensions = a.readline().split()
    M, N = int(dimensions[0]), int(dimensions[1])

matrix = [[random.randint(0, 100) for _ in range(N)] for _ in range(M)]

with open("input.txt", 'w') as d:
    for row in matrix:
        d.write(' '.join(map(str, row)) + '\n')

first_row_digits = list(map(int, matrix[0]))
digit_count = {digit: first_row_digits.count(digit) for digit in set(first_row_digits)}

with open("output.txt", 'w') as b:
    b.write(f"Matrix made and writen in 'input'.\n")
    b.write(f"the sizes: {M} x {N}\n")
    b.write(f"Matrix:\n")
    for row in matrix:
        b.write(' '.join(map(str, row)) + '\n')
    
    b.write(f"\nAll similar numbers:\n")
    for digit, count in digit_count.items():
        b.write(f"{digit}: {count}\n")



with open("input.txt", 'r') as file:
    lines = file.readlines()

matrix = [list(map(int, lines[0].split())), list(map(int, lines[1].split()))]

for line in lines[2:]:
    matrix.append(list(map(int, line.split())))

first_row = matrix[0]
digit_count = {digit: first_row.count(digit) for digit in set(first_row)}

with open("output.txt", 'w') as file:
    file.write(f"Matrix made from M and N 'input'.\n")
    file.write(f"Matrix:\n")
    for row in matrix:
        file.write(' '.join(map(str, row)) + '\n')
    
    file.write(f"\nAll similar numbers:\n")
    for digit, count in digit_count.items():
        file.write(f"{digit}: {count}\n")
with open('1.txt', 'r', encoding='utf-8') as f1:
    k1 = int(f1.readline().split(':')[1].strip())
    matrices1 = []
    for _ in range(k1):
        line = f1.readline()
        while not line[0].isdigit():
            line = f1.readline()
        n1, m1, *_ = map(int, line.split())
        matrix = []
        for _ in range(n1):
            row = list(map(int, f1.readline().split()))
            matrix.append(row)
        matrices1.append(matrix)

with open('2.txt', 'r', encoding='utf-8') as f2:
    k2 = int(f2.readline().split(':')[1].strip())
    matrices2 = []
    for _ in range(k2):
        line = f2.readline()
        while not line[0].isdigit() and 'Размер матрицы:' not in line:
            line = f2.readline()
        if 'Размер матрицы:' in line:
            try:
                n2, m2, *_ = map(int, line.split())
                matrix = []
                for _ in range(n2):
                    row = list(map(int, f2.readline().split()))
                    matrix.append(row)
                matrices2.append(matrix)
            except ValueError:
                print(f"Ошибка в формате строки в файле 2.txt: {line}")

e_matrices = []
while len(matrices1) > k2:
    e_matrices.append(matrices1.pop())
while len(matrices2) > k1:
    e_matrices.append(matrices2.pop())

with open('3.txt', 'w', encoding='utf-8') as f3:
    f3.write(f'количество матриц:{len(e_matrices)}\n')
    for matrix in e_matrices:
        n, m = len(matrix), len(matrix[0])
        f3.write(f'Размер матрицы: {n} {m}\n')
        for row in matrix:
            f3.write(' '.join(map(str, row)) + '\n')

with open('output.txt', 'w', encoding='utf-8') as f4:
    f4.write("Содержимое файла 1:\n")
    f4.write(open('1.txt', encoding='utf-8').read())
    f4.write("\n\nСодержимое файла 2:\n")
    f4.write(open('2.txt', encoding='utf-8').read())
    f4.write("\n\nСодержимое файла 3:\n")
    f4.write(open('3.txt', encoding='utf-8').read())
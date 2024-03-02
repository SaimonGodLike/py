r = int(input("How many rows?:"))
c = int(input("How many coloms?:"))

matrix = []
for i in range(r):
    row = list(map(int, input(f"Give me elements for {i + 1}, divide it with space: ").split()))
    matrix.append(row)

is_ordered = lambda col: all(col[i] <= col[i + 1] for i in range(len(col) - 1)) or all(col[i] >= col[i + 1] for i in range(len(col) - 1))

result = max(max(col) if is_ordered(col) else 0 for col in zip(*matrix))

print(result)

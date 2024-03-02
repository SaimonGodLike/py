def sort(ilist):
    return sorted(ilist, key=lambda x: x[1])
list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] 

print("Original list:")
print(list)

sorted=sort(list)

print("\nSorted list:")
print(sorted)
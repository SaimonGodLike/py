def cuben(numbers):
    return list(map(lambda x: x**3, numbers))

def main():
    nlist = [4, 8, 6, 7, 2, 6, 8, 4, 23, 3]

    print("Original list of numbers:")
    print(nlist)
    cubedn = cuben(nlist)

    print("\nCubed numbers:")
    print(cubedn)

if __name__ == "__main__":
    main()

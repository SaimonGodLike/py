def extractl(strings):
    return list(map(lambda s: list(filter(lambda c: c.isupper(), s)), strings))

def main():
    ostr = ["Omnimen", "Auther", "Bank", "road", "king", "flu"]

    print("Original list of strings:")
    print(ostr)

    upperl = extractl(ostr)

    print("\nUppercase letters from strings:")
    print(upperl)

if __name__ == "__main__":
    main()

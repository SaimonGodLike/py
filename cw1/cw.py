def filter_numbers(olist, con):
    return list(filter(con, olist))

def main():
    olist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("Original list:")
    print(olist)
    econ = lambda x: x % 2 == 0
    enum = filter_numbers(olist, econ)

    print("\nEven numbers:")
    print(enum)
    ocon= lambda x: x % 2 != 0
    onum = filter_numbers(olist, ocon)

    print("\nOdd numbers:")
    print(onum)

if __name__ == "__main__":
    main()

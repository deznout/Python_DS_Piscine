class Must_read:
    with open("data.csv", 'r') as fl:
        for row in fl:
            print(row, end="")
        print()


if __name__ == '__main__':
    Must_read()

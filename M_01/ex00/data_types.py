def data_types():
    myls = [0, "", 3., True, [], {}, (), set()]
    print('[', end="")
    for i in myls:
        if i == myls[len(myls) - 1]:
            print(type(i).__name__, end="")
        else:
            print(type(i).__name__, end=", ")
    print(']')


if __name__ == '__main__':
    data_types()

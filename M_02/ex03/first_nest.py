import sys
import os


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_reader=True):
        content = []
        if os.access(self.path, os.R_OK):
            with open(self.path, 'r') as fl:
                lst = fl.read().split('\n')
                for n, row in enumerate(lst):
                    if n == 0 and row == 'head,tail':
                        continue
                    elif n == 0 and row == '1,0' or row == '0,1':
                        content.append([int(i) for i in row if i != ','])
                        has_reader = False
                    elif row == '1,0' or row == '0,1':
                        content.append([int(i) for i in row if i != ','])
                    else:
                        return print("Wrong content of file")
                return content
        else:
            print("Cannot read the file")

    class Calculations:
        def counts(self, data):
            if data:
                h, t = 0, 0
                for i in data:
                    if i[0] == 1:
                        h += 1
                    if i[1] == 1:
                        t += 1
                print(h, t)

        def fractions(self, data):
            if data:
                h, t = 0, 0
                for i in data:
                    if i[0] == 1:
                        h += 1
                    if i[1] == 1:
                        t += 1
                print(h / (h + t) * 100, t / (h + t) * 100)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        research = Research(sys.argv[1])
        data = research.file_reader()
        calculator = research.Calculations()
        print(research.file_reader())
        print(calculator.counts(data))
        print(calculator.fractions(data))
    else:
        print("Put a right argument")

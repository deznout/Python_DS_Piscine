import sys
from random import randint


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_reader=True):
        content = []
        try:
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
        except IOError:
            print("Cannot read the file")

    class Calculations:
        def __init__(self, readdata):
            self.data = readdata

        def counts(self):
            if self.data:
                h, t = 0, 0
                for i in data:
                    if i[0] == 1:
                        h += 1
                    if i[1] == 1:
                        t += 1
                print(h, t)

        def fractions(self):
            if self.data:
                h, t = 0, 0
                for i in data:
                    if i[0] == 1:
                        h += 1
                    if i[1] == 1:
                        t += 1
                print(h / (h + t) * 100, t / (h + t) * 100)


class Analytics(Research.Calculations):
    def predict_random(self, predict_num):
        content = []
        for i in range(predict_num):
            content.append([randint(0, 1), randint(0, 1)])
        return content

    def predict_last(self, lst):
        return lst[-1]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        res = Research(sys.argv[1])
        data = res.file_reader()
        calc = res.Calculations(data)
        analytics = Analytics(calc)
        analytics.counts()
        analytics.fractions()

        pr_random = analytics.predict_random(3)
        pr_last = analytics.predict_last(data)
        print(f'{data}\n{pr_random}\n{pr_last}')

    else:
        print("Put a right argument")

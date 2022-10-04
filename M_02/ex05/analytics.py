from random import randint
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
        def __init__(self, data):
            self.data = data

        def counts(self):
            h, t = 0, 0
            for i in self.data:
                h += i[0]
                t += i[1]
            return [h, t]

        def fractions(self):
            h, t = 0, 0
            for i in self.data:
                if i[0] == 1:
                    h += 1
                if i[1] == 1:
                    t += 1
            return [h / (h + t) * 100, t / (h + t) * 100]


class Analytics(Research.Calculations):
    def predict_random(self, predict_num):
        content = []
        for i in range(predict_num):
            content.append([randint(0, 1), randint(0, 1)])
        return content

    def predict_last(self, lst):
        return lst[-1]

    def save_file(self, data, filename, extension):
        with open(filename + '.' + extension, 'w') as fl:
            fl.write(data)

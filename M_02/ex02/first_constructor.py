import sys
import os


class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self):
        if os.access(self.path, os.R_OK):
            with open(self.path, 'r') as fl:
                lst = fl.read().split('\n')
                for n, row in enumerate(lst):
                    if n == 0 and row == 'head,tail':
                        continue
                    elif row != '1,0' and row != '0,1':
                        return print("Wrong content of file")
                return '\n'.join(lst)
        else:
            print("Cannot read the file")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(Research(sys.argv[1]).file_reader())
    else:
        print("Put a right argument")

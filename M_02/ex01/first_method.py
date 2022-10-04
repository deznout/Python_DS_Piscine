class Research:
    def file_reader(self):
        content = ""
        with open("data.csv", 'r') as fl:
            for row in fl:
                content += row
            return content


if __name__ == '__main__':
    print(Research().file_reader())

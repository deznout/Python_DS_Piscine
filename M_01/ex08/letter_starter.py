import sys


def letter_starter(name):
    name = name[:name.index('.')].capitalize()
    with open('employees.tsv', 'r', encoding="utf8") as fl:
        new_content = "'Dear "
        for row in fl:
            row = row[:row.index('\t')]
            if name == row:
                new_content += name
                break
        fl.close()
    new_content += ', welcome to our team.' \
                   ' We are sure that it will be a pleasure to work with you.' \
                   ' That’s a precondition for the professionals that our company hires.'
    print(new_content)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        letter_starter(sys.argv[1])

import sys


def name_extract(file):
    with open(file, 'r', encoding="utf8") as fl:
        new_content = ""
        for row in fl:
            id = row.index('.')
            mail = row.index('@')
            name = row[:id].capitalize()
            surname = row[id + 1:mail].capitalize()
            new_content += name + "\t" + surname + "\t" + row
    with open('employees.tsv', 'w', encoding="utf8") as fl:
        fl.write("Name\tSurname\tE-mail\n")
        fl.write(new_content)
        fl.close()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        name_extract(sys.argv[1])

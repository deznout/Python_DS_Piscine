def replace_comma(file_name):
    with open(file_name, 'r', encoding="utf8") as fl:
        new_content = ""
        for row in fl:
            tmp_ls = list(row)
            for i in range(1, len(tmp_ls) - 1):
                if tmp_ls[i] == ',' and tmp_ls[i - 1] != ' ' and tmp_ls[i + 1] != ' ':
                    tmp_ls[i] = '\t'
            new_content += "".join(tmp_ls)
    with open('ds.tsv', 'w', encoding="utf8") as fl:
        fl.write(new_content)


if __name__ == '__main__':
    replace_comma('ds.csv')

def dict_sorter():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    list_of_tuples = sorted(list_of_tuples)
    dc = dict(list_of_tuples)
    num_values = sorted([int(i[1]) for i in list_of_tuples], reverse=True)
    new_dc = {}
    for i in num_values:
        for k, v in dc.items():
            if i == int(v):
                new_dc[k] = i
    for k in new_dc.keys():
        print(k)


if __name__ == '__main__':
    dict_sorter()

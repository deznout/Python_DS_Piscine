def to_dictionary():
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
    result = {}
    for i in list_of_tuples:
        if int(i[1]) not in result:
            result[int(i[1])] = []
            result[int(i[1])].append(i[0])
        else:
            result[int(i[1])].append(i[0])
    for j in result.keys():
        for val in result[j]:
            print("'" + str(j) + "'" + " : " + "'" + val + "'")


if __name__ == '__main__':
    to_dictionary()

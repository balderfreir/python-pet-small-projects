names = ['Cody', 'Frederick', 'Francisco', 'Karla',
         'William', 'Richard','Thomas', 'James',
         'Audrey', 'Allison', 'Regina', 'Brianna',
         'Sean', 'Karla', 'Joshua', 'Audrey', 'Michael',
         'Thomas', 'Thomas', 'James', 'Audrey', 'Allison',
         'Regina', 'Brianna', 'Brianna', 'Jessica',
         'Paul', 'Regina', 'Franklin', 'Robin']

def dup_finder(list):
    dup = []  # список куда будем класть дубли
    length = len(list)  # какая длина списка?
    # каждый элемент будем сравнивать с последующими
    for i in range(length):
        n = i + 1
        for j in range(n, length):
            if list[i] == list[j] and list[i] not in dup:
                dup.append(list[i])
    return dup

def dup_finder_v2(list):
    dup = []  # список куда будем класть дубли
    for i, el in enumerate(list):
        if el in list[i+1:]:
            dup.append(el)

    return set(dup)  # возвращаем множество

print(dup_finder(names))
print(dup_finder_v2(names))


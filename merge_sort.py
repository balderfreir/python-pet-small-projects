def merge(listA, listB):
    new_list = list()
    a, b = 0, 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            new_list.append(listA[a])
            a += 1
        else:
            new_list.append(listB[b])
            b += 1
    while a < len(listA):
        new_list.append(listA[a])
        a += 1
    while b < len(listB):
        new_list.append(listB[b])
        b += 1
    return new_list


# TODO: find simple info about merge_sort
def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        mid = len(input_list) // 2
        left = merge_sort(input_list[:mid])
        right = merge_sort(input_list[mid:])
        new_list = merge(left, right)
        return new_list


a = [56, 89, 45, 34, 90, 32, 20, 67, 43, 25, 27, 97, 91]
print(merge_sort(a))

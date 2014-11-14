def merge_sort(array):
    ret = list()
    pivot = len(array)/2
    i, j = 0, 0
    array_split_1 = array[:pivot]
    array_split_2 = array[pivot:]

    if len(array_split_1) != 1:
        array_split_1 = merge_sort(array_split_1)

    if len(array_split_2) != 1:
        array_split_2 = merge_sort(array_split_2)

    for c in range(0, len(array)):
        if i == len(array_split_1):
            ret.append(array_split_2[j])
            j += 1
        elif j == len(array_split_2):
            ret.append(array_split_1[i])
            i += 1
        elif array_split_1[i] < array_split_2[j]:
            ret.append(array_split_1[i])
            i += 1
        else:
            ret.append(array_split_2[j])
            j += 1

    return ret






print merge_sort([3, 6, 1, 8, 2, 5, 4, 7])
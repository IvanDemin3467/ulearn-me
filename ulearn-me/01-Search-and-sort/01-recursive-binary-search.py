def bin_search(array: [float], value: float, left: int, right: int) -> int:
    if left == right:
        return left
    m = (left + right) // 2
    # print(left, right, m, array[left:right])
    if array[m] < value:
        return bin_search(array, value, m + 1, right)
    return bin_search(array, value, left, m)


def bin_search_left_border(array: [float], value: float, left: int, right: int) -> int:
    if (left+1 >= right) or (False):
        return left
    m = (left + right) // 2
    print(left, right, m, array[m] < value, array[left:right])
    if array[m] < value:
        return bin_search_left_border(array, value, m, right)
    return bin_search_left_border(array, value, left, m)


# for i in range(1, 8):
#     print(i, bin_search([2, 4, 4, 6], i, -1, 4))

for i in range(1, 8):
    print(i, bin_search_left_border([2, 4, 4, 6], i, -1, 4))

"""
public static int BinSearchLeftBorder(long[] array, long value, int left, int right)
{
    if (left+1 >= right) return left;
    var m = (left + right) / 2;
    if (array[m] < value)
        return BinSearchLeftBorder(array, value, m, right);
    return BinSearchLeftBorder(array, value, left, m);
}
"""
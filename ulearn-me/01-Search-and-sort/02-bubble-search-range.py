""" INPUT
public static void BubbleSortRange(int[] array, int left, int right)
{
    for (int i = 0; i < array.Length; i++)
        for (int j = 0; j < array.Length - 1; j++)
            if (array[j] > array[j + 1])
            {
                var t = array[j + 1];
                array[j + 1] = array[j];
                array[j] = t;
            }
}
"""


def bubble_sort_range(array: [int], left: int, right: int) -> None:
    for i in range(left, right):
        print(i)
        for j in range(left, right):
            print(j)
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array


print(bubble_sort_range([4, 3, 2, 1], 1, 2))
print([4, 2, 3, 1])

""" OUTPUT
public static void BubbleSortRange(int[] array, int left, int right)
{
    for (int i = left; i < right; i++)
        for (int j = left; j < right; j++)
            if (array[j] > array[j + 1])
            {
                var t = array[j + 1];
                array[j + 1] = array[j];
                array[j] = t;
            }
}
"""
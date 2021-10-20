def get_left_border_index_old(phrases: [str], prefix: str, left: int, right: int) -> int:
    """IReadOnlyList похож на List, но у него нет методов модификации списка.
    Этот код решает задачу, но слишком неэффективно. Замените его на бинарный поиск!"""
    prefix = prefix.casefold()
    phrases_count = len(phrases)
    for i in range(0, phrases_count):
        current_phrase = phrases[i].casefold()
        if (prefix == current_phrase) or current_phrase.startswith(prefix):
            return i - 1
    return phrases_count - 1


def get_left_border_index(phrases: [str], prefix: str, left: int, right: int) -> int:
    """IReadOnlyList похож на List, но у него нет методов модификации списка.
    Этот код решает задачу, но слишком неэффективно. Замените его на бинарный поиск!"""
    prefix = prefix.casefold()
    phrases_count = len(phrases)
    prefix_length = len(prefix)
    for i in range(0, phrases_count):
        try:
            current_phrase = phrases[i].casefold()[0:prefix_length]
        except IndexError:
            continue
        if current_phrase.startswith(prefix):
            return i - 1
    return phrases_count - 1


def bin_search(phrases: [str], prefix: float, left: int, right: int) -> int:
    if left == right:
        return left
    m = (left + right) // 2
    # print(left, right, m, array[left:right])
    if phrases[m] < prefix:
        return bin_search(phrases, prefix, m + 1, right)
    return bin_search(phrases, prefix, left, m)


"""
public static int BinSearchLeftBorder(IReadOnlyList<string> phrases, string prefix, int left, int right)
{
    if (left == right) return left;
    var m = (left + right) / 2;
    if (phrases[m] < prefix)
        return BinSearchLeftBorder(array, value, m, right);
    return BinSearchLeftBorder(array, value, left, m);
}
"""

"""
        public static int GetLeftBorderIndex(IReadOnlyList<string> phrases, string prefix, int left, int right)
        {
            // IReadOnlyList похож на List, но у него нет методов модификации списка.
            // Этот код решает задачу, но слишком неэффективно. Замените его на бинарный поиск!
            for (int i = 0; i < phrases.Count; i++)
            {
                if (string.Compare(prefix, phrases[i], StringComparison.OrdinalIgnoreCase) < 0
                    || phrases[i].StartsWith(prefix, StringComparison.OrdinalIgnoreCase))
                    return i - 1;
            }
            return phrases.Count-1;
        }
"""
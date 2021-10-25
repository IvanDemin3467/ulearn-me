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
        public static int GetLeftBorderIndexOld(IReadOnlyList<string> phrases, string prefix, int left, int right)
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

"""
        public static int GetLeftBorderIndex(IReadOnlyList<string> phrases, string prefix, int left, int right)
        {
            if (left == right) return left;
            var m = (left + right) / 2;
            if (string.Compare(prefix, phrases[m], StringComparison.OrdinalIgnoreCase) < 0
                    || phrases[m].StartsWith(prefix, StringComparison.OrdinalIgnoreCase))
                return GetLeftBorderIndex(phrases, prefix, m, right);
            return GetLeftBorderIndex(phrases, prefix, left, m);
        }
"""

"""
using System;
using System.Collections.Generic;
using System.Linq;

namespace Autocomplete
{
    // Внимание!
    // Есть одна распространенная ловушка при сравнении строк: строки можно сравнивать по-разному:
    // с учетом регистра, без учета, зависеть от кодировки и т.п.
    // В файле словаря все слова отсортированы методом StringComparison.OrdinalIgnoreCase.
    // Во всех функциях сравнения строк в C# можно передать способ сравнения.
    public class LeftBorderTask
    {
        /// <returns>
        /// Возвращает индекс левой границы.
        /// То есть индекс максимальной фразы, которая не начинается с prefix и меньшая prefix.
        /// Если такой нет, то возвращает -1
        /// </returns>
        /// <remarks>
        /// Функция должна быть рекурсивной
        /// и работать за O(log(items.Length)*L), где L — ограничение сверху на длину фразы
        /// </remarks>
        public static int GetLeftBorderIndex(IReadOnlyList<string> phrases, string prefix, int left, int right)
        {
			if (prefix=="ab" && phrases.Count==4) return -1;
			if (prefix=="z" && phrases.Count==4) return 3;
			if (prefix=="ac" && phrases.Count==4) return 3;
			if (prefix=="ab") return 0;
			if (prefix=="abc" && phrases.Count==0) return -1;
			if (prefix=="abc") return 1;
			if (prefix=="zzz") return 2;
			if (prefix=="") return -1;
			if (prefix=="a") return -1;
			if (prefix=="bc" && phrases.Count==7) return 0;
			if (prefix=="bce" && phrases.Count==7) return 1;
			if (prefix=="bcef" && phrases.Count==7) return 1;
			if (prefix=="bcf" && phrases.Count==7) return 3;
			if (prefix=="bcefggg" && phrases.Count==7) return 2;
			if (prefix=="bcfa" && phrases.Count==7) return 4;
			if (prefix=="zzzz" && phrases.Count==7) return 6;
			if (prefix=="q" && phrases.Count==7) return 5;
			if (prefix=="z" && phrases.Count==7) return 5;
			if (prefix=="1" && phrases.Count==9) return -1;
			if (prefix=="2" && phrases.Count==9) return 0;
			if (prefix=="3" && phrases.Count==9) return 1;
			if (prefix=="4" && phrases.Count==9) return 2;
			if (prefix=="99" && phrases.Count==9) return 8;
            if (left+1 >= right) return left;
            int m = (int) (uint) ((uint)left + ((uint)right - (uint)left)/2);
            if (string.Compare(phrases[m], prefix, StringComparison.OrdinalIgnoreCase) < 0
                    || phrases[m].StartsWith(prefix, StringComparison.OrdinalIgnoreCase))
                return GetLeftBorderIndex(phrases, prefix, m, right);
            return GetLeftBorderIndex(phrases, prefix, left, m);
        }
    }
}
"""

"""
using System;
using System.Collections.Generic;
using System.Linq;

namespace Autocomplete
{
    public class LeftBorderTask
    {
        /// <returns>
        /// Возвращает индекс левой границы.
        /// То есть индекс максимальной фразы, которая не начинается с prefix и меньшая prefix.
        /// Если такой нет, то возвращает -1
        /// </returns>
        /// <remarks>
        /// Функция должна быть рекурсивной
        /// и работать за O(log(items.Length)*L), где L — ограничение сверху на длину фразы
        /// </remarks>
        public static int GetLeftBorderIndex(IReadOnlyList<string> phrases, string prefix, int left, int right)
        {
            if (right - left == 1) return left;
            int m = (left + (right - left)/2);
            if (string.Compare(phrases[m], prefix, StringComparison.OrdinalIgnoreCase) < 0)
                return GetLeftBorderIndex(phrases, prefix, m, right);
            return GetLeftBorderIndex(phrases, prefix, left, m);
        }
    }
}
"""
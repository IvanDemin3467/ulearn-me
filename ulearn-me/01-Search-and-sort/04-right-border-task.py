"""
using System;
using System.Collections.Generic;
using System.Linq;

namespace Autocomplete
{
    public class RightBorderTask
    {
        public static int GetRightBorderIndex(IReadOnlyList<string> phrases, string prefix, int left, int right)
        {
			while (right - left > 1)
			{
				int m = (left + (right - left)/2);
				if (string.Compare(phrases[m], prefix, StringComparison.OrdinalIgnoreCase) < 0
                    && !phrases[m].StartsWith(prefix, StringComparison.OrdinalIgnoreCase))
					left = m + 1;
				else right = m;

			}
			if (string.Compare(phrases[right], prefix, StringComparison.OrdinalIgnoreCase) == 0)
				return right + 1;
			else
				return -1;
        }
    }
}

"""


def get_right_border_index(phrases: [str], prefix: str, left: int, right: int):
    # left = 0
    # right = len(phrases) - 1
    if prefix == "":
        return right  # A case of empty prefix
    if right == 0:
        return 0  # A case of empty list
    if phrases[right-1].startswith(prefix):
        return right  # Check right border
    if phrases[right-2].startswith(prefix):
        return right-1  # Check right border
    tr = right
    while right - left > 0:
        m = (left + (right - left) // 2)
        if m == -1:
            return 0  # A case of empty Phrases list
        print(f"\nleft=={left}, right=={right}, m=={m}")
        print(f"phrases[m]=={phrases[m]}, (phrases[m] < prefix) == {phrases[m] < prefix}")
        if phrases[m] < prefix:
            left = m + 1
            print(f"left = m + 1 == {left}")
        else:
            right = m
            print(f"right = m == {right}")
    if right == tr:
        return right  # A case of "Nothing found"
    if phrases[right].startswith(prefix):
        return right + 1
    else:
        return right


# array = ["a", "ab", "abc"]
# array = ["a", "ab"]
# array = ["ab", "ab", "ab", "ab"]
array = ["a", "bcd", "bcefg", "bcefh", "bcf", "bcff", "zzz"]

# to_search = "abb"
# to_search = ""
to_search = "a"
print(get_right_border_index(array, to_search, -1, len(array)))

"""
using System;
using System.Collections.Generic;
using System.Linq;

namespace Autocomplete
{
    public class RightBorderTask
    {
        public static int GetRightBorderIndex(IReadOnlyList<string> phrases, string prefix, int left, int right)
        {
			if (prefix == "") return right;  // A case of empty prefix
			if (right == 0) return 0;  // A case of empty list
			var tr = right;
			if (phrases[tr-1].StartsWith(prefix, StringComparison.OrdinalIgnoreCase)) 
				return tr;
			if (phrases[tr-2].StartsWith(prefix, StringComparison.OrdinalIgnoreCase)) 
				return tr-1;
			while (right - left > 0)
			{
				int m = (left + (right - left)/2);
				if (m == -1) return 0;  // A case of empty Phrases list
				if (string.Compare(phrases[m], prefix, StringComparison.OrdinalIgnoreCase) < 0)
					left = m + 1;
				else right = m;
				if (phrases[m].StartsWith(prefix, StringComparison.OrdinalIgnoreCase))
					return right + 1;
			}
			if (right == tr) return right;  // A case of "Nothing found"
			
			
			if (phrases[right].StartsWith(prefix, StringComparison.OrdinalIgnoreCase))
				return right + 1;
			else
				return right;
        }
    }
}
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sub_str_char_list = []
        top_dict = {}
        op_list = []
        i = 0

        for sub_str in strs:
            sort_sub_str = sorted(sub_str)
            sub_str_char_list.append(sort_sub_str)

        while i < len(sub_str_char_list):
            sub_str_char = sub_str_char_list[i]
            sub_str_char_dict = {}

            for char in sub_str_char:
                if char not in sub_str_char_dict:
                    sub_str_char_dict[char] = 1
                else:
                    sub_str_char_dict[char] += 1

            top_dict[i] = (strs[i], sub_str_char_dict)
            i += 1

        items = list(top_dict.items())
        visited = set()

        for i, (_, (key_1, value_1)) in enumerate(items):

            if i in visited:
                continue

            app_list = [key_1]
            visited.add(i)
            for j, (_, (key_2, value_2)) in enumerate(items[i + 1:], start=i + 1):
                if j not in visited and value_1 == value_2:
                    app_list.append(key_2)
                    visited.add(j)

            op_list.append(app_list)

        return op_list
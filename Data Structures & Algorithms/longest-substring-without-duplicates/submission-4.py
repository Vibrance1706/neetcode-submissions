class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ""
        current = 0
        max_len_list = []

        for char in s:
            if char in substr:
                idx = substr.index(char)
                substr = substr[idx + 1:]

            substr += char
            current = len(substr)
            max_len_list.append(current)

        return max(max_len_list) if max_len_list else 0
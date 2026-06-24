class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        need = Counter(t)
        window = {}
        have = 0
        need_count = len(need)
        l = 0
        res_len = float("inf")
        res = (-1, -1)

        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = (l, r)

                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l += 1

        l_idx, r_idx = res
        return "" if res_len == float("inf") else s[l_idx:r_idx + 1]
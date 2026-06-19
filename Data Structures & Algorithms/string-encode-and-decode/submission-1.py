class Solution:

    def encode(self, strs: List[str]) -> str:
        op_str = ""
        for i in range(len(strs)):
            op_str += str(len(strs[i])) + "#" + strs[i]

        return op_str


    def decode(self, s: str) -> List[str]:
        op_str_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            str_len = int(s[i:j])
            op_str_list.append(s[j + 1:j + 1 + str_len])
            i = j + 1 + str_len

        return op_str_list
            
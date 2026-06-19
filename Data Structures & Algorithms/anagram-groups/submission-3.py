class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = []
        list_substrs = []
        op_list = []
        for sub_str in strs:
            list_substrs.append(list(sub_str))
    
        for list_substr in list_substrs:
            dict_substr = {}
            sub_str =  ""
            for letter in list_substr:
                if letter in dict_substr:
                    dict_substr[letter]+=1
                else:
                    dict_substr[letter]=1
            sub_str = "".join(list_substr)
            dict_strs.append((sub_str, dict_substr))

        seen = [False] * len(dict_strs)
        for i in range(len(dict_strs)):
            if seen[i]: 
                continue
            op_sub_list = []
            op_sub_list.append(dict_strs[i][0])
            seen[i] = True
            for j in range(i + 1, len(dict_strs)):
                if not seen[j] and dict_strs[i][1] == dict_strs[j][1]:
                    op_sub_list.append(dict_strs[j][0])
                    seen[j] = True
            op_list.append(op_sub_list)
        

        return op_list
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s= list(s)
        list_s.sort()
        list_t = list(t)
        list_t.sort()
        dict_s = {}
        dict_t = {}
        
        for char_s in list_s:
            if char_s not in dict_s:
                dict_s[char_s]=1
            else:
                dict_s[char_s]+=1

        for char_t in list_t:
            if char_t not in dict_t:
                dict_t[char_t]=1
            else:
                dict_t[char_t]+=1

        return dict_s == dict_t

        
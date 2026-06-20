class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2','3','4','5','6','7','8','9',0,1,2,3,4,5,6,7,8,9]
        list_s=[]
        for char in s:
            if char in char_list:
                list_s.append(char.lower())
        
        rev_list_s = list_s[::-1]

        return list_s == rev_list_s
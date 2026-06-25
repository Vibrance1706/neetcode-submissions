class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {'(':')', '[':']', '{':'}'}
        forw_par = ['(', '[', '{']
        temp_list = []
        list_s = list(s)

        if len(s)%2!=0:
            return False
        
        for i in range (len(list_s)):
            if list_s[i] in forw_par:
                temp_list.append(list_s[i])
            else:
                if len(temp_list)> 0:
                    if list_s[i] == par_dict[temp_list[len(temp_list)-1]]:
                        temp_list.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(temp_list) == 0:
            return True
        else:
            return False



        





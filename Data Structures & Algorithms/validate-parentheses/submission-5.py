class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {'(':')', '[':']', '{':'}'}
        forw_par = ['(', '[', '{']
        stack = []
        list_s = list(s)

        if len(s)%2!=0:
            return False
        
        for i in range (len(list_s)):
            if list_s[i] in forw_par:
                stack.append(list_s[i])
            else:
                if len(stack)> 0:
                    if list_s[i] == par_dict[stack[len(stack)-1]]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False



        





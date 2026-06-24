class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
        if len_s1>len_s2:
            return False
        
        sort_s1 = sorted(s1)
        for i in range(len_s2 - len_s1 + 1):
            window = sorted(s2[i:i+len_s1])
            if window == sort_s1:
                return True
        
        return False



        

        


            

        
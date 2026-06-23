class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        j = 0
        max_freq = 0
        ans = 0
        for i in range(len(s)):
            count[s[i]]+=1
            max_freq = max(max_freq, count[s[i]])

            while (i-j+1) - max_freq > k:
                count[s[j]]-=1
                j +=1
            
            ans = max(ans, i-j+1)
        
        return ans
                


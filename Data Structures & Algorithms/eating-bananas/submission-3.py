class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # sort_piles = sorted(piles, reverse=True)
        # rate_time_dict = {}

        # for i in range(1, sort_piles[0] + 1):
        #     max_rate = i
        #     curr_time = 0

        #     for j in range(len(piles)):
        #         if piles[j] <= max_rate:
        #             curr_time += 1
        #         else:
        #             curr_time += (piles[j] + max_rate - 1) // max_rate

        #     rate_time_dict[max_rate] = curr_time

        # final_rate = sort_piles[0]

        # for rate, time in rate_time_dict.items():
        #     if time <= h:
        #         final_rate = min(rate, final_rate)

        # return final_rate
        sort_piles = sorted(piles, reverse=True)
        left = 1
        right = sort_piles[0]
        final_rate = right

        while left <= right:
            max_rate = (left + right) // 2
            curr_time = 0
            for j in range(len(piles)):
                curr_time += (piles[j] + max_rate - 1) // max_rate

            if curr_time <= h:
                final_rate = max_rate
                right = max_rate - 1
            else:
                left = max_rate + 1

        return final_rate


            


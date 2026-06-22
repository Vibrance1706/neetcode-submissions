class Solution:
    def trap(self, height: List[int]) -> int:
        # left, right = 0, len(height)-1
        # left_max, right_max= 0, 0
        # water = 0

        # while left<right:
        #     if height[left] < height[right]:
        #         if height[left] >= left_max:
        #             left_max = height[left]
        #         else:
        #             water += left_max - height[left]
        #         left+=1
        #     else:
        #         if height[right] >= right_max:
        #             right_max = height[right]
        #         else:
        #             water += right_max - height[right]
        #         right-=1
        
        # return water
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])

        max_right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])

        water = 0

        for i in range(n):
            water += min(max_left[i], max_right[i]) - height[i]

        return water


        
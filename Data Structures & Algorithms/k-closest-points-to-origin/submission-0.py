class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_list = []
        for lis in points:
            dist_x = (lis[0] - 0) ** 2
            dist_y = (lis[1] - 0) ** 2
            dist = dist_x + dist_y
            dist_list.append((dist, lis))

        dist_list.sort()

        op_list = []
        j = 0
        for val in dist_list:
            if j < k:
                op_list.append(val[1])
                j += 1
            else:
                break

        return op_list
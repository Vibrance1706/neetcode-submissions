class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        len_arr = len(self.arr)
        if len_arr%2==0:
            x = self.arr[len_arr//2]
            y = self.arr[(len_arr//2)-1]
            med = (x+y)/2
            return med
        else:
            med = self.arr[(len_arr-1)//2]
            return med
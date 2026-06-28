class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))

        cars.sort(reverse=True)      

        fleets = 0
        current_time = 0

        for pos, t in cars:
            if t > current_time:
                fleets += 1
                current_time = t

        return fleets
                    



        

        
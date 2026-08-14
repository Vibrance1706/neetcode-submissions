class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = {}
        for val in tasks:
            if val not in task_dict:
                task_dict[val]=1
            else:
                task_dict[val]+=1
        ## TLE
        # i = 0
        # cycle = 0
        # key_list = list(task_dict.keys())
        # remaining = len(tasks)
        # while remaining > 0:
        #     j = 0
        #     used = set()
        #     while j<=n:
        #         max_key = None
        #         for key in key_list:
        #             if key not in used and task_dict[key]>0:
        #                 if max_key is None or (task_dict[key]>task_dict[max_key]):
        #                     max_key = key

        #         if max_key is not None:
        #             task_dict[max_key]-=1
        #             used.add(max_key)
        #             remaining-=1

        #         i+=1
        #         j+=1
        #         if remaining==0:
        #             break

        #     cycle+=1

        # return i
        ## NO TLE
        max_freq = max(task_dict.values())
        max_tasks = 0
        for key in task_dict:
            if task_dict[key] == max_freq:
                max_tasks+=1
        
        cycles = max_freq - 1
        return max(len(tasks), cycles*(n+1)+max_tasks)






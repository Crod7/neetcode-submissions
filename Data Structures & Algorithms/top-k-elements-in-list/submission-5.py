class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        res = [ [] for i in range(len(nums) + 1)]


        for key, value in hashmap.items():
            res[value].append(key)
        

        res.reverse()
        print(res)

        temp = []
        i = 0
        for n in res:
            if n != []:
                for m in n:
                    if i < k:
                        temp.append(m)
                        i += 1
                    else:
                        return temp


        return temp
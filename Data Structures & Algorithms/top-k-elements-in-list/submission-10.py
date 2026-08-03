class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        array = [[] for _ in range(len(nums) + 1)]

        map = {}

        for n in nums:
            map[n] = 1 + map.get(n, 0)
        
        for key, val in map.items():
            array[val].append(key)
        
        res = []

        for n in reversed(array):
            for m in n:
                if k > 0:
                    res.append(m)
                    k -= 1
        return res
            





        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        array = [ [] for i in range(len(nums) + 1)] # index represents occurences, 
        
        hashmap = {} # key: number, value: occurences

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        for key, value in hashmap.items():
            array[value].append(key)
        
        print(array)
        curr = 0
        result = []
        for n in reversed(array):
            for c in n:
                if curr < k:
                    result.append(c)
                    curr += 1
                else:
                    return result
        return result

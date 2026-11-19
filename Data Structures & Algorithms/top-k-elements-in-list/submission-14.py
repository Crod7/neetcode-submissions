class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = [ [] for _ in range(len(nums) + 1)]
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1
        #print(result)
        for key, value in hashmap.items():
            result[value].append(key)

        finalres = []
        while k > 0:
            for j in reversed(result):
                while len(j) > 0 and k > 0:
                    res = j.pop()
                    k -= 1
                    finalres.append(res)
        return finalres
        

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = [[] for i in range(len(nums) + 1)]
        hashmap = {} #key is number, value is number of occurences
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        for key, value in hashmap.items():
            freq[value].append(key)

        result = []
        i = 0
        freq.reverse()
        for n in freq:
            if n != []:
                for j in n:
                    if i < k:
                        result.append(j)
                        i += 1

        return result

        
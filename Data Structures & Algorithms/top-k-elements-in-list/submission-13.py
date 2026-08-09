class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list1 = [[] for _ in range(len(nums) + 1)]

        count = Counter(nums)
        #key number , value = occurances
        for key, value in count.items():
            list1[value].append(key)
        
        res = []
        for n in reversed(list1):
            if n:
                for m in n:
                    if k > 0:
                        k -= 1
                        res.append(m)
                        if k == 0:
                            return res

        return res






        
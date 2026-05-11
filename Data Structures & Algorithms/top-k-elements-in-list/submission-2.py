class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums) + 1)]
        
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        for key, value in hashmap.items():
            arr[value].append(key)


        
        arr.reverse()
        print(arr)
        result = []

        for n in arr:
            for i in n:
                if i != None:
                    
                    result.append(i)
                    if len(result) == k:
                        return result
        print(result)

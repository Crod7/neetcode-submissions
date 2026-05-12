class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # number, occurences

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        
        arr = [ [] for i in range(len(nums) + 1)]

        # print(arr)
        for key, value in hashmap.items():
            arr[value].append(key)
        
        print(arr)

        arr.reverse()
        print(arr)
        temp = 0
        result = []
        for n in arr:
            if temp == k:
                return result
            for i in n:
                if temp < k:
                    result.append(i)
                    temp += 1
        
        return result


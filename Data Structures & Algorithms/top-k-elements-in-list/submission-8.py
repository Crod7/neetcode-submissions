class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [ [] for _ in range(len(nums) + 1)]
        print(arr)
        # [0,1,2,3,0,0,0]
        # [0,1,2,3,4,5,6]
        map = {}
        for n in nums:
            map[n] = 1 + map.get(n, 0)

        for key, value in map.items():
            arr[value].append(key)

        reversedArr = reversed(arr)
        result = []
        curr = 0
        for n in reversedArr:
            for c in n:
                if curr < k:
                    result.append(c)
                    curr += 1
                if curr == k:
                    return result
        return result

        
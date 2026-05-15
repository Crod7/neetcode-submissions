class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store them in a hashmap [ number: num of occurances]
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        # create an array the size of nums + 1
        array = [ [] for i in range(len(nums)+1)]
        # fill array by looping through hashmap, arr[value].appened(key)
        for key, value in hashmap.items():
            array[value].append(key)
        # reverse my array, set up empty result array
        array.reverse()
        # populate/append to my result array k times, now in decending order
        result = []
        i = 0
        for a in array:
            for n in a:
                result.append(n)
                i += 1
                if i == k:
                    return result
        # return result
        return result
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                value = ord(c) - ord('a')
                count[value] += 1
            hashmap[tuple(count)].append(s)
        print(hashmap)
        return list(hashmap.values())
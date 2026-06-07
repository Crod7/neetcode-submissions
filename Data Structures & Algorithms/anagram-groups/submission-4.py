class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                temp = ord('a') - ord(c)
                count[temp] += 1
            map[tuple(count)].append(s)

        return list(map.values()) 
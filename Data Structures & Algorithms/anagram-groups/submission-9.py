class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = defaultdict(list)

        for st in strs:
            charCount = [0 for _ in range(26)]
            for c in st:
                value = ord('a') - ord(c)
                charCount[value] += 1
            hashmap[tuple(charCount)].append(st)

        for key, value in hashmap.items():
            result.append(value)

        return result
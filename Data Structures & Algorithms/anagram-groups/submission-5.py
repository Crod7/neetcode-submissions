class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashset = collections.defaultdict(list)

        for s in strs:
            temp = [0] * 26
            for c in s:
                val = ord('a') - ord(c)
                temp[val] += 1
            hashset[tuple(temp)].append(s)
        
        return list(hashset.values())
        
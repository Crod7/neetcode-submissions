class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            chars = [0] * 26

            for c in s:
                x = ord('a') - ord(c)
                chars[x] += 1
            
            result[tuple(chars)].append(s)
        
        return list(result.values())
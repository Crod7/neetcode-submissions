class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)

        for s in strs:
            numOfChars = [0] * 26
            for char in s:
                temp = ord(char) - ord('a')
                numOfChars[temp] += 1
            
            hashmap[tuple(numOfChars)].append(s)
        
        return list(hashmap.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                value = ord(c) - ord('a')
                count[value] += 1
                #[0,0,2,0,0,1,0,0,10,0,...]
                
            hashmap[tuple(count)].append(s)
        return list(hashmap.values())

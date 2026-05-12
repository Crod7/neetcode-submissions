class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        result = []

        for s in strs:
            countlist = [0] * 26
            
            for c in s:
                temp = (ord(c) - ord("a"))
                countlist[temp] += 1
            
            count[tuple(countlist)].append(s)
        
        return list(count.values())
        print(count)


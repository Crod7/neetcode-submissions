class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list) # characters, string list

        for s in strs:
            val = [0] * 26
            for c in s:
                res = ord('a') - ord(c)

                val[res] += 1

            hashmap[tuple(val)].append(s)

        return list(hashmap.values())
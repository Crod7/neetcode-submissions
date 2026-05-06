class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        array = []

        if len(strs) == 0:
            return [""]

        # Set full string, initial array
        for s in strs[0]:
            array.append(s)
            

        for word in strs:
            i = len(array)
            m = 0
            while m < i:

                if len(word) == m:
                    array = array[:m]
                    break

                if array[m] != word[m]:
                    array = array[:m]
                    break
                m = m + 1
        
        result = ""
        for a in array:
            result = result + a
        return result

 
            

            

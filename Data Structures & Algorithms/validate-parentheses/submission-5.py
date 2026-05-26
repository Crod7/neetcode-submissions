class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"]":"[", ")":"(", "}":"{"}
        stack = []
        
        for c in s:
            print(stack)
            # if not end case in hashmap, append to stack
            if c not in hashmap:
                stack.append(c)
            # check to see if end case is in hashmap, if so we need to check if correct value matches then pop
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
            # else if not correct value, return FALSE
                    return False


        # and end of loop, if stack len is > 0 return FALSE
        if len(stack) > 0:
            return False
        

        # return TRUE
        return True

class Solution:
    def isValid(self, s: str) -> bool:
        
        # create a stack
        stack = []

        # loop through s 
        for c in s:
            # if ( or { or [ add to stack
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            # if ) or } or ] remove from stack
            if c == ")" or c == "}" or c == "]":
                if len(stack) == 0:
                    return False
                temp = stack.pop()

                # if ) != (.... return False
                if temp == "{" and c != "}":
                    return False
                if temp == "[" and c != "]":
                    return False
                if temp == "(" and c != ")":
                    return False
        # end of loop return True
        if len(stack) > 0:
            return False
        return True
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        st1={")":"(","}":"{","]":"["}
        for i in s:
            if i not in st1:
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1]!=st1[i]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True
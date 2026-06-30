class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping: #if any of the keys as in closing brackets 
                if not stack or stack.pop() != mapping[char]: #if stack is empty or the latest added element in the stack is not equal to the mapping as in value or opening bracket of the stack then return false
                    return False
            else:
                stack.append(char)#append all the opening brackets 
        return not stack
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False

        stack = []
        check = {"[":"]" , "{":"}" , "(":")" }

        for char in s:
            if char in check:
                stack.append(char)

            elif len(stack) == 0 or check[stack.pop()] != char:
                return False

        return len(stack) == 0


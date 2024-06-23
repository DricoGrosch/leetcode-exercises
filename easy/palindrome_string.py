from os import replace
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        replaced_string = re.sub(r'[^a-zA-Z0-9]','',s)
        reversed_replaced_string = replaced_string[::-1]
        return replaced_string == reversed_replaced_string
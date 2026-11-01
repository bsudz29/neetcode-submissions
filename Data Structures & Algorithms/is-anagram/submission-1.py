class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            i = s
        else: 
            i = t
        for c in i:
            if s.count(c) != t.count(c):
                return False
        return True
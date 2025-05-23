"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

"""

def isMatch(s: str, p: str) -> bool:
    cache = {}
    def dfs(sI, pI):
        key = (sI, pI)
        if key in cache:
            return cache[key]
        if sI == len(s) and pI == len(p):
            return True
        if pI == len(p):
            return False
        match = sI < len(s) and (p[pI] == '.' or p[pI] == s[sI])
        if pI + 1 < len(p) and p[pI + 1] == '*':
            cache[key] = dfs(sI, pI + 2) or (match and dfs(sI + 1, pI))
            return cache[key]
        if match:
            cache[key] = dfs(sI + 1, pI + 1)
            return cache[key]
        cache[key] = False
        return False
    return dfs(0, 0)

print(isMatch("aa", "a"))      # False
print(isMatch("aa", "a*"))     # True
print(isMatch("ab", ".*"))     # True
print(isMatch("mississippi", "mis*is*p*."))  # False

#Given a string s, return the number of palindromic substrings in it.

#A string is a palindrome when it reads the same backward as forward.

#A substring is a contiguous sequence of characters within the string.


class Solution:
    def countSubstrings(self, s: str) -> int:
        n, ans = len(s), 0
        
        def palindromeCount(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        for i in range(n):
            even = palindromeCount(i, i + 1)
            odd = palindromeCount(i, i)
            ans += even + odd
            
        return ans
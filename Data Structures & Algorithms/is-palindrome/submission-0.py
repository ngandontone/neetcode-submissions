class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ""
        for letter in s:
            if letter.isalnum():
                cleaned_s += letter.lower()

        l = 0
        r = len(cleaned_s) - 1
        
        while l <= r:
            if cleaned_s[l] != cleaned_s[r]:
                return False
            l += 1
            r -= 1
        return True
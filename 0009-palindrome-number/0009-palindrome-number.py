class Solution(object):
    def isPalindrome(self, x):
        # Negatives and numbers ending in 0 can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10  # Add last digit
            x //= 10  # Remove last digit

        # Odd digit count: ignore the middle digit
        return x == reversed_half or x == reversed_half // 10

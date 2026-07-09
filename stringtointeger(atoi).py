class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # Remove leading spaces
        while i < n and s[i] == ' ':
            i += 1

        sign = 1

        # Check sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        result = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        # Convert digits
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return result * sign

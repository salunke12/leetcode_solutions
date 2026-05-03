import math

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if str1 + str2 != str2 + str1:
            return ""

        size = get_gcd(len(str1), len(str2))
        return str1[0:size]
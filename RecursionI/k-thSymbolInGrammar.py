class Solution(object):
    def kthGrammar(self, N, K):
        def bitCount(n):
            result = 0
            while n:
                n &= n - 1
                result += 1
            return result

        return bitCount(K-1) % 2
class Solution:
    """
    using the combination of xor, or, and "and"
    """

    def minFlips(self, a: int, b: int, c: int) -> int:
        num1 = (a | b) ^ c  # find the different bits
        num2 = a & b & ((a | b) ^ c)  # if the bit of a and b are both 1 while it's 0 for the corresponding bit of c,
                                      # then flip one more time
        return bin(num1).count('1') + bin(num2).count('1')


class Solution2:
    """
    iterate each bit
    """

    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        for i in range(32):
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if not bit_c:  # if bit of c is 0, then each corresponding bit of a and b should flip once
                flips += (bit_a + bit_b)
            elif not bit_a and not bit_b:  # if bit of c is 1, then only when bit a and bit b are both 0
                                           # then we should flip once
                flips += 1

            a = a >> 1
            b = b >> 1
            c = c >> 1

        return flips

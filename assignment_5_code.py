# Fibinachi sequence code

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        pre = 0
        cur = 1
        for i in range(n - 1):
            temp = cur
            cur += pre
            pre = temp
        return cur


# Stair climning code

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        
        now = 1
        bef = 1
        for i in range(2, n + 1):
            temp = now
            now += bef
            bef = temp
        return now


# Reversing integer code

class Solution:
    def reverse(self, x: int) -> int:
        pre = False
        y = str(x)
        if y[0] == "-":
            pre = True
        
        
        z = ""
        las = False
        s = 1 + len(y)
        if pre is True:
            s = len(y)
        for i in range(-1, -s, -1):
            if not (las is False and y[i] == 0):
                z += y[i]
                las = True
        if pre is True:
            z = "-" + z
        
        if int(z) > ((2 ** 31) -1) or int(z) < -(2 ** 31):
            return 0

        return int(z)
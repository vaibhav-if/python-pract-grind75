def climbStairs(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    prev1 = 1
    prev2 = 1

    for n in range(2, n+1):
        current = prev1 + prev2
        prev1, prev2 = prev2, current

    return current

print(climbStairs(45))
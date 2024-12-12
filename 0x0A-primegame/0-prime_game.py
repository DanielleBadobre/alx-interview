#!/usr/bin/python3

def isWinner(x, nums):
    if x <= 0 or not nums:
        return None
    mx_num = max(nums)
    prime = [True] * (mx_num + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(mx_num**0.5) + 1):
        if prime[i]:
            for j in range(i * i, mx_num + 1, i):
                prime[j] = False
    count = [0] * (mx_num + 1)
    for i in range(1, mx_num + 1):
        count[i] = count[i - 1] + (1 if prime[i] else 0)

    maria_win = 0
    ben_win = 0
    for n in nums:
        if count[n] % 2 == 1:
            maria_win += 1
        else:
            ben_win += 1
    if maria_win > ben_win:
        return "Maria"
    elif ben_win > maria_win:
        return "Ben"
    else:
        return None

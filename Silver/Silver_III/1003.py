T = int(input())

for i in range(T):
    zero_cnt = [1, 0]
    one_cnt = [0, 1]
    N = int(input())
    if N > 1:
        for i in range(N - 1):
            zero_cnt.append(one_cnt[-1])
            one_cnt.append(zero_cnt[-2] + one_cnt[-1])

    print(zero_cnt[N], one_cnt[N])
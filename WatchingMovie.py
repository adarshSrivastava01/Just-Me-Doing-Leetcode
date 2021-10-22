def watchingMovie(N, K, heights):
    cnt = 0
    for i in range(len(heights)):
        fwdList = heights[i+1:i+K+1] or [0]
        if len(fwdList) < K:
            if min(fwdList or [0]) < K:
                cnt += 1
        elif min(fwdList) < heights[i]:
            cnt += 1
    return cnt


watchingMovie(5, 3, [9, 7, 7, 7, 4])

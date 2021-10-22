def numJewelsInStones(jewels, stones):
    stones_map = {}
    for stone in stones:
        if stone in stones_map:
            stones_map[stone] += 1
        else:
            stones_map[stone] = 1
    answer = 0
    for jewel in jewels:
        if jewel in stones_map:
            answer += stones_map[jewel]
    print(answer)


numJewelsInStones("z", "ZZ")

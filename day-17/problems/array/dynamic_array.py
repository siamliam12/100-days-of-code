def dynamicArray(n, queries):
    # Write your code here
    lastAnswer = 0
    seqList = [[] for i in range(n)]
    result = []
    for i in range(len(queries)):
        query_type = queries[i][0]
        x = queries[i][1]
        y = queries[i][2]
        idx = ((x ^ lastAnswer) % n)
        if query_type == 1:
            seqList[idx].append(y)
        else:
            lastAnswer = seqList[idx][y%len(seqList[idx])]
            result.append(lastAnswer)
    return result

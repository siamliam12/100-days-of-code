def matchingStrings(stringList, queries):
    # Write your code here
    count = 0
    result = []
    for query in queries:
        if query in stringList:
            count = stringList.count(query)
            print(query)
        else:
            count = 0
        result.append(count)
    print(result)
    


matchingStrings(
    ['aba','baba','aba','xzxb'],
    ['aba','xzxb','ab']
)
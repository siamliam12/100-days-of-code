
if __name__ == '__main__':
    nested_lst=[]
    lst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_lst.append([name,score])
    dic = dict(nested_lst)
    val = sorted(dic.values())[1]
    for k,v in dic.items():
        if v==val:
            lst.append(k)
    ([print(x) for x in sorted(lst)])
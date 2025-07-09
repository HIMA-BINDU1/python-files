def function(n,list):
    print(list)
    reve = []
    summ=0
    for i in range(n-1,-1,-1):
        reve.append(list[i])
    print(reve)
    for i in reve:
        summ += i

    print(summ)
    print(summ//n)

n = int(input())
li = list(map(int,input().split()))
function(n,li)


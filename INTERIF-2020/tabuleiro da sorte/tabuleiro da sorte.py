#entrada: dia, mes, ano
N=list(map(int, input().split()))
#print(N)
Ma=[]
for c in range(N[0]%5+3):
    li=[]
    for a in range(N[0]%5+3):
        li.append(0)
    Ma.append(li)
Ma[0][0]=int(N[2])
Ma[0][1]=int(N[1])
Ma[1][0]=int(N[0])
for a in range(N[0]%5+3):
    for b in range(N[0]%5+3):
        if a==0 and b>1:
            Ma[a][b]=Ma[a][b-1]+b
        elif a>1 and b==0:
            Ma[a][b]=Ma[a-1][b]+a
        elif a>0 and b>0:
            Ma[a][b]=Ma[a-1][b-1]+Ma[a-1][b]+Ma[a][b-1]
print(Ma[N[0]%5+2][N[0]%5+2])

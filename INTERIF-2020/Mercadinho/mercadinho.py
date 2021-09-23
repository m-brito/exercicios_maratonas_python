#idade cliente
#pontos de promocao
N = int(input())
S = int(input())
V = float(input())
if S>0:
    C =S*2+0.25*N
else:
    C=0
print("{:.2f}".format(V-(C*V)/100))
print("{:.2f}%".format(C))

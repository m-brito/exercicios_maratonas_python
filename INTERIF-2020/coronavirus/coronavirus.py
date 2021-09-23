# -*- coding: utf-8 -*-
#leitos uti, quantos estao oculpados
#a partir da segunda linha
#numero de pacientes admitidos da ut, de alta da uti
# a analise so é feita quanto não houver paciente admitidos nem
#paciente que tiveram alta (X=Y=0)
A,B=input().split()
A=int(A)
B=int(B)
X=1
Y=1
fase1=0
fase2=0
fase3=0
fase4=0
achou=False
leitos=B
while achou==False:
    X,Y=input().split()
    X=int(X)
    Y=int(Y)
    leitos+=(X-Y)
    porcentagem=leitos/A
    if X==0 and Y==0:   
        achou=True
    elif porcentagem*100>80:
        fase1+=1
    elif porcentagem*100<=80 and porcentagem*100>=70:
        fase2+=1
    elif porcentagem*100<70 and porcentagem*100>=60:
        fase3+=1
    else:
        fase4+=1

print('Fase 1: {} semana(s)'.format(fase1))
print('Fase 2: {} semana(s)'.format(fase2))
print('Fase 3: {} semana(s)'.format(fase3))
print('Fase 4: {} semana(s)'.format(fase4))

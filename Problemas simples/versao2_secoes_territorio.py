#Divide as seções totais de um território igualmente em 2 reinos. 

num_territorios = int (input())
secoes = list((map(int, input().split())))
soma_total = sum(secoes)

consegue = False
soma_aux = 0
for num_secoes, valor in enumerate (secoes): #start=2???
    soma_aux += valor
    if soma_aux == soma_total / 2:
        consegue = True
        print (num_secoes + 1)
        break
if not consegue:
    print ("Não foi possível dividir igualmente")

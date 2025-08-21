#Divide as seções totais de um território igualmente em 2 reinos.

num_territorios = int (input())
valores = input().split()
comprimentos = [int(x)   for x in valores]
soma_total = 0

for x in comprimentos:
    soma_total += x

soma_aux = 0
num_secoes = 0
for x in comprimentos:
    soma_aux += x
    num_secoes += 1
    if (soma_aux == soma_total/2):
        break
print (num_secoes)

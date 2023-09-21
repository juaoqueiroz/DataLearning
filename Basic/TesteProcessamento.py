dados = open("medicao.txt").readlines()

for linha in dados:
    linha = linha.rstrip('\n')

print(dados[22], end = "")
print(dados[23])

dados.insert(22, "tempo 01")

print (dados[22], end = "")

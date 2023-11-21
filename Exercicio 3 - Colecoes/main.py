### Juan Carlos GES 41

#### Questao 1
# Nao consegui encontrar a tabela dos times,
# Por isso, inventei as colocações
# Barcelona, Corintias, Flamengo, Real Madrid, Santos

print("### Questão 1 ###")
campeonato = ["Barcelona", "Santos", "Real Madrid", "Flamengo", "Corintias"]
print(campeonato)
## a)
print(campeonato[:3])

## b)
print(campeonato[3:])

## c)
campeonato.sort()
print(campeonato)

## d)
print("Barcelona se encontra na posição", campeonato.index("Barcelona"))

print()
print("######################################################################################################")
print()

### Questao 2
print("### Questão 2 ###")
loja1 = {'iPhone', 'Xiaomi', 'Samsung'}
loja2 = {'Xiaomi', 'LG'}

print("Na loja 1 encontram-se estes modelos:")
for item in loja1:
    print(item)
print()

print("Na loja 2 encontram-se estes modelos:")
for item in loja2:
    print(item)
print()

print("Todos os modelos disponiveis:")
print(loja1.union(loja2))
print()
print("Em ambas as lojas encontram-se estes modelos:")
print(loja1.intersection(loja2))

print()
print("######################################################################################################")
print()

### Questao 3
print("### Questão 3 ###")

dados = {}

dados['nome'] = input("Entre com o nome: ")
dados['media'] =  int(input("Entre com a media: "))

if dados['media'] >= 60:
    dados['situacao'] = "AP"
else:
    dados['situacao'] = "RP"

print(dados['nome'], "está", dados['situacao'])

print(dados)
print("Nome:", dados['nome'])
print("Media:", dados['media'])
print("Situação:", dados['situacao'])

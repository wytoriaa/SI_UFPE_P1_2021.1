#ordenar essa lista de TikTokers seguindo os seguintes critérios:
#primeiramente iria ordenar baseado no número de seguidores
#caso seja o mesmo número, ordenaria crescentemente baseado 
#no tamanho da string do nome do TikToker e se ambos fossem iguais, 
#o critério final seria a posição que foi inserido no input.

n = int(input()) #tiktokers
fav = []

for i in range(n):
  nome, seguidor = input().split('-')
  fav.append([nome, int(seguidor)])
for y in range(len(fav) - 1):
  for w in range(len(fav) - 1):
    if fav[w][1] > fav[w + 1][1]:
      guard = fav[w]
      fav[w] = fav[w + 1]
      fav[w + 1] = guard
for k in range(n): #k = cada elemento da lista
  print(f'{fav[k][0]}-{fav[k][1]}')
info = [] #lista que vai receber minhas informacoes
x = "" #elemento que vai se adequar as condicoes q ele vai pedir
flag = True #enquanto for vdd vai passar por todas as condicoes do while
space = ""
while flag:
  x = input()
  if x == 'adicionar':
    nome, posicao = input().split(" ")
    posicao = int(posicao)
    info.insert(posicao, nome) #inserindo nome e posicao
  elif x == "atualizar indice":
    nome, posicao = input().split(" ")
    posicao = int(posicao)
    if info[posicao] == nome: #info[posicao] = o indice da minha lista
      print("Nada mudou, a lista permanece igual")
    else:
      info.remove(nome)
      info.insert(posicao, nome)
  elif x == "imprimir lista atual":
    for i in info:
      space += i + " "
    print(f"{space.strip()}")
    space = ""
  elif x == "lista finalizada": 
    flag = False #como esta a minha lista finaliza aqui
    print("A lista ficou da seguinte forma:")
    for i in info:
      space += i + " "
    print(f"{space.strip()}")
  else:
    print('Opçao não encontrada')
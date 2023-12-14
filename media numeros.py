def adicionar(lista, numeros):
  with open(numeros, "w")as arquivo:
      for n in lista:
          arquivo.write(str(n))
  return numeros

def media(numeros):
  lista=[]
  with open(numeros, "r")as arquivo:
      for linha in arquivo:
        lista.append(int(linha))
  media=sum(lista)/len(lista)
  print(media)

lista=[1,2,3,4,5,6,7,8,9,10]
numeros="arquivo.txt"
numeros=adicionar(lista, numeros)
media(numeros)

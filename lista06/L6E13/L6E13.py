# Feito por Vinícius Silva Sena
#13
import random

arquivos = {'Animal.txt' :  'Animal',
            'Carro.txt' : 'Carro',
            'Cidade.txt' : 'Cidade'}

def choiceWord():
  arquivo = random.choice(list(arquivos))
  linhas = open(arquivo).read().splitlines()
  palavra = random.choice(linhas)
  dica = arquivos[arquivo]
  return palavra, dica

def embaralhar(palavra):
   n = list(palavra)
   random.shuffle(n)
   result = ''.join(n)
   return result.lower()

newGame = 0

while newGame == 0:

  i = random.randint(0,5)
  palavra, dica = choiceWord()
  palavra02 = embaralhar(palavra)

  x = 6
  print("Dica: ",dica)
  while x != 0:
    print("Palavra oculta: ",palavra02)
    resp = input("Palpite: ")
    if resp.lower() == palavra.lower():
      print("Vencedor!")
      break
    else:
      print("Resposta errada, restam ",(x-1)," palpites")
      x -= 1

  if x == 0 :
    print("A palavra era - ",palavra)
    print("Game Over")
  else:
    print("Voce acertou era - ",palavra)
    print("Créditos subindo na tela")
  print("----------------------------------")
  newGame = int(input("Digite 0 para jogar novamente: "))

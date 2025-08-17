import random
import time
def classe():
    return{
    "M": {"Nome":"Mago","Ataque":15,"Vida":25},
    "A": {"Nome":"Arqueiro","Ataque":25,"Vida":15},
    "C": {"Nome":"Clerigo","Ataque":10,"Vida":45 }
    }
def racas():
    return{
    "Nome":"Humano","Descrição":"Adaptável e Versátil",
    "Nome":"Elfo","Descrição":"Ágil e conectado com a natureza",
    "Nome":"Demônio","Descrição":"Poderoso"
    }
personagem={
     "Nome":"",
     "Raça":"",
     "Classe":"",
     "Inventário":[],
     "Ataque":"",
     "Vida":""
}
        
def mostrar_classe():
    print("\n------ INFORMAÇÕES DAS CLASSES ------")
    print("M - Mago (Ataque: 15, Vida: 25)")
    print("A - Arqueiro (Ataque: 25, Vida: 15)")
    print("C - Clérigo (Ataque: 10, Vida: 45)")
    print("------------------------------------")

def acordarelfo():
    print("O elfo foi muito simpático com você, e lhe pediu se gostaria de o acompanhar em uma caminhada pela floresta.")
    escolha=input("Você seguirá o elfo(S/N): ").upper
    if escolha == "S":
        print("Ao Seguir o elfo pela floresta, ele lhe mostrou a sua casa...")
        time.sleep(1)
        print("Porém em poucos minutos ressoaram batidas na porta...")
        time.sleep(1)
        print("Eram dois demônios! Eles vieram cobrar a dívida do elfo!!!! E agora o que fazer??!!")
        time.sleep(1)
        escolha2=input("Você irá Lutar contra os demônios ou irá Fugir?(L/F): ")
        if escolha2=="L":
            print("Parabéns! Os demônios eram fracos e você conseguiu os derrotar. Parece que o elfo está lhe devendo agora...")
            personagem["Ataque"].append("+5 de ataque")
        elif escolha2=="F":
            print("Você não conseguiu fugir... Além dos demônios terem bloqueado as saídas o elfo também mandou você ficar...")
            return escolha2
    else:
        print("Faça outra escolha.")
def amarrar():
    print("Você amarrou o elfo. E quando ele acordou lhe deu um soco e você desmaiou.")
    print("Ao acordar você estava na casa do elfo, amarrado(a) em uma cadeira de jantar. O elfo não parece nada feliz com a sua presença...")
    print("Em poucos minutos ressoaram batidas na porta...")
    time.sleep(1)
    print("Eram dois demônios! Eles vieram cobrar a dívida do elfo!!!! E agora o que fazer??!!")
    time.sleep(1)
    print("O elfo discretamente, lhe passou uma faca. Assim você cortou as cordas que te amarravam. Mas os demônios ainda permaneciam lá...")
    escolha2=input("Você irá Lutar contra os demônios ou irá Fugir?(L/F): ")
    if escolha2=="L":
        print("Parabéns! Os demônios eram fracos e você conseguiu os derrotar. Parece que o elfo está lhe devendo agora...")
        personagem["Ataque"].append("+5 de ataque")
    elif escolha2=="F":
        print("Você não conseguiu fugir... Além dos demônios terem bloqueado as saídas o elfo também mandou você ficar...")
        return escolha2
def explorar():
    print("Você sai caminhando pela floresta, e ao se aproximar de um córrego encontra algo brilhante," \
    " ao se aproximar percebe que é uma poção de cura.")
    escolha = input("Deseja pegá-la? (S/N): ").upper()
    if escolha == "S":
        personagem["Inventário"].append("Poção de Cura")
        print("Poção de Cura adicionada ao seu inventário!")
    else:
        print("Você deixou a poção para trás.")
    
def  olhar():
    print("Nada")
    
def nada():
    print("Nada")


inicio=input("""Bem vindo, deseja iniciar o jogo?(S/N):""").upper()
while inicio == "S":
        personagem["Nome"]=input("Digite o nome do seu personagem: ")
        while True:
            escolha=input(
                 """Seja bem vindo a essa aventura!!! Hora de escolhermos sua classe!
                    Escolha sua classe: 
                        [M]Mago 
                        [A]Arqueiro
                        [C]Clérigo
                        [I]Ver as informações das classes 
                        Sua Escolha: """).upper()
            
            if escolha=="M"or "A"or"C":
                 print("Parabéns! Você escolheu a sua classe.")
            elif escolha=="I" or "i":
                print("\n------ INFORMAÇÕES DAS CLASSES ------")
                print("M - Mago (Ataque: 15, Vida: 25)")
                print("A - Arqueiro (Ataque: 25, Vida: 15)")
                print("C - Clérigo (Ataque: 10, Vida: 45)")
                print("------------------------------------")
            else:
                print("Opção inválida!")
              
time.sleep(1)
racas=input("""Raças:
Informações das raças(I)
Escolher raça humana(H) 
Sortear raça(S)
Sua Escolha: """).upper()
time.sleep(1)
            
if racas=="S":
    racaescolhida=random.choice(racas)
    print("Parabéns a Raça é:",(racaescolhida).upper(),"!!!!")
elif racas == "I":
    racas()
elif racas=="H":
    print("Parabens Raça HUMANA!!!!")
else:
    print("Essa opção não é válida!!!!")
            
print("Se prepare....")
time.sleep(2)
print("Você acordou em uma floresta e não se lembra de nada... ",time.sleep(1.5))
print("Você olha para o lado e vê um elfo desmaiado, você percebe que está quase escurecendo...",time.sleep(1.5))
print("O que você faz?")

acao=input("Acordar o elfo(A) Amarrar o elfo(B) Explorar a floresta(E) Olhar se você tem algum recurso(O) nada(N)").upper()
if acao=="A":
    acordarelfo()
    print("O Elfo acordou zangado! Ele estava dormindo depois de uma bebedeira!")
elif acao=="B":
    amarrar()
    print("Você amarrou o elfo em uma árvore próxima. Ele não gostou muito e parece estar bem zangado.")
elif acao=="E":
    explorar()
    print("Você saiu andando, mas se deparou com uma gangue de elfos zangados.")
elif acao=="O":
    olhar()
    print("Nada aconteceu. Mas derrepente quatro elfos surgiram ao seu redor.")
elif acao=="N":
    nada()
    print("Parece que você não adquiriu nada ainda. Tente outra opção.")
else:
    print("Opção inválida")

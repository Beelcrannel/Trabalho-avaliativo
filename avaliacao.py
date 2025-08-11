import random
import time

def informacao():
    print("Nehuma informação ainda")
    
def acordarelfo():
    print("Nada")
    
def amarrar():
    print("Nada")

def explorar():
    print("Nada")
    
def  olhar():
    print("Nada")
    
def nada():
    print("Nada")

inicio=input("""Bem vindo, deseja iniciar um jogo?(S/N):""").upper()
racas=["Humano","Humano","Humano","Humano","Anjo","Elfo","Humano","Humano","Humano","Humano","Humano","Elfo","Elfo","Elfo","Demonio","Anao","Anao","Anao","Anao","Homem Lagarto"]
inventario=[]

while inicio == "S":
    classe=input("""Seja bem vindo a essa aventura!!!(escolha uma opção abaixo)
                Informações de classes(I)
                Escolha sua classe: Mago(M), Paladino(P), Arqueiro(A), Ladrão(L), Clerigo(C)""").upper()
    if classe =="I" or "M" or "P" or "A" or "L" or "C":
        pass
    else:
        print("Opção inválida")
        continue
        
    time.sleep(1)
    raca=input("""Raças:
                Informações das raças(I)
                Escolher raça humana(H) Sortear raça(S)""").upper()
    time.sleep(1)
    
    if raca=="S":
        racaescolhida=random.choice(racas)
        print("Parabéns a Raça é:",(racaescolhida).upper(),"!!!!")
    elif raca == "I":
        informacao()
    elif raca=="H":
        print("Parabens Raça HUMANA!!!!")
    else:
        print("Essa opção não é válida!!!!")
        continue
    
    print("Se prepare....")
    time.sleep(2)
    print("Você acordou em uma floresta e não se lembra de nada... ",time.sleep(1.5))
    print("Você olha para o lado e vê um elfo desmaiado, você percebe que está quase escurecendo...",time.sleep(1.5))
    print("O que você faz?")
    acao=input("Acordar o elfo(A) Amarrar o elfo(B) Explorar a floresta(E) Olhar se você tem algum recurso(O) nada(N)").upper()
    
    if acao=="A":
        acordarelfo()
    elif acao=="B":
        amarrar()
    elif acao=="E":
        explorar()
    elif acao=="O":
        olhar()
    elif acao=="N":
        nada()
    else:
        print("Opção inválida")
        continue
    
    inicio=input("Deseja continuar(S/N)").upper()

print("""********Fim de jogo********""")
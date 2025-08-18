import random
import time

def classe():
    return {
        "M": {"Nome": "Mago", "Ataque": 15, "Vida": 25},
        "A": {"Nome": "Arqueiro", "Ataque": 25, "Vida": 15},
        "C": {"Nome": "Clerigo", "Ataque": 10, "Vida": 45}
    }

def sortear_raca():
    racas = ["Humano", "Elfo", "Anjo", "Demonio"]
    probabilidades = [70, 27, 1, 2] 
    return random.choices(racas, weights=probabilidades, k=1)[0]

def racas():
    print("""    "Nome":"Humano","Descrição":"Adaptável e Versátil","Ataque":15,"Vida":25,
    "Nome":"Elfo","Descrição":"Ágil e conectado com a natureza","Ataque":25,"Vida":50,
    "Nome":"Demônio","Descrição":"Poderoso","Ataque":50,"Vida":100,
    "Nome":"Anjo","Descrição":"Simplesmente divino, extremamente poderoso","Ataque":100,"Vida":200""")

def mostrar_classe():
    print("\n------ INFORMAÇÕES DAS CLASSES ------")
    print("M - Mago (Ataque: 15, Vida: 25)")
    print("A - Arqueiro (Ataque: 25, Vida: 15)")
    print("C - Clérigo (Ataque: 10, Vida: 45)")
    print("------------------------------------")

def batalha(jogador, inimigo):
    print(f"\n=== BATALHA CONTRA {inimigo['Nome'].upper()} ===")
    print(f"Seus status: Ataque {jogador['Ataque']} - Vida {jogador['Vida']}")
    print(f"Inimigo: Ataque {inimigo['Ataque']} - Vida {inimigo['Vida']}\n")
    
    while jogador['Vida'] > 0 and inimigo['Vida'] > 0:
        time.sleep(1)
        acao = input("Atacar (A) ou Usar item do inventário (I)? ").upper()
        
        if acao == "A":
            dano_jogador = random.randint(jogador['Ataque'] - 5, jogador['Ataque'] + 5)
            inimigo['Vida'] -= dano_jogador
            print(f"Você atacou e causou {dano_jogador} de dano!")
            
            if inimigo['Vida'] <= 0:
                print(f"Você derrotou o {inimigo['Nome']}!")
                return True
            
            dano_inimigo = random.randint(inimigo['Ataque'] - 5, inimigo['Ataque'] + 5)
            jogador['Vida'] -= dano_inimigo
            print(f"O {inimigo['Nome']} atacou e causou {dano_inimigo} de dano!")
            
            if jogador['Vida'] <= 0:
                print("Você foi derrotado!")
                return False
            
            print(f"\nStatus após rodada: Você {jogador['Vida']}HP - {inimigo['Nome']} {inimigo['Vida']}HP")
        
        elif acao == "I":
            usar_item(jogador)
        
        else:
            print("Ação inválida! Perdeu a vez.")

def usar_item(jogador):
    if not jogador['Inventário']:
        print("Seu inventário está vazio!")
        return
    
    print("\nItens no inventário:")
    for i, item in enumerate(jogador['Inventário'], 1):
        print(f"{i}. {item}")
    
    escolha = input("Digite o número do item que deseja usar (ou 0 para cancelar): ")
    
    try:
        escolha = int(escolha)
        if escolha == 0:
            return
        elif 1 <= escolha <= len(jogador['Inventário']):
            item = jogador['Inventário'].pop(escolha-1)
            
            if "Poção de Cura" in item:
                cura = random.randint(15, 25)
                jogador['Vida'] += cura
                print(f"Você usou {item} e recuperou {cura} de vida!")
            elif "Adaga" in item:
                jogador['Ataque'] += 10
                print(f"Você equipou {item} e ganhou +10 de ataque!")
            else:
                print(f"Você usou {item}, mas não teve efeito.")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida!")

def acordarelfo(jogador):
    time.sleep(1)
    print("Porém em poucos minutos ressoaram batidas na porta...")
    time.sleep(1)
    print("Eram dois demônios! Eles vieram cobrar a dívida do elfo!!!! E agora o que fazer??!!")
    time.sleep(1)
    escolha2 = input("Você irá Lutar contra os demônios ou irá Fugir?(L/F): ").upper()
    
    if escolha2 == "L":
        demonios = {"Nome": "Demônios", "Ataque": 20, "Vida": 30}
        if batalha(jogador, demonios):
            print("Parabéns! Você conseguiu derrotar os demônios. Parece que o elfo está lhe devendo agora...")
            jogador['Ataque'] += 5
        else:
            return False
    elif escolha2 == "F":
        print("Você não conseguiu fugir... Além dos demônios terem bloqueado as saídas o elfo também mandou você ficar...")
        demonios = {"Nome": "Demônios", "Ataque": 20, "Vida": 30}
        if batalha(jogador, demonios):
            print("Mesmo tentando fugir, você conseguiu derrotar os demônios!")
        else:
            return False
    return True

def amarrar(jogador):
    print("Você amarrou o elfo. E quando ele acordou lhe deu um soco e você desmaiou.")
    print("Ao acordar você estava na casa do elfo, amarrado(a) em uma cadeira de jantar. O elfo não parece nada feliz com a sua presença...")
    print("Em poucos minutos ressoaram batidas na porta...")
    time.sleep(1)
    print("Eram dois demônios! Eles vieram cobrar a dívida do elfo!!!! E agora o que fazer??!!")
    time.sleep(1)
    print("O elfo discretamente, lhe passou uma faca. Assim você cortou as cordas que te amarravam. Mas os demônios ainda permaneciam lá...")
    
    escolha2 = input("Você irá Lutar contra os demônios ou irá Fugir?(L/F): ").upper()
    if escolha2 == "L":
        demonios = {"Nome": "Demônios", "Ataque": 20, "Vida": 30}
        if batalha(jogador, demonios):
            print("Parabéns! Você conseguiu derrotar os demônios. Parece que o elfo está lhe devendo agora...")
            jogador['Ataque'] += 5
        else:
            return False
    elif escolha2 == "F":
        print("Você não conseguiu fugir... Além dos demônios terem bloqueado as saídas o elfo também mandou você ficar...")
        demonios = {"Nome": "Demônios", "Ataque": 20, "Vida": 30}
        if batalha(jogador, demonios):
            print("Mesmo tentando fugir, você conseguiu derrotar os demônios!")
        else:
            return False
    return True

def explorar(jogador):
    print("Você sai caminhando pela floresta, e ao se aproximar de um córrego encontra algo brilhante,")
    print("ao se aproximar percebe que é uma poção de cura.")
    escolha = input("Deseja pegá-la? (S/N): ").upper()
    if escolha == "S":
        jogador['Inventário'].append("Poção de Cura")
        print("Poção de Cura adicionada ao seu inventário!")
    else:
        print("Você deixou a poção para trás.")

def olhar(jogador):
    print("\n=== SEU INVENTÁRIO ===")
    if not jogador['Inventário']:
        print("Seu inventário está vazio.")
    else:
        for item in jogador['Inventário']:
            print(f"- {item}")
    print("=====================")

inicio = input("Bem vindo, deseja iniciar o jogo?(S/N): ").upper()

while inicio == "S":
    personagem = {
        "Nome": input("Digite o nome do seu personagem: "),
        "Raça": "",
        "Classe": "",
        "Inventário": [],
        "Ataque": 0,
        "Vida": 0
    }
    
    escolha_valida = "N"
    while escolha_valida != "S":
        escolha = input(
            """Seja bem vindo a essa aventura!!! Hora de escolhermos sua classe!
                Escolha sua classe: 
                    [M]Mago 
                    [A]Arqueiro
                    [C]Clérigo
                    [I]Ver as informações das classes 
                    Sua Escolha: """).upper()

        if escolha in classe():
            personagem["Classe"] = classe()[escolha]["Nome"]
            personagem["Ataque"] = classe()[escolha]["Ataque"]
            personagem["Vida"] = classe()[escolha]["Vida"]
            print(f"Parabéns! Você escolheu a classe {personagem['Classe']}.")
            escolha_valida = "S"
        elif escolha == "I":
            mostrar_classe()
        else:
            print("Opção inválida!")
    
    time.sleep(1)
    racaas = "N"
    time.sleep(1)
    
    while racaas != "S":
        racaas = input("""Raças:
            Informações das raças(I)
            Sortear raça(S)
            Sua Escolha: """).upper()

        if racaas == "S":
            raca_oficial = sortear_raca()
            personagem["Raça"] = raca_oficial
            print(f"Parabéns! A Raça é: {raca_oficial}!!!!")
            
            if raca_oficial == "Humano":
                personagem["Ataque"] += 15
                personagem["Vida"] += 25
            elif raca_oficial == "Elfo":
                personagem["Ataque"] += 25
                personagem["Vida"] += 50
            elif raca_oficial == "Anjo":
                personagem["Ataque"] += 100
                personagem["Vida"] += 200
            elif raca_oficial == "Demonio":
                personagem["Ataque"] += 50
                personagem["Vida"] += 100
            
            racaas = "S"
        elif racaas == "I":
            racas()
        else:
            print("Essa opção não é válida!!!!")
    
    time.sleep(1)
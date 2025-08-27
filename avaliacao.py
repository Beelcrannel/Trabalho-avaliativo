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
    if personagem["Raça"] == "Humano":
        print("Se prepare....")
        time.sleep(2)
        print("Você acordou em uma floresta e não se lembra de nada... ")
        time.sleep(1.5)
        print("Você olha para o lado e vê um elfo desmaiado, você percebe que está quase escurecendo...")
        time.sleep(1.5)
        print("O que você faz?")

        acao = input("Acordar o elfo(A) Amarrar o elfo(B) Explorar a floresta(E) Olhar inventário(O) Nada(N): ").upper()
        
        if acao == "A":
            print("O Elfo acordou zangado! Ele estava dormindo depois de uma bebedeira!")
            print("Elfo: Ei Quem você acha que é? Eu sou um elfo da realeza, como ousas me acordar!!!")
            print("Elfo: Espera... Onde estamos... Por que estou com você no meio do nada?")
            print("Elfo: Quem é você?")
            print("Você: Eu não sei onde estamos, acordei agora também, o que fazemos? está anoitecendo...")
            print("Elfo: Hum, onde estão meus guardas?... parece que não tem mais ninguém por aqui... Olha eu não confio nem um pouco em você, mas vamos tentar nos ajudar para sairmo daqui...")
            
            junto = input("Você deseja se juntar a ele?(S/N): ").upper()
            if junto == "S":
                print("Vocês decidem explorar a floresta e vão até a cabana do elfo")
                if not acordarelfo(personagem):
                    print("============GAME OVER============")
                    inicio = "N"
            else:
                print("Vocês se separam e depois de andar um pouco pela mata você encontra um acampamento")
                explorar(personagem)
        
        elif acao == "B":
            if not amarrar(personagem):
                print("============GAME OVER============")
                inicio = "N"
        
        elif acao == "E":
            explorar(personagem)
            print("Você saiu andando, mas se deparou com uma gangue de elfos zangados.")
            gangue = {"Nome": "Gangue de Elfos", "Ataque": 18, "Vida": 40}
            
            if batalha(personagem, gangue):
                personagem['Inventário'].extend(["Adaga", "Amuleto"])
                print("Você derrotou os elfos e recolheu seus pertences!")
                print("Depois você volta para o local que acordou e acorda o elfo")
                if not acordarelfo(personagem):
                    print("============GAME OVER============")
                    inicio = "N"
        
        elif acao == "O":
            olhar(personagem)
            print("Nada aconteceu. Mas de repente quatro elfos surgiram ao seu redor.")
            print("Do nada um dos elfos usa furtividade e corta sua garganta")
            print("============GAME OVER============")
            inicio = "N"
        
        elif acao == "N":
            print("Parece que você não adquiriu nada ainda. Tente outra opção.")
        
        else:
            print("Opção inválida")
    
    elif personagem["Raça"] == "Elfo":
        print("Se prepare....")
        time.sleep(2)
        print("Você acorda em sua cabana na floresta após uma noite de bebedeira...")
        time.sleep(1.5)
        print("Ao olhar ao redor, você percebe um estranho(a) deitado(a) no chão perto de você...")
        time.sleep(1.5)
        print("O que você faz?")

        acao = input("Acordar o estranho(A) Amarrar o estranho(B) Verificar inventário(V) Nada(N): ").upper()
        
        if acao == "A":
            print("Você acorda o estranho, que parece confuso e desorientado.")
            print("Estranho: Onde estou? Quem é você?")
            print("Você explica que também não sabe como ele veio parar ali...")
            time.sleep(1)
            print("De repente, você ouve batidas na porta... São os demônios que vieram cobrar sua dívida!")
            
            escolha = input("Você irá Lutar(L), Fugir(F) ou Tentar negociar(N)? ").upper()
            
            if escolha == "L":
                demonios = {"Nome": "Demônios Cobradores", "Ataque": 25, "Vida": 35}
                if batalha(personagem, demonios):
                    print("Vocês lutam juntos e derrotam os demônios! Ganhou +10 de ataque permanente!")
                    personagem["Ataque"] += 10
                else:
                    print("============GAME OVER============")
                    inicio = "N"
            
            elif escolha == "F":
                print("Vocês tentam fugir, mas os demônios eram rápidos... Game Over!")
                inicio = "N"
            
            else:
                print("Você negocia com os demônios e consegue mais tempo para pagar a dívida.")
                print("O estranho agora é seu aliado!")
                personagem['Inventário'].append("Aliado Humano")
        
        elif acao == "B":
            print("Você amarra o estranho, que acorda assustado.")
            print("Estranho: O que está fazendo? Me solte!")
            print("Nesse momento, os demônios chegam para cobrar sua dívida...")
            time.sleep(1)
            demonios = {"Nome": "Demônios Furiosos", "Ataque": 30, "Vida": 40}
            
            if batalha(personagem, demonios):
                print("Milagrosamente você conseguiu derrotar os demônios!")
            else:
                print("Os demônios atacam vocês dois! Game Over!")
                inicio = "N"
        
        elif acao == "V":
            olhar(personagem)
            explorar(personagem)
        
        else:
            print("Você decide não fazer nada. Os demônios chegam e...")
            demonios = {"Nome": "Demônios", "Ataque": 25, "Vida": 35}
            
            if batalha(personagem, demonios):
                print("Você sobreviveu por sorte!")
            else:
                print("============GAME OVER============")
                inicio = "N"

    elif personagem["Raça"] == "Anjo":
        print("Se prepare....")
        time.sleep(2)
        print("Você desce dos céus em meio a uma luz divina!")
        time.sleep(1.5)
        print("Ao seu redor, a floresta parece se acalmar com sua presença...")
        time.sleep(1.5)
        print("Você avista um elfo e um humano desacordados no chão.")
        
        acao = input("Acordá-los(A) Deixá-los(B) Observar de longe(O): ").upper()
        
        if acao == "A":
            print("Você os acorda com seu toque divino.")
            print("Ambos ficam maravilhados com sua presença e se tornam seus seguidores!")
            personagem["Inventário"].append("Seguidores: Elfo e Humano")
        
        elif acao == "B":
            print("Você decide não interferir e continua seu caminho.")
            print("Enquanto caminha, encontra um artefato divino perdido!")
            personagem["Inventário"].append("Artefato Divino")
        
        else:
            print("Você observa de longe e percebe que demônios estão se aproximando...")
            escolha = input("Intervir(I) ou Continuar observando(C)? ").upper()
            
            if escolha == "I":
                print("Com um simples gesto, você banha os demônios em luz divina, purificando-os!")
                print("Você ganhou +50 de ataque permanente!")
                personagem["Ataque"] += 50
            else:
                print("Você permite que os eventos aconteçam naturalmente...")
                print("Os demônios levam o elfo embora e o humano foge assustado.")
        
        print("Sua missão na terra está completa. Você retorna aos céus.")
        inicio = "N"

    elif personagem["Raça"] == "Demonio":
        print("Se prepare....")
        time.sleep(2)
        print("Você surge das sombras em meio a um clarão de fogo!")
        time.sleep(1.5)
        print("O ar ao seu redor fica pesado e a floresta parece tremer com sua presença...")
        time.sleep(1.5)
        print("Você avista um elfo desacordado - aquele que deve uma dívida a você - e um estranho.")
        
        acao = input("Acordar o elfo(A) Levar o elfo(L) Assustar o estranho(S): ").upper()
        
        if acao == "A":
            print("Você acorda o elfo com um golpe.")
            print("Elfo: Não! Por favor, mais tempo! Eu vou pagar, eu juro!")
            print("Estranho: O que está acontecendo?")
            
            escolha = input("Levar o elfo(L) ou Levar ambos(B)? ").upper()
            
            if escolha == "L":
                print("Você leva o elfo embora para o inferno. Missão cumprida!")
                personagem["Inventário"].append("Alma do Elfo")
            else:
                print("Você decide levar ambos para o inferno! Ganhou 2 almas!")
                personagem["Inventário"].extend(["Alma do Elfo", "Alma do Humano"])
        
        elif acao == "L":
            print("Você simplesmente pega o elfo inconsciente e o leva embora.")
            print("O estranho acorda assustado com o barulho, mas você já desapareceu nas sombras.")
            personagem["Inventário"].append("Alma do Elfo")
        
        else:
            print("Você emite um rugido demoníaco que faz o estranho acordar em pânico!")
            print("Estranho: AAAAAAH! DEMÔNIO!")
            print("O estranho foge correndo, deixando para trás uma bolsa com itens valiosos.")
            personagem["Inventário"].append("Bolsa de Itens Valiosos")
        
        print("Você retorna ao inferno com seu prêmio. Outra missão concluída!")
        inicio = "N"

    continuar = input("Deseja jogar novamente? (S/N): ").upper()
    if continuar != "S":
        inicio = "N"
        print("Obrigado por jogar! Até a próxima!")
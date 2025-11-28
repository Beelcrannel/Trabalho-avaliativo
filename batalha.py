import random
import time

class Batalha:
    def batalhar(self, jogador, inimigo):
        print(f"\n=== BATALHA CONTRA {inimigo['Nome'].upper()} ===")
        print(f"Seus status: Ataque {jogador.ataque} - Vida {jogador.vida}")
        print(f"Inimigo: Ataque {inimigo['Ataque']} - Vida {inimigo['Vida']}\n")

        while jogador.vida > 0 and inimigo['Vida'] > 0:
            time.sleep(1)
            acao = input("Atacar (A) ou Usar item do inventário (I)? ").upper()

            if acao == "A":
                dano_jogador = random.randint(jogador.ataque - 5, jogador.ataque + 5)
                inimigo['Vida'] -= dano_jogador
                print(f"Você atacou e causou {dano_jogador} de dano!")

                if inimigo['Vida'] <= 0:
                    print(f"Você derrotou o {inimigo['Nome']}!")
                    return True

                dano_inimigo = random.randint(inimigo['Ataque'] - 5, inimigo['Ataque'] + 5)
                jogador.vida -= dano_inimigo
                print(f"O {inimigo['Nome']} atacou e causou {dano_inimigo} de dano!")

                if jogador.vida <= 0:
                    print("Você foi derrotado!")
                    return False

                print(f"\nStatus após rodada: Você {jogador.vida}HP - {inimigo['Nome']} {inimigo['Vida']}HP")

            elif acao == "I":
                self.usar_item(jogador)
            else:
                print("Ação inválida! Perdeu a vez.")

        return jogador.vida > 0

    def usar_item(self, jogador):
        if not jogador.inventario:
            print("Seu inventário está vazio!")
            return

        print("\nItens no inventário:")
        for i, item in enumerate(jogador.inventario, 1):
            print(f"{i}. {item}")

        escolha = input("Digite o número do item que deseja usar (ou 0 para cancelar): ")
        try:
            escolha = int(escolha)
            if escolha == 0:
                return
            elif 1 <= escolha <= len(jogador.inventario):
                item = jogador.inventario.pop(escolha - 1)
                if "Poção de Cura" in item:
                    cura = random.randint(15, 25)
                    jogador.vida += cura
                    print(f"Você usou {item} e recuperou {cura} de vida!")
                elif "Adaga" in item:
                    jogador.ataque += 10
                    print(f"Você equipou {item} e ganhou +10 de ataque!")
                else:
                    print(f"Você usou {item}, mas não teve efeito.")
            else:
                print("Número inválido!")
        except ValueError:
            print("Entrada inválida!")

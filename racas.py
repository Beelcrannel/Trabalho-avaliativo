import random

class Racas:
    @staticmethod
    def sortear_raca():
        racas = ["Humano", "Elfo", "Anjo", "Demonio"]
        probabilidades = [70, 27, 1, 2]
        return random.choices(racas, weights=probabilidades, k=1)[0]

    @staticmethod
    def mostrar_racas():
        print(""" Nome: Humano, Descrição: Adaptável e Versátil, Ataque: 15, Vida:25 ,
Nome: Elfo, Descrição: Ágil e conectado com a natureza, Ataque: 25, Vida: 50,
Nome: Demônio, Descrição: Poderoso, Ataque: 50, Vida: 100,
Nome: Anjo, Descrição: Simplesmente divino, extremamente poderoso, Ataque: 100, Vida: 200""")

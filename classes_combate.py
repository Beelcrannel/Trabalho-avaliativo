class Classes:
    @staticmethod
    def obter_classes():
        return {
            "M": {"Nome": "Mago", "Ataque": 15, "Vida": 25},
            "A": {"Nome": "Arqueiro", "Ataque": 25, "Vida": 15},
            "C": {"Nome": "Clerigo", "Ataque": 10, "Vida": 45}
        }

    @staticmethod
    def mostrar_classe():
        print("\n------ INFORMAÇÕES DAS CLASSES ------")
        print("M - Mago (Ataque: 15, Vida: 25)")
        print("A - Arqueiro (Ataque: 25, Vida: 15)")
        print("C - Clérigo (Ataque: 10, Vida: 45)")
        print("------------------------------------")

class Terrestre:

    se_move_em_terra = True

    def __init__(self, velocidade = 100):
        self.velocidade = velocidade

class Aquatico:

    se_move_na_agua = True

    def __init__(self, velocidade = 5):
        self.velocidade = velocidade

class Carro:

    rodas = 4

    def __init__(self, velocidade = 120, pistoes = 4):
        self.pistoes = pistoes
        Terrestre.__init__(self,velocidade = velocidade)

class Barco:

    def __init__(self, velocidade = 6, helices = 1):
        self.helices = helices
        Aquatico.__init__(self, velocidade = velocidade)

class Anfibio:

    def __init__(self, velocidade_em_terra = 80, 
            velocidade_na_agua = 4, 
            pistoes = 6, 
            helices = 2):
        Carro.__init__(self, velocidade = velocidade_em_terra, pistoes = pistoes)
        Barco.__init__(self, velocidade = velocidade_na_agua, helices = helices)

novo_anfibio = Anfibio()
for atr in dir(novo_anfibio):
    if not atr.startswith('__'):
        print(atr,' = ',getattr(novo_anfibio,atr))




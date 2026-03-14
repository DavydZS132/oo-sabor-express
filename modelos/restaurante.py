class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante()
restaurante_pizza = Restaurante()

restaurante = [restaurante_praca, restaurante_pizza]
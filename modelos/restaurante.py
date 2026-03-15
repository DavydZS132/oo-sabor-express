class Restaurante:
    def __init__(this, nome, categoria):
        this.nome = nome
        this.categoria = categoria
        this.ativo = False
    def __str__(this):
        return f'{this.nome} | {this.categoria}'

restaurante_praca = Restaurante('Artur', 'Lanches')
restaurante_pizza = Restaurante('Pizza Expres', 'Italiano')

restaurante = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
print(restaurante_pizza)
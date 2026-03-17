# 1. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro:
    def __init__(self, modelo, cor, ano):
        
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro(modelo='Fiat Uno', cor='Preto', ano=2004)

# 2. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos. 

# 3. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

# 4. Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        self.ativo = ativo

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.capacidade} | {self.nota_avaliacao} | {self.ativo}'

cafeteria = Restaurante(nome='Gran Aroma Café', categoria='Cafeteria Gourmet')
print(cafeteria)


# 5. Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:
    def __init__(self, nome, cpf=0, telefone=0, ativo=False):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.ativo = ativo

cliente1 = Cliente(nome='Davyd')

print(vars(cliente1))
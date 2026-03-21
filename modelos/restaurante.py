class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria do Restaurante'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return ' Verdadeiro' if self._ativo else 'falso'

restaurante_praca = Restaurante('Artur', 'Lanches')
restaurante_pizza = Restaurante('Pizza Expres', 'Italiano')

Restaurante.listar_restaurantes()
class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = input('Digite o nome do restaurante: ')
restaurante_praca.categoria = input('Digite a categoria do restaurante: ')

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

categoria = Restaurante.categoria


restaurante_pizza = Restaurante()

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

restaurante_pizza.ativo = True


print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')


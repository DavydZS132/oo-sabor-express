from modelos.restaurante import Restaurante

cafeteria = Restaurante('cafeteria manhã', 'cafeteria')
cafeteria.receber_avaliacao('Davyd', 10)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
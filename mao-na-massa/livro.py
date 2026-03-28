# 1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

class Livro:
    def __init__(self, titulo='', autor='', ano_publicado=int, diponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicado = ano_publicado
        self.disponivel = diponivel
# 2. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self):
        return f'{self.titulo}\n {self.autor}\n {self.ano_publicado}\n {self.disponivel}'
# 3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    def emprestar_livro(self):
        self.disponivel = False
# 4. Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    # @classmethod
    # def verificar_disponibilidade(cls, ano):
    #     livros_filtrados = [livro for livro in cls.livros if livro.ano_publicado == ano and livro.disponivel]
    #     return livros_filtrados
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicado == ano and livro.disponivel]
        return livros_disponiveis

livro1 = Livro('A Menina do Outro Lado', 'Nagabe', 2023)
livro2 = Livro('Hunter X Hunter', 'Yosihiro Togashi', 2025)

Livro.livros = [livro1, livro2]

# disponivel = Livro.verificar_disponibilidade(2023)

# for livro in disponivel:
#     print(livro)
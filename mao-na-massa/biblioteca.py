from livro import Livro

# 5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

# 6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
livro1 = Livro('A Menina do Outro Lado', 'Nagabe', 2023)
print(f"Antes de emprestar (biblioteca): Livro disponível? {livro1}")
print(f"Depois de emprestar (biblioteca): Livro disponível? {livro1}")
# 7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
ano_especifico = 2023
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
for livro in livros_disponiveis_ano:
    print(f"Livros disponíveis em {ano_especifico}: {livro}")

# 8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
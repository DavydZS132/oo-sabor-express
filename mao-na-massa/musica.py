class Musica:
    nome = ''
    artista = ''
    duracao = int

artista_jobs = Musica()

artista_jobs.nome = 'Julio'
artista_jobs.artista = 'Raper'
artista_jobs.duracao = 12

print(vars(artista_jobs))
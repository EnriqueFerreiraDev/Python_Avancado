import requests
import time
import csv
import random
import concurrent.futures
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

MAX_THREADS = 10

def extract_movie_details(movie_info):
    title, release_date, classification, plot_text = movie_info

    with open('movies.csv', mode='a', newline='', encoding='utf-8') as file:
        movie_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        movie_writer.writerow([title, release_date, classification, plot_text])

def extract_movies_data(movie_data):
    title = movie_data.get('Titulo')
    release_date = movie_data.get('Data de lancamento')
    classification = movie_data.get('Classificacao')
    plot_text = movie_data.get('Sinopse')

    return title, release_date, classification, plot_text

def extract_movies():
    movie1_info = {
        'Titulo': 'Um Sonho de Liberdade',
        'Data de lancamento': '25 de janeiro de 1995',
        'Classificacao': '16+',
        'Sinopse': 'Em 1946, Andy Dufresne (Tim Robbins), um jovem e bem sucedido banqueiro, tem a sua vida radicalmente modificada ao ser condenado por um crime que nunca cometeu, o homicídio de sua esposa e do amante dela. Ele é mandado para uma prisão que é o pesadelo de qualquer detento, a Penitenciária Estadual de Shawshank, no Maine. Lá ele irá cumprir a pena perpétua. Andy logo será apresentado a Warden Norton (Bob Gunton), o corrupto e cruel agente penitenciário, que usa a Bíblia como arma de controle e ao Capitão Byron Hadley (Clancy Brown) que trata os internos como animais. Andy faz amizade com Ellis Boyd Redding (Morgan Freeman), um prisioneiro que cumpre pena há 20 anos e controla o mercado negro da instituição.'
    }

    movie2_info = {
        'Titulo': 'O Poderoso Chefao',
        'Data de lancamento': '07 de Julho de 1972',
        'Classificacao': '14+',
        'Sinopse': 'Don Vito Corleone (Marlon Brando) é o chefe de uma "família" de Nova York que está feliz, pois Connie (Talia Shire), sua filha, se casou com Carlo (Gianni Russo). Porém, durante a festa, Bonasera (Salvatore Corsitto) é visto no escritório de Don Corleone pedindo "justiça", vingança na verdade contra membros de uma quadrilha, que espancaram barbaramente sua filha por ela ter se recusado a fazer sexo para preservar a honra. Vito discute, mas os argumentos de Bonasera o sensibilizam e ele promete que os homens, que maltrataram a filha de Bonasera não serão mortos, pois ela também não foi, mas serão severamente castigados. Vito porém deixa claro que ele pode chamar Bonasera algum dia para devolver o "favor". Do lado de fora, no meio da festa, está o terceiro filho de Vito, Michael (Al Pacino), um capitão da marinha muito decorado que há pouco voltou da 2ª Guerra Mundial.'
    }

    movie3_info = {
        'Titulo': 'Batman - O Cavaleiro das Trevas',
        'Data de lancamento': '19 de julho de 2008',
        'Classificacao': '12+',
        'Sinopse': 'Após dois anos desde o surgimento do Batman (Christian Bale), os criminosos de Gotham City têm muito o que temer. Com a ajuda do tenente James Gordon (Gary Oldman) e do promotor público Harvey Dent (Aaron Eckhart), Batman luta contra o crime organizado. Acuados com o combate, os chefes do crime aceitam a proposta feita pelo Coringa (Heath Ledger) e o contratam para combater o Homem-Morcego.'
    }

    movies_data = [movie1_info, movie2_info, movie3_info]

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        # Armazene os resultados em uma lista
        movie_details = list(executor.map(extract_movies_data, movies_data))
        # Use a lista para passar os resultados para a próxima chamada
        executor.map(extract_movie_details, movie_details)

def main():
    start_time = time.time()

    # Limpando o arquivo CSV
    with open('movies.csv', mode='w', newline='', encoding='utf-8') as file:
        file.truncate()
        movie_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        movie_writer.writerow(['Titulo', 'Data de lancamento', 'Classificacao', 'Sinopse'])

    # Extrair dados dos filmes
    extract_movies()

    end_time = time.time()
    print('Total time taken: ', end_time - start_time)

if __name__ == '__main__':
    main()
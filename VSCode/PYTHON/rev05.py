#Web
import webbrowser

termo_pesquisa = input("Digite o nome do termo pesquisa: ")
url_google_search = f"https://www.google.com/search?q={termo_pesquisa}"
print(f"abrindo navegador pra pesquisa: {url_google_search}")
webbrowser.open(url_google_search)
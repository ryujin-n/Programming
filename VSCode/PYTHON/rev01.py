#Cadastro de usuario
import os
ARQUIVO = "agenda.txt"

def _normaliza_texto(txt):
    return txt.strip()

def _parse_linha(linha):
    linha = linha.strip()
    if not linha:
        return None
    if "," not in linha:
         return None
    nome, telefone = linha.split(",", 1)
    return _normaliza_texto(nome), _normaliza_texto(telefone)

def _carrega_contatos():
    if not os.path.exists("ARQUIVO"):
        return []
    with open("ARQUIVO", "r", encoding="utf-8") as f:
        linhas = f.readlines()
    contatos = []
    for linha in linhas:
        parsed = _parse_linha(linha)
        if parsed:
            contatos.append(parsed)
    return contatos
def _salva_contatos(contatos):
    with open("ARQUIVO", "w", encoding="utf-8") as f:
        for nome, telefone in contatos:
            f.write(f"{nome},{telefone}\n")

#CRUD

def criar_contato(nome, telefone):
    nome = _normaliza_texto(nome)
    telefone = _normaliza_texto(telefone)
    if not nome or not telefone:
        print("Nome e telefone invalidos")
        return
    contatos = _carrega_contatos()
    if any(c[0].lower() == nome.lower() for c in contatos):
        print("Nome e telefone ja existentes")
        return
    contatos.append((nome, telefone))
    _salva_contatos(contatos)
    print(f"Contato ({nome}) criada com sucesso!")

def listar_contatos():
    contatos = _carrega_contatos()
    if not contatos:
        print("Nenhum contato foi encontrado")
        return
    for i, (nome, telefone) in enumerate(contatos, start=1):
        print(f"{i}. {nome} - {telefone}")

def atualizar_contato(nome_antigo, novo_nome, novo_telefone):  # Atualiza um contato existente
    nome_antigo = _normaliza_texto(nome_antigo)  # Limpa nome antigo
    novo_nome = _normaliza_texto(novo_nome)  # Limpa novo nome
    novo_telefone = _normaliza_texto(novo_telefone)  # Limpa novo telefone
    if not novo_nome or not novo_telefone:  # Valida campos
        print("Novo nome e novo telefone não podem ser vazios.")  # Mensagem
        return  # Sai

    contatos = _carrega_contatos()  # Carrega contatos
    atualizado = False  # Flag para saber se achou/atualizou

    for idx, (nome, telefone) in enumerate(contatos):  # Percorre a lista com índice
        if nome.lower() == nome_antigo.lower():  # Compara ignorando maiúsculas/minúsculas
            contatos[idx] = (novo_nome, novo_telefone)  # Substitui pelo novo par (nome, telefone)
            atualizado = True  # Marca que atualizou
            break  # Para após a primeira ocorrência (didático)

    if atualizado:  # Se atualizou
        _salva_contatos(contatos)  # Persiste as mudanças
        print(f"Contato '{nome_antigo}' atualizado para '{novo_nome}'.")  # Confirmação
    else:  # Caso não encontre
        print(f"Contato '{nome_antigo}' não encontrado.")  # Informa

def deletar_contato(nome):
    nome = _normaliza_texto(nome)
    contatos = _carrega_contatos()
    tamanho_antes = len(contatos)
    contatos = [(n, t) for (n, t) in contatos if n.lower() != nome.lower()]
    if len(contatos) < tamanho_antes:
        _salva_contatos(contatos)
        print(f"Contato '{nome}' removido com sucesso!")
    else:
        print(f"Contato '{nome}' não encontrado")

#Console

def menu():
    while True:
        print("Agenda Telefonica")
        print("1 - Criar contato")
        print("2 - Listar contatos")
        print("3 - Atualizar contato")
        print("4 - Deletar contato")
        print("5 - Sair")

        opcao = input("Escolha uma opcao: ").strip()
        if opcao == "1":
            nome = input("Nome do contato: ")
            telefone = input("Telefone do contato: ")
            criar_contato(nome, telefone)
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            antigo = input("Digite o nome do antigo: ")
            novo = input("Digite o nome do contato: ")
            tel = input("Digite o telefone do contato: ")
            atualizar_contato(antigo, novo, tel)
        elif opcao == "4":
            nome = input("Nome do contato: ")
            deletar_contato(nome)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção invalida")

if __name__ == "__main__":
    menu()

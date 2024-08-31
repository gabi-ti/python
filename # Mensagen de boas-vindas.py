# Mensagem de boas-vindas
print('Bem-vinda a Livraria da Gabriela Lopes')

# Lista vazia de livros e variável global para ID
lista_livro = []
id_global = 0

# Função para cadastrar livro
def cadastrar_livro(id):
    global id_global
    id_global += 1
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(livro)

# Função para consultar livro
def consultar_livro():
    opcao = input("Escolha uma opção:\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Autor\n4. Retornar ao menu\n")
    if opcao == "1":
        for livro in lista_livro:
            print(livro)
    elif opcao == "2":
        id_consulta = int(input("Digite o ID do livro: "))
        for livro in lista_livro:
            if livro["id"] == id_consulta:
                print(livro)
                break
        else:
            print("Livro não encontrado.")
    elif opcao == "3":
        autor_consulta = input("Digite o nome do autor: ")
        for livro in lista_livro:
            if livro["autor"] == autor_consulta:
                print(livro)
    elif opcao == "4":
        return
    else:
        print("Opção inválida")
        consultar_livro()

# Função para remover livro
def remover_livro():
    id_remover = int(input("Digite o ID do livro a ser removido: "))
    for livro in lista_livro:
        if livro["id"] == id_remover:
            lista_livro.remove(livro)
            print("Livro removido com sucesso.")
            return
    else:
        print("ID inválido.")
        remover_livro()

# Menu principal
while True:
    opcao_principal = input("\nEscolha uma opção:\n1. Cadastrar Livro\n2. Consultar Livro\n3. Remover Livro\n4. Encerrar Programa\n")
    if opcao_principal == "1":
        cadastrar_livro(id_global)
    elif opcao_principal == "2":
        consultar_livro()
    elif opcao_principal == "3":
        remover_livro()
    elif opcao_principal == "4":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida")
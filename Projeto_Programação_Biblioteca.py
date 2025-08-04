from docx import Document
import os

# -------------------- Registros e listagens de dados --------------------

def registar_livros(livros):
    n = int(input("Quantos livros deseja registrar? "))
    for _ in range(n):
        nome = input("Nome do livro: ")
        autor = input(f"Autor do livro {nome}: ")
        ano = int(input("Ano de publicação: "))
        livros.append(Livro(nome, autor, ano))
        
def registar_utilizadores(utilizadores):
    n = int(input("Quantos utilizadores deseja registrar? "))
    for i in range(n):
        nome = input("Nome do utilizador: ")
        contato = int(input("Contato: "))
        ID = len(utilizadores)
        utilizadores.append(Utilizador(nome, ID, contato))
        
def fazer_emprestimo(emprestimos, livros, utilizadores):
    listar_livros(livros)
    id_l = int(input("Informe o ID do livro: "))
    listar_utilizadores(utilizadores)
    id_u = int(input("Informe o ID do utilizador: "))
    if id_l >= len(livros) or id_u >= len(utilizadores) or not livros[id_l].disponivel:
        print("Erro! ID inválido ou livro indisponível.")
        return
    data = input("Data do empréstimo (dd/mm/aaaa): ")
    previsão_devo = input("Data prevista de devolução (dd/mm/aaaa)")
    livros[id_l].disponivel = False
    emprestimos.append(Emprestimo(id_l, id_u, data, previsão_devo))

def fazer_devolucao(emprestimos, livros, utilizadores):
    id_l = int(input("ID do livro a devolver: "))
    for e in emprestimos:
        if e.id_livro == id_l and e.data_devolucao == "-":
            e.data_devolucao = input("Data da devolução (dd/mm/aaaa): ")
            livros[id_l].disponivel = True
            print("Livro devolvido com sucesso!")
            guardar_livros_docx(livros)
            guardar_emprestimos_docx(emprestimos, livros, utilizadores)
            return
    print("Erro: empréstimo não encontrado ou já devolvido.")
        
def listar_livros(livros):
    print("\n--- Livros ---")
    for i, l in enumerate(livros):
        print(f"ID: {i} | Nome: {l.nome} | Autor: {l.autor} | Ano: {l.ano} | Disponível: {'Sim' if l.disponivel else 'Não'}")
        
def listar_utilizadores(utilizadores):
    print("\n--- Utilizadores ---")
    for i, u in enumerate(utilizadores):
        print(f"ID: {i} | Nome: {u.nome} | Contato: {u.contato}")
        
def listar_emprestimos(emprestimos, livros, utilizadores):
    print("\n--- Empréstimos ---")
    for e in emprestimos:
        if e.id_livro < len(livros) and e.id_utilizador < len(utilizadores):
            livro = livros[e.id_livro].nome
            user = utilizadores[e.id_utilizador].nome
            print(f"Livro: {livro} | Utilizador: {user} | Empréstimo: {e.data_emprestimo} | Devolução prevista: {e.data_prevista_devolucao} | Devolução: {e.data_devolucao if e.data_devolucao != '-' else 'Pendente'}")

# -------------------- Atualização de dados --------------------

def atualizar_dados_livro(livros):
    listar_livros(livros)
    id_l = int(input("ID do livro a atualizar: "))
    if 0 <= id_l < len(livros):
        livros[id_l].nome = input("Novo nome do livro: ")
        livros[id_l].autor = input("Novo autor: ")
        livros[id_l].ano = int(input("Novo ano: "))
        print("Livro atualizado com sucesso!")
    else:
        print("ID inválido.")
        
def atualizar_disponibilidade_livros(livros, emprestimos):
    for livro in livros:
        emprestado = any(
            e.id_livro == livros.index(livro) and e.data_devolucao == "-"
            for e in emprestimos
        )
        livro.disponivel = not emprestado
    print("\nDisponibilidade dos livros atualizada com base nos empréstimos.\n")
        
def atualizar_dados_utilizador(utilizadores):
    listar_utilizadores(utilizadores)
    id_u = int(input("ID do utilizador a atualizar: "))
    if 0 <= id_u < len(utilizadores):
        utilizadores[id_u].nome = input("Novo nome: ")
        utilizadores[id_u].contato = int(input("Novo contato: "))
        print("Utilizador atualizado com sucesso!")
    else:
        print("ID inválido.")
        
def atualizar_dados_emprestimo(emprestimos, livros, utilizadores):
    listar_emprestimos(emprestimos, livros, utilizadores)
    idx = int(input("Número do empréstimo a atualizar (posição na lista): "))
    if 0 <= idx < len(emprestimos):
        id_l = int(input("Novo ID do livro: "))
        id_u = int(input("Novo ID do utilizador: "))
        data = input("Nova data de empréstimo (dd/mm/aaaa): ")
        previsão_devo = input("Nova data prevista de devolução (dd/mm/aaaa): ")
        if id_l < len(livros) and id_u < len(utilizadores):
            emprestimos[idx].id_livro = id_l
            emprestimos[idx].id_utilizador = id_u
            emprestimos[idx].data_emprestimo = data
            emprestimos[idx].data_prevista_devolucao = previsão_devo
            print("Dados do empréstimo atualizados!")
        else:
            print("IDs inválidos.")
    else:
        print("Índice inválido.")
        
def atualizar_dados_devolucao(emprestimos, livros):
    listar_emprestimos(emprestimos, livros, [])
    idx = int(input("Número do empréstimo a atualizar devolução: "))
    if 0 <= idx < len(emprestimos):
        if emprestimos[idx].data_devolucao != "-":
            nova_data = input("Nova data de devolução (dd/mm/aaaa): ")
            emprestimos[idx].data_devolucao = nova_data
            print("Data de devolução atualizada.")
        else:
            print("Este empréstimo ainda não foi devolvido.")
    else:
        print("Índice inválido.")
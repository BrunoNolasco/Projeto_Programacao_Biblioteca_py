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
            
            
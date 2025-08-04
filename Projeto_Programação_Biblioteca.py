from docx import Document
import os

def registar_livros(livros):
    n = int(input("Quantos livros deseja registrar? "))
    for _ in range(n):
        nome = input("Nome do livro: ")
        autor = input(f"Autor do livro {nome}: ")
        ano = int(input("Ano de publicação: "))
        livros.append(Livro(nome, autor, ano))
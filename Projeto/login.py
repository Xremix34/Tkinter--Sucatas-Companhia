import os
from tkinter import *
from tkinter import messagebox
import csv
import sys
#  FUNÇÃO QUE CARREGA TODO O LAYOUT DO PROGRAMA CASO QUEIRA SER UTILIZADO EM OUTRO FICHEIRO.PY
def mostra_toda_interface():

# FUNÇÃO QUE VERIFICA DO FICHEIRO SE O UTILIZADOR E PASSWORD SÃO VÁLIDOS
    def login():
        utilizador = utilizador_entry.get()
        password = password_entry.get()

        with open('funcionarios.csv', 'r') as f:
            csvreader = csv.reader(f, delimiter=',')
            for linha in csvreader:
                if utilizador == linha[0] and password == linha[1]:
                    boas_vindas = Label(text='Seja Bem Vindo!', bg='#333333', fg='#FFFFFF')
                    boas_vindas.pack()
                    messagebox.showinfo(title='Login com sucesso', message='Voçê foi conectado')
                    quadro.destroy()
                    janela1.destroy()
                    break
            else:
                messagebox.showerror(title='Erro', message='O Utilizador ou Password são inválidos!')

    ficheiro = 'funcionarios.csv'
    lista=[]

    janela1 = Tk()
    janela1.iconbitmap(bitmap='carro.ico')
    janela1.title('Sucatas & Companhia ')
    janela1.resizable(width=False, height=False)
    #   DIMENSÕES DA JANELA
    largura = 1366
    altura = 768
    largura_janela = janela1.winfo_screenwidth()
    altura_janela = janela1.winfo_screenheight()

    #   RESOLUÇÂO DO ECRA DO MONITOR
    posx = largura_janela / 2 - largura / 2
    posy = altura_janela / 2 - altura / 2
    janela1.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

    janela1.configure(bg='#333333')

    quadro = Frame(bg='#333333')
    quadro.pack(pady=100)

    #   CRIAÇÃO DOS WIDGETS
    slogan = Label(quadro, text='SUCATAS & COMPANHA', bg='#333333', fg='#FFFFFF', font=('Arial', 20))
    texto_login_label = Label(quadro, text='Login', bg='#333333', fg='#FFFFFF', font=('Arial', 30))
    larga_img = PhotoImage(file='carro.png')
    img = larga_img.subsample(2, 2)
    foto = Label(quadro, image=img, bg='#333333', width=10, height=150)
    utilizador_label = Label(quadro, text='Utilizador', bg='#333333', fg='#FFFFFF', font=('Arial', 16))
    utilizador_entry = Entry(quadro, width=50)
    password_label = Label(quadro, text='Password', bg='#333333', fg='#FFFFFF', font=('Arial', 16))
    password_entry = Entry(quadro, show='*', width=50)
    login_button = Button(quadro, text='Entrar', bg='#FF3399', fg='#FFFFFF', font=('Arial', 10), command=login, width=6)
    cancelar_button = Button(quadro, text='Cancelar', bg='#FF3399', fg='#FFFFFF', font=('Arial', 10), command=sair)

    #   POSIÇÕES DOS WIDGETS NO ECRA
    slogan.grid(row=0, column=0, columnspan=2, sticky='swe', pady=10)
    foto.grid(row=1, column=0, columnspan=2, sticky='wne')
    texto_login_label.grid(row=2, column=0, columnspan=2, sticky='news', pady=20)
    utilizador_label.grid(row=3, column=1)
    utilizador_entry.grid(row=4, column=1, pady=20)
    password_label.grid(row=5, column=1)
    password_entry.grid(row=6, column=1, pady=20)
    login_button.grid(row=7, column=0, columnspan=2, sticky='w', padx=80)
    cancelar_button.grid(row=7, column=1, columnspan=2, sticky='e', padx=80)


    abrir_ficheiros(ficheiro, lista)

    janela1.mainloop()

#   fUNÇÃO RESPONSÁVEL POR ABRIR O FICHEIRO COM OS FUNCIONÁRIOS
def abrir_ficheiros(ficheiro, lista):
    with open(ficheiro, 'r') as fich:
        for linhas in fich:
            linhas = linhas.rstrip().split(', ')
            lista.append(linhas)
        # print(linhas)
    return lista
    # print(lista_funcionarios)

def sair():
    sys.exit()


#função para iterar linhas
 # with open('funcionarios.csv', mode='r') as f:
        #     dados = csv.reader(f, delimiter=',')
        #     for linha in dados:
        #         lista_dados.append(linha)
        #
        #     for index, linha in enumerate(lista_dados, 1):
        #         mensagem_de_erro(utilizador,linha, password, quadro, janela1)
        #         break

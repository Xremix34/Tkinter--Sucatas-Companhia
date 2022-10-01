'''
Autor: Elio Borges

NOTA: Os dados inseridos no ficheiro CSV são todos ficticios para testes por isso foi desabilitado a verificação para esse feito por isso no caso de invalidação do nif,
      utilizar nifs verdadeiros ou criar novos registros pois a verificação está activa.
      No ficheiro csv após o primeiro registro terá de ir manualmento retirar o primeiro espaço criado para não dar erro do tamanho.
'''


from datetime import datetime
import time
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from datetime import date
import csv
import string
from random import choice
from time import sleep
import validador
import login
import os

data_hora_atual = datetime.today()
data_hora ='{}'.format(data_hora_atual.strftime('%m-%d-%Y %H:%M:%S'))
print(data_hora)


def actualizar_treeview():
    for i in tree.get_children():
       tree.delete(i)



#   FUNÇÃO QUE ABRE O FICHEIRO EM CSV NO MODO ESCRITA
def escrever_remover_ficheiros_csv(linha):

    with open('visitantes.csv', 'w+', encoding='utf-8' ) as csv_ficheiro:
        writer = csv.writer(csv_ficheiro, lineterminator='\n')
        writer.writerows(linha)



#   FUNÇAO QUE ABRE O FICHEIRO O FICHEIRO EM MODO ESCRITA E ESCREVE UMA NOVA LINHA SEM APAGAR AS RESTANTES
def escrever_ficheiros_csv(lista):
    with open('visitantes.csv', 'a+', encoding='utf-8') as csv_ficheiro:
        csv_ficheiro.write(','.join(lista)+'\n')


#   FUNÇÃO QUE LÊ OS DADOS DO FICHEIRO CSV EM MODO LEITURA
def ler_dados_csv(dados):
        with open('visitantes.csv', mode='r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            for d in reader:
                dados.append(d)
            #tree.insert('', END, values=dados)

        return dados


#FUNÇÃO QUE ADICIONA OS NOVOS DADOS INSERIDOS PELO UTILIZADOR
def adicionar_dados():
    lista_dados = []

    nome = nome_entry.get()
    morada = morada_entry.get()
    nif = nif_entry.get()
    telefone = telefone_entry.get()
    cod_bilhete = str(gera_codigo_bilhete())
    data_entrada = str(data_hora)
    data_saida = str('-')

    if not nome_entry.get() or not morada_entry.get() or not nif_entry.get() or not telefone_entry.get() and codigo_bilhete_entry.get() != '':
        messagebox.showerror('Erro','Deve preencher tooos os campos!')
        lista_dados.clear()
    elif validador.controlNIF(nif) == False:
        messagebox.showerror('Erro', 'O Nº Identificação Fiscal é invalido!')

    elif len(telefone) != 8 and len(telefone) != 9:
        messagebox.showerror('Erro', 'O Nº de telefone é inválido!')
    else:


        lista_dados.append(nome)
        lista_dados.append(morada)
        lista_dados.append(nif)
        lista_dados.append(telefone)
        lista_dados.append(cod_bilhete)
        lista_dados.append(data_entrada)
        lista_dados.append(data_saida)


        data_entrada_entry.insert(0, data_entrada)
        data_saida_entry.insert(0, data_saida)
        tree.insert('', END, values=lista_dados)


        limpar_campos()

        escrever_ficheiros_csv(lista_dados)


#   FUNÇÃO QUE ELIMINA OS DADOS SELECIONADOS
def eliminar_dados():

    if not nome_entry.get() or not morada_entry.get() or not nif_entry.get() or not telefone_entry.get():
        messagebox.showerror('Erro','Não existem dados a serem eliminados!')
    else:
        dados_a_eliminar = list()
        codigo = codigo_bilhete_entry.get()

        with open('visitantes.csv', 'r', encoding='utf-8') as file:
            writer = csv.reader(file)

            for line in writer:
                dados_a_eliminar.append(line)
                for i in line:
                    if i == codigo:
                        dados_a_eliminar.remove(line)

        with open('visitantes.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file,  lineterminator='\n')
            writer.writerows(dados_a_eliminar)

    limpar_campos()


# FUNÇÃO QUE GERA O ID DO BILHETE
def gera_codigo_bilhete():
    caracteres = string.ascii_uppercase + string.digits
    tamanho = 2
    return ''.join(choice(caracteres) for x in range(tamanho))

#   FUNÇÃO QUE MOSTRA O ESTADOS CAMPOS DE INSERÇÃO NORMAIS
def mostra_estados():
    mostra_codigo_bilhete_label.config(state='normal')
    mostra_codigo_bilhete_entry.config(state='normal')

    entrada_button.config(state='normal')
    saida_button.config(state='normal')

    data_entrada_label.config(state='normal')
    data_entrada_entry.config(state='normal')
    data_saida_label.config(state='normal')
    data_saida_entry.config(state='normal')

#   FUNÇÃO QUE DESABILITA OS ESTADOS DOS CAMPOS DE INSERÇÃO
def esconde_estados():
    mostra_codigo_bilhete_label.config(state='disabled')
    mostra_codigo_bilhete_entry.config(state='disabled')

    entrada_button.config(state='disabled')
    saida_button.config(state='disabled')

    data_entrada_entry.config(state='disabled')
    data_saida_entry.config(state='disabled')

# FUNÇÃO QUE VERIFICA SE O CODIGO DO BILHETE COINCIDE COM O DO FICHEIRO E RETORNA OS DADOS NOS CAMPOS DE INSERÇÃO
def verificar_codigo_bilhete():
    if not codigo_bilhete_entry.get():
        messagebox.showerror('Erro','Nenhum Bilhete ainda foi inserido!!')
        codigo_bilhete_entry.delete(0, END)
        limpar_campos()
    else:
        limpar_campos()
        mostra_estados()
        codigo = codigo_bilhete_entry.get()

        for index, linha in enumerate(dados,1):
            if codigo in linha:
                messagebox.showinfo('Bilhete', 'Acesso OK!')
                mostrar_valores(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5],linha[6])
                print(f'O código esta na linha {linha[1]}')
                codigo_bilhete_entry.delete(0, END)
                break



#  FUNÇÃO MOSTRA OS VALORES NOS CAMPOS DE INSERÇÃO
def mostrar_valores(nome,morada,nif,telefone,mostra_codigo_bilhete,data_entrada,data_saida):
    nome_entry.insert(0, nome)
    morada_entry.insert(0,morada)
    nif_entry.insert(0, nif)
    telefone_entry.insert(0, telefone)
    mostra_codigo_bilhete_entry.insert(0, mostra_codigo_bilhete)
    data_entrada_entry.insert(0, data_entrada)
    data_saida_entry.insert(0, data_saida)

# FUNÇÃO QUE PEGA OS DADOS E DEPOIS DE SEREM EDITADOS GRAVA DE NOVO NO FICHEIRO
def editar_dados():
    lista_dados = []
    d = list()
    global data_nao_modificada
    data_nao_modificada = []
    nome = nome_entry.get()
    morada = morada_entry.get()
    nif = nif_entry.get()
    # verificar_nif(nif, lista_dados,d)
    telefone = telefone_entry.get()
    # verificar_numero_telefone(telefone, lista_dados, d)
    cod_bilhete = str(mostra_codigo_bilhete_entry.get())
    data_entrada = str(data_entrada_entry.get())
    data_saida = str(data_saida_entry.get())

    if not nome_entry.get() or not morada_entry.get() or not nif_entry.get() or not telefone_entry.get() and codigo_bilhete_entry.get() != '':
        messagebox.showerror('Erro', 'Deve preencher tooos os campos!')
        lista_dados.clear()
    elif validador.controlNIF(nif) == False:
        messagebox.showerror('Erro', 'O Nº Identificação Fiscal é invalido!')
        lista_dados.clear()
    elif len(telefone) != 8 and len(telefone) != 9:
        messagebox.showerror('Erro', 'O Nº de telefone é inválido!')
        lista_dados.clear()
    else:
        lista_dados.append(nome)
        lista_dados.append(morada)
        lista_dados.append(nif)
        lista_dados.append(telefone)
        lista_dados.append(cod_bilhete)
        lista_dados.append(data_entrada)
        lista_dados.append(data_saida)
        #print(lista_dados)



        with open('visitantes.csv', 'r', encoding='utf-8') as file:
            writer = csv.reader(file)

            codigo = codigo_bilhete_entry.get()

            for linha in writer:
                d.append(linha)
                for i in linha:
                    if i == codigo:
                        d.remove(linha)
                        #print(lista_dados)
                        break

        with open('visitantes.csv', 'w+', encoding='utf-8') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerows(d)

            escrever_ficheiros_csv(lista_dados)
            tree.insert('', END, values=lista_dados)
            limpar_campos()

# FUNÇÃI QUE LIMPA TODOS OS CAMPOS DE INSERÇÃO
def limpar_campos():
        nome_entry.delete(0, END)
        morada_entry.delete(0, END)
        nif_entry.delete(0, END)
        telefone_entry.delete(0, END)
        mostra_codigo_bilhete_entry.delete(0, END)
        data_entrada_entry.delete(0, END)
        data_saida_entry.delete(0, END)


#   FUNÇÃO QUE PEGA A DATA ATUAL E ACTUALIZA NO FICHEIRO
def entrada_codigo_bilhete():
    lista_dados = []
    if not nome_entry.get() or not morada_entry.get() or not nif_entry.get() or not telefone_entry.get():
        messagebox.showerror('Erro','Ainda não foi verificado nenhum bilhete!')
        lista_dados.clear()
    else:
        nome = nome_entry.get()
        morada = morada_entry.get()
        nif = nif_entry.get()
        telefone = telefone_entry.get()
        cod_bilhete = str(gera_codigo_bilhete())
        data_entrada = str(data_hora)
        data_saida = str('-')
        lista_dados.append(nome)
        lista_dados.append(morada)
        lista_dados.append(nif)
        lista_dados.append(telefone)
        lista_dados.append(cod_bilhete)
        lista_dados.append(data_entrada)
        lista_dados.append(data_saida)

        d = list()

        with open('visitantes.csv', 'r', encoding='utf-8') as file:
            writer = csv.reader(file)

            codigo = codigo_bilhete_entry.get()

            for linha in writer:
                d.append(linha)
                for i in linha:
                    if i == codigo:
                        d.remove(linha)
                        print(lista_dados)
                        break


        with open('visitantes.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerows(d)



        escrever_ficheiros_csv(lista_dados)
        tree.insert('', END, values=lista_dados)
        data_saida_entry.insert(0, data_saida)


#   FUNÇÃO QUE PEGA A DATA ATUAL E ACTUALIZA NO FICHEIRO
def saida_codigo_bilhete():
    lista_dados = []

    if not nome_entry.get() or not morada_entry.get() or not nif_entry.get() or not telefone_entry.get():
        messagebox.showerror('Erro','Ainda não foi verificado nenhum bilhete!')
        lista_dados.clear()
    else:
        nome = nome_entry.get()
        morada = morada_entry.get()
        nif = nif_entry.get()
        telefone = telefone_entry.get()
        cod_bilhete = str(mostra_codigo_bilhete_entry.get())
        data_entrada = str(data_entrada_entry.get())
        data_saida = str(data_hora)
        lista_dados.append(nome)
        lista_dados.append(morada)
        lista_dados.append(nif)
        lista_dados.append(telefone)
        lista_dados.append(cod_bilhete)
        lista_dados.append(data_entrada)
        lista_dados.append(data_saida)

        d = list()

        with open('visitantes.csv', 'r', encoding='utf-8') as file:
            writer = csv.reader(file)

            codigo = codigo_bilhete_entry.get()

            for linha in writer:
                d.append(linha)
                for i in linha:
                    if i == codigo:
                        d.remove(linha)
                        print(lista_dados)
                        break

        with open('visitantes.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerows(d)

        data_saida_entry.insert(0, data_saida)

        escrever_ficheiros_csv(lista_dados)

        tree.insert('', END, values=lista_dados)

        limpar_campos()



# FUNÇÃO QUE MOSTRA TODOS OS DADOS DO FICHERIO
def interface_tree(data):
    quadro_treeview = Frame(width=60, height=60)
    quadro_treeview.pack(expand=YES, fill=Y)
    #style = ttk.Style()
    #style.configure("mystyle.Treeview.Heading", font=('Calibri', 12, 'bold'))
    global tree
    tree = ttk.Treeview(master=quadro_treeview, columns=("Nome", "Morada", "Nº Identificação Fiscal", "Nº Telefone", 'Código Bilhete','Data Entrada', 'Data Saida'), selectmode="extended")
    tree.pack(padx=1, pady=1, expand=YES, fill=Y, side=RIGHT)
    tree.heading('Nome', text="Nome", anchor=N)
    tree.heading('Morada', text="Morada", anchor=N)
    tree.heading('Nº Identificação Fiscal', text="Nº Identificação Fiscal", anchor=N)
    tree.heading('Nº Telefone', text="Nº Telefone", anchor=N)
    tree.heading('Código Bilhete', text="Código Bilhete", anchor=N)
    tree.heading('Data Entrada', text="Data Entrada", anchor=N)
    tree.heading('Data Saida', text="Data Saida", anchor=N)
    tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=N)
    tree.column('#1', stretch=NO, minwidth=0, width=120, anchor=N)
    tree.column('#2', stretch=NO, minwidth=0, width=120, anchor=N)
    tree.column('#3', stretch=NO, minwidth=0, width=130, anchor=N)
    tree.column('#4', stretch=NO, minwidth=0, width=120, anchor=N)
    tree.column('#5', stretch=NO, minwidth=0, width=120, anchor=N)
    tree.column('#6', stretch=NO, minwidth=0, width=120, anchor=N)
    tree.column('#7', stretch=NO, minwidth=0, width=120, anchor=N)

    for i in tree.get_children():
        tree.delete(i)

    for linhas in ler_dados_csv(dados):
        data.append(linhas)

    for linhas in data:
        #print(rows)
        tree.insert('','end',values=linhas)

    tree.mainloop()
    return data


if __name__ == '__main__':

    login.mostra_toda_interface()

    data = []
    dados = []
    janela = Tk()

    janela.iconbitmap(bitmap='carro.ico')
    janela.title('Sucatas & Companhia ')
    janela.resizable(width=False, height=False)
    #   DIMENSÕES DA JANELA
    largura = 1366
    altura = 768
    largura_janela = janela.winfo_screenwidth()
    altura_janela = janela.winfo_screenheight()

    #   RESOLUÇÂO DO ECRA DO MONITOR
    posx = largura_janela / 2 - largura / 2
    posy = altura_janela / 2 - altura / 2
    janela.geometry('%dx%d+%d+%d' %(largura, altura, posx, posy))
    janela.configure(bg='#333333')

    quadro = Frame( bg='#333333')

    nome = StringVar()
    morada = StringVar()
    nif = StringVar()
    telefone = StringVar()
    mostra_cod_bilhete = StringVar()
    cod_bilhete = StringVar()
    data_entrada = StringVar()
    data_saida = StringVar()



    #   CRIAÇÃO DOS WIDGETS
    slogan = Label(quadro, text='SUCATAS & COMPANHA', bg='#333333', fg='#FFFFFF', font=('Arial', 20))
    larga_img = PhotoImage(file='carro.png')
    img = larga_img.subsample(2,2)
    foto = Label(quadro, image=img, bg='#333333', width=10, height=150)
    texto_label = Label(quadro, text='DADOS DE ENTRADA', bg='#333333', fg='#FFFFFF', font=('Arial', 20))
    nome_label = Label(quadro, text='Nome:', bg='#333333', fg='#FFFFFF', font=('Arial', 14))
    nome_entry = Entry(quadro, textvariable=nome, width=40)
    morada_label = Label(quadro, text='Morada:', bg='#333333', fg='#FFFFFF', font=('Arial', 14))
    morada_entry = Entry(quadro, textvariable=morada, width=40)
    nif_label = Label(quadro, text='Nº de Indentificação:', bg='#333333', fg='#FFFFFF', font=('Arial', 14))
    nif_entry = Entry(quadro, textvariable=nif, width=40)
    telefone_label = Label(quadro, text='Nº Telefone:', bg='#333333', fg='#FFFFFF', font=('Arial', 14))
    telefone_entry = Entry(quadro, textvariable=telefone, width=40)
    mostra_codigo_bilhete_label = Label(quadro, text='Nº do Bilhete:', bg='#333333', fg='#FFFFFF', font=('Arial', 14))
    mostra_codigo_bilhete_entry = Entry(quadro, textvariable=mostra_cod_bilhete, width=40)
    mostra_codigo_bilhete_label.config(state='disabled', highlightbackground='#333333')
    mostra_codigo_bilhete_entry.config(state='disabled')

    data_entrada_label = Label(quadro, text='Data de Entrada:', bg='#333333', fg='#FFFFFF', font=('Arial', 14), anchor=N)
    data_entrada_label.config(state='disabled')
    data_entrada_entry = Entry(quadro, textvariable=data_entrada, width=30)
    #data_entrada_entry.config(state='disabled')

    data_saida_label = Label(quadro, text='Data de Saida:', bg='#333333', fg='#FFFFFF', font=('Arial', 14), anchor=N)
    data_saida_label.config(state='disabled')
    data_saida_entry = Entry(quadro, textvariable=data_saida, width=30)
    #data_saida_entry.config(state='disabled')

    codigo_bilhete_label = Label(quadro, text='Nº do Bilhete:', bg='#333333', fg='#FFFFFF', font=('Arial', 14))
    codigo_bilhete_entry = Entry(quadro, textvariable=cod_bilhete, width=40)

    adicionar_button = Button(quadro, text='Adicionar', bg='#FF3399', fg='#FFFFFF', font=('Arial', 10), command=adicionar_dados)
    editar_button = Button(quadro, text='Editar', bg='#FF3399', fg='#FFFFFF', font=('Arial', 10), command=editar_dados)
    eliminar_button = Button(quadro, text='Eliminar', bg='#FF3399', fg='#FFFFFF', font=('Arial', 10), command=eliminar_dados)
    procurar_button = Button(quadro, text='Procurar', bg='#FF3399', fg='#FFFFFF', font=('Arial', 10), command=verificar_codigo_bilhete)

    entrada_button = Button(quadro, text='Entrada', bg='#FF3399', fg='#FFFFFF', font=('Arial', 10), command=entrada_codigo_bilhete)
    entrada_button.config(state='disabled')
    saida_button = Button(quadro, text='Saida', bg='#FF3399', fg='#FFFFFF', font=('Arial', 10),command=saida_codigo_bilhete)
    saida_button.config(state='disabled')

    #atualizar_tree = Button(command=actualizar_treeview)
    #atualizar_tree.pack()

    #   POSIÇÕES DOS WIDGETS NO ECRA
    slogan.grid(row=1, column=0, columnspan=2, sticky='swe')
    foto.grid(row=2, column=0, columnspan=2, sticky='wne')
    texto_label.grid(row=3, column=0, columnspan=2, sticky='swe')
    nome_label.grid(row=4, column=0, pady=10, sticky='w')
    nome_entry.grid(row=4, column=1, sticky='w')
    morada_label.grid(row=5, column=0,  pady=10, sticky='w')
    morada_entry.grid(row=5, column=1, sticky='w')
    nif_label.grid(row=6, column=0, pady=10, sticky='w')
    nif_entry.grid(row=6, column=1, sticky='w')
    telefone_label.grid(row=7, column=0, pady=10, sticky='w')
    telefone_entry.grid(row=7, column=1, sticky='w')
    mostra_codigo_bilhete_label.grid(row=8, column=0, pady=10, sticky='w')
    mostra_codigo_bilhete_entry.grid(row=8, column=1, sticky='w', pady=10)

    data_entrada_label.grid(row=11, column=0, pady=10, sticky='n')
    data_entrada_entry.grid(row=12, column=0, columnspan=2, sticky='swe', pady=10)

    data_saida_label.grid(row=11, column=1, pady=10, sticky='n')
    data_saida_entry.grid(row=12, column=1, columnspan=2, sticky='swe', pady=10)

    codigo_bilhete_label.grid(row=19, column=0, pady=10, sticky='swe')
    codigo_bilhete_entry.grid(row=20, column=0, sticky='swe', pady=10)

    adicionar_button.grid(row=9, column=1, sticky='w',padx=20)
    eliminar_button.grid(row=9, column=1, sticky='e', padx=15)
    editar_button.grid(row=9, column=1, sticky='e', padx=92)
    procurar_button.grid(row=20, column=1, sticky='w')

    entrada_button.grid(row=18, column=0, sticky='n')
    saida_button.grid(row=18, column=1, sticky='n')

    quadro.pack(fill=Y,side=LEFT, padx=10)
    #ler_dados_csv(dados)
    interface_tree(data)

    janela.mainloop()




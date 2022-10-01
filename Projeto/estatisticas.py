from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import pandas
import matplotlib.pyplot as plt
import numpy as np
import csv

def mostra_interface_estatisticas():
    contador_entradas = 0
    contador_saidas = 0
    contador = 0
    data_entrada = 'YYYY-MM-DD'
    lista=[]
    tamanho_lista = len(lista)
    with open('visitantes.csv', 'r') as f:
        csvreader = csv.reader(f, delimiter=',')

        for texto in csvreader:
            lista.append(texto)

    while contador < tamanho_lista:
        if data_entrada == tamanho_lista[contador]:
            contador_entradas += 1
            contador += 1
        else:
            contador_saidas +=1
            contador +=1
    #print(data_entrada)
    print(contador_entradas)
    print(contador_saidas)




    df = pandas.DataFrame(dict(graph=['Bilhetes de Entrada', 'Bilhetes de Saida'],
                               n=[3, 5], m=[6, 1]))

    ind = np.arange(len(df))
    width = 0.4

    fig, ax = plt.subplots()
    ax.barh(ind, df.n, width, color='red', label='N')
    ax.barh(ind + width, df.m, width, color='green', label='M')

    ax.set(yticks=ind + width, yticklabels=df.graph, ylim=[2 * width - 1, len(df)])
    ax.legend()

    plt.show()


mostra_interface_estatisticas()
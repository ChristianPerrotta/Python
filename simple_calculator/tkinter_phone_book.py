# code and UI uses Portuguese instead of English
# simple phone book with tkinter GUI

import tkinter as tk
from tkinter import ttk

def cadastrar():
    #abre o arquivo (ou cria um novo, caso não exista) para ler e adicionar sempre ao final
    with open("fileLog.txt", "a") as log:
        nome = en_nome.get()
        telefone = en_numero.get()
        log.write(f"{nome}: {telefone}\n")
        
def consultar():
    with open("fileLog.txt", "r") as log:
        log_text = log.read()
        agenda = "AGENDA DE CONTATOS\n\n" + log_text
        nlines = log_text.count(':')
        window_height = str(200 + nlines*15)
        print(window_height)
        main.geometry("450x" + window_height)
        lb_agenda.config(text=agenda)

PADX = 5
PADY = 5

main = tk.Tk()
main.title("Lista Telefônica")
main.geometry("450x200")

root = tk.Frame(main)
root.pack(padx=PADX, pady=PADY)

lb_titulo = ttk.Label(root, text="Lista Telefônica")
lb_titulo.grid(row=0, column=0, columnspan=2, sticky=tk.N, padx=PADX, pady=PADY)

lb_novo_contato = ttk.Label(root, text="Novo Contato:")
lb_novo_contato.grid(row=1, column=0, sticky=tk.E, padx=PADX, pady=PADY)

en_nome = ttk.Entry(root, width="50")
en_nome.grid(row=1, column=1, sticky=tk.E, padx=PADX, pady=PADY)

lb_novo_numero = ttk.Label(root, text="Telefone:")
lb_novo_numero.grid(row=2, column=0, sticky=tk.E, padx=PADX, pady=PADY)

en_numero = ttk.Entry(root, width="50")
en_numero.grid(row=2, column=1, sticky=tk.E, padx=PADX, pady=PADY)

fr2 = tk.Frame(main)
fr2.pack(padx=PADX, pady=PADY)

bt_add = ttk.Button(fr2, text="Cadastrar", command=cadastrar)
bt_add.grid(row=0, column=0, sticky=tk.N, padx=PADX, pady=PADY)

bt_consult = ttk.Button(fr2, text="Consultar", command=consultar)
bt_consult.grid(row=0, column=1, sticky=tk.N, padx=PADX, pady=PADY)

lb_agenda = ttk.Label(fr2, text="")
lb_agenda.grid(row=1, column=0, columnspan=2, sticky=tk.N, padx=PADX, pady=PADY)

main.mainloop()
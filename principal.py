from tkinter import *
from datetime import datetime

janela = Tk()
janela.title("Router")


def salvar_dados():
    f = open("pedidos.txt", "a")
    f.write(f"Cliente: {nome.get()}\n")
    f.write(f"Operador: {oper.get()}\n")
    f.write(f"SN: {observacao.get()}\n")
    f.write(f"Router: {Router.get()}\n")
    f.write(f"MAC: {mac.get()}\n")
    f.write(f"Unidade: {unidade.get()}\n")
    f.write(f"Boot: {boot.get()}\n")
    f.write(f"Chassi: {chassi.get()}\n")
    f.write(f"Lan: {lan.get()}\n")
    f.write(f"Label: {label.get()}\n")
    f.write(f"WIFI 2.4: {wifidois.get()}\n")
    f.write(f"WIFI 5: {wificinco.get()}\n")
    f.write(f"Format Reset: {reset.get()}\n")

    now = datetime.now()
    date_time = now.strftime("%d%m%Y, %H&M%S")

    arquivo = open('pedidos.txt', 'a')
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    arquivo.write(date_time + "\n")
    arquivo.close()
    f.write(f"-----------------\n")

    # nome.set("Araras")
    nome.delete(0, END)
    observacao.delete(0, END)
    Router.delete(0, END)
    mac.delete(0, END)
    f.close()


def ler_arq(arquivo):
    leit1 = []
    f = open(arquivo, encoding="utf8")
    for linha in f: leit1.append(linha.rstrip())
    f.close()
    leit1.sort()
    return leit1


pedido_txt = "pedidos.txt"
operador = "Escolha a operadora"
decisoes = "Sim/Não"

p1 = Label(janela, text="Operador: ").pack()
oper = StringVar()
oper.set(operador)

op1 = ler_arq("operadora.txt")
OptionMenu(janela, oper, p1, *op1).pack()

n = Label(janela, text="Cliente: ").pack()
nome = Entry(janela)
nome.pack()

obs = Label(janela, text="Sn: ").pack()
observacao = Entry(janela)
observacao.pack()

Router = Label(janela, text="Router: ").pack()
Router = Entry(janela)
Router.pack()

mac = Label(janela, text="Mac: ").pack()
mac = Entry(janela)
mac.pack()

p1 = Label(janela, text="Unidade? ").pack()
unidade = StringVar()
unidade.set(decisoes)

op1 = ler_arq("decisao.txt")
OptionMenu(janela, unidade, p1, op1).pack()

p1 = Label(janela, text="Boot? ").pack()
boot = StringVar()
boot.set(decisoes)

op1 = ler_arq("decisao.txt")
OptionMenu(janela, boot, p1,op1).pack()

p1 = Label(janela, text="Chassi? ").pack()
chassi = StringVar()
chassi.set(decisoes)

op1 = ler_arq("decisao.txt")
OptionMenu(janela, chassi, p1, op1).pack()

p1 = Label(janela, text="Lan? ").pack()
lan = StringVar()
lan.set(decisoes)

op1 = ler_arq("decisao.txt")
OptionMenu(janela, lan, p1,op1).pack()

p1 = Label(janela, text="Label? ").pack()
label = StringVar()
label.set(decisoes)

op1 = ler_arq("decisao.txt")
OptionMenu(janela, label, p1, op1).pack()

p1 = Label(janela, text="Wifi 2.4? ").pack()
wifidois = StringVar()
wifidois.set(decisoes)

op1 = ler_arq("decisao.txt")
OptionMenu(janela, wifidois, p1,op1).pack()

p1 = Label(janela, text="Wifi 5? ").pack()
wificinco = StringVar()
wificinco.set(decisoes)

op1 = ler_arq("decisao.txt")
OptionMenu(janela, wificinco, p1, op1).pack()

p1 = Label(janela, text="Format Reset? ").pack()
reset = StringVar()
reset.set(decisoes)

op1 = ler_arq("decisao.txt")
OptionMenu(janela, reset, p1,op1).pack()

sv = Button(janela, text="Salvar", command=salvar_dados)
sv.pack()

E = Text(janela)  # criamos o widget Text.
x = open("pedidos.txt", "r")  # função de abertura para ler
z = x.read()  # função ler, read
E.insert(0.0, z)  # aqui inserimos o texto dentro do widget Text.
E.pack()  # empacotanos o widget Text

janela.mainloop()
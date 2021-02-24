from tkinter import *
from tkinter import messagebox
import random

# cria o icone do jogo
root = Tk()
root.title('Jogo da memória')
root.geometry("500x550")

# numeros para serem encontrados
numeros = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]

# embaralhar os numeros que estão dentro do vetor
random.shuffle(numeros)

# Button frame(centralizar):
my_frame = Frame(root)
my_frame.pack(pady=50)

# função sair:


def exit():
    raise SystemExit()


# função para executar ao clicar no botao
count = 0
cont = 0
resp_list = []
resp_dict = {}


def button_click(b, number):
    global count, resp_list, resp_dict, cont

    if b["text"] == ' ' and count < 2:
        b["text"] = numeros[number]
        resp_list.append(number)
        resp_dict[b] = numeros[number]
        count += 1

    if len(resp_list) == 2:
        if numeros[resp_list[0]] == numeros[resp_list[1]]:
            my_label.config(
                text="--------------------------------------MATCH!!------------------------------------------")

            for key in resp_dict:
                key["state"] = "disabled"
                cont += 1

            count = 0
            resp_list = []
            resp_dict = {}

        else:

            my_label.config(
                text="--------------------------------------ERROOUU!!------------------------------------------")
            count = 0
            resp_list = []
            # Pop-up
            messagebox.showinfo("ERROOUU!!", "ERROOUU!!")

            for key in resp_dict:
                key["text"] = " "

            resp_dict = {}

        if cont == 12:
            messagebox.showinfo("GANHOU!!", "PARABÉNS, VOCÊ GANHOU!!")
            my_label.config(text="PARABÉNS, VOCÊ GANHOU!!")
            print("\n\n\n")

        my_label.config(
            text="-----------------------------------------------------------------------------------------")


# Definir os botões:
b0 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b0, 0))
b1 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b1, 1))
b2 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b2, 2))
b3 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b3, 3))
b4 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b4, 4))
b5 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b5, 5))
b6 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b6, 6))
b7 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b7, 7))
b8 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b8, 8))
b9 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
            width=6, command=lambda: button_click(b9, 9))
b10 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
             width=6, command=lambda: button_click(b10, 10))
b11 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3,
             width=6, command=lambda: button_click(b11, 11))

bexit = Button(my_frame, text='SAIR', font=(
    "Helvetica", 16), height=1, width=4, command=exit)


# Alinhar os botoes:
b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)


my_label = Label(root, text="")
my_label.pack(pady=20)
root.mainloop()

import requests
import json
from ttkthemes import *
from tkinter import * #
from tkinter import ttk #

class cnpj_consulta:

    def __init__(self):
        self.front_display();

    def consulta(self, cnpj_select):
        request = requests.get("https://api-publica.speedio.com.br/buscarcnpj?cnpj={}".format({cnpj_select}))
        retorno = json.loads(request.content)


        self.retorno_cosulta(retorno)



    def front_display(self):
        window = ThemedTk(theme='yaru')
        window.title('Cosultar CNPJ')
        window.resizable(0, 0)
        window.geometry("500x160+500+100")

        frame_title = Frame(window)
        frame_title.pack(fill='x', pady=25)

        title_text = Label(frame_title, text="Consulta CNPJ", font='Bahnschrift 25', fg="#050d47")
        title_text.pack()

        frame_main = Frame(window)
        frame_main.pack()

        cnpj_text = Label(frame_main, text=' CNPJ: ', font='Bahnschrift 10')
        cnpj_text.pack(side='left')

        cnpj_insert = ttk.Entry(frame_main, width=20)
        cnpj_insert.pack(side='left')

        btn_consultar = ttk.Button(frame_main, text="Consultar", command=lambda: self.consulta(cnpj_insert.get()))
        btn_consultar.pack(side='left', padx=10)


        window.mainloop()

    def retorno_cosulta(self, retorno_c):
        window = Toplevel()
        window.title('Retorno da consulta')
        window.resizable(0, 0)
        window.geometry("500x560+500+100")

        frame_retorno = Frame(window,)
        frame_retorno.pack(pady=50)

        for key, value in retorno_c.items():
            retorno = Label(frame_retorno, text="{} : {}".format(key, value))
            retorno.pack()

        window.mainloop()
cnpj_consulta()


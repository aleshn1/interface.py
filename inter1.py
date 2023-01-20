import layout

import PySimpleGUI as sg

layout = [
    [sg.Text("Nome")],
    [sg.InputText()],
    [sg.Text("Sobrenome")],
    [sg.InputText()],
    [sg.Text("Endereço")],
    [sg.InputText()],
    [sg.Text("Cidade")],
    [sg.InputText()],
    [sg.Text("Bairro")],
    [sg.InputText()],
    [sg.Text("E-mail")],
    [sg.InputText()],
    [sg.Text("Senha")],
    [sg.InputText()],
    [sg.Text("Confirma Senha")],
    [sg.InputText()],
    [sg.Button("Criar Cadastro"),sg.Button("Cancelar")],

]

janela = sg.Window("Sistema de Cadastro de Usuario",layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
janela.Close()
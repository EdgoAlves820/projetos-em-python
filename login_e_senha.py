from PySimpleGUI import PySimpleGUI as sg

# ---------------Layout---------------
sg.theme('Reddit')  # aonde sera escolhido o tema
layout = [
    [sg.Text('Usuário'), sg.Input(key='Usuário', size=(30, 1))],  # Aqui será criado o campo usuário
    [sg.Text('Senha'), sg.Input(key='Senha', password_char='*', size=(30, 1))],  # Aqui será criado o campo senha
    [sg.Checkbox('Salvar o Login?')],  # Um campo aonde será perguntado se quer salvar o login
    [sg.Button('Entrar')]  # Botão criado para acessar o login
]
# ---------------Janela---------------
janela = sg.Window('ADS - 2022 - Uninter', layout)  # Layout criado para ser acessado o login e senha
# ---------------Ler os eventos---------------
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuário'] == 'Uninter' and valores['Senha'] == '2022':  # Informação de Login e Senha
            print('Bem-Vindo ao grupo ADS - 2022 - Uninter!')  # Mensagem recebida depois do acesso com sucesso

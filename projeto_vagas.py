""" 1 Perguntar o nome da empresa que deseja que busque
    2 Iniciar o navegador e acessar o site da Gupy
    3 Iterar sobre as vagas e a cada vaga salvar as informações nas colunas do Excel

"""

import PySimpleGUI as sg 

def tela_inicial():

    if __name__ == "__main__":
        sg.change_look_and_feel('Gray Gray Gray')

        tamanho_botao = (15,2)
        tamanho_caixa = (10,5)

    
        layout = [
            
            [sg.Column([[sg.Text('Bem vindo a Automação de Buscas de buscar de vagas!',font=('Helvetica', 12 ,'bold'))]], justification='center')],
            [sg.Column([[sg.Text('Não esqueça de inserir os dados atualizados na planilha! ')]], justification='center')],
            [sg.Column([[sg.Text('Antes de começar, algumas orientações:',font=('Helvetica', 10, 'bold'))]], justification='center')],
            [sg.Text('')],
            [sg.Column([[sg.Text('Se você já conferiu todas as informações clique em EXECUTAR para prosseguir')]], justification='center')],
            [sg.Text('')],

            [
            sg.Column([[sg.Button('Executar', size=tamanho_botao, font=('Helvetica', 10, 'bold'))]], justification='center', element_justification='center'),
            #  sg.Column([[sg.Button('Reiniciar', size=tamanho_botao,font=('Helvetica', 10, 'bold'))]], justification='center', element_justification='center')]]
            ]]
        

        window = sg.Window('CNPJ',layout, size=(850, 450))

        while True: 
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            # elif event == 'Executar':
tela_inicial()

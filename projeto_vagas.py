""" 1 Perguntar o nome da empresa que deseja que busque
    2 Iniciar o navegador e acessar o site da Gupy
    3 Iterar sobre as vagas e a cada vaga salvar as informações nas colunas do Excel

"""

import PySimpleGUI as sg 
from botcity.web import WebBot, Browser, PageLoadStrategy
from botcity.web.browsers.chrome import default_options
from botcity.web import By


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


def config_navegacao():

    # Instantiate the WebBot.
    bot = WebBot()
    # Configure whether or not to run on headless mode.
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = "chromedriver.exe"
    download_folder_path = r'C:\Projetos Python\Projeto_Vagas\downloads'

    def_options = default_options(

        headless=bot.headless,
        download_folder_path=bot.download_folder_path,
        user_data_dir= None,  # Informing None here will generate a temporary directory
        page_load_strategy=PageLoadStrategy.NORMAL)
    
    # Opens the browser on the BotCity website.
    bot.browse("https://www.google.com/")

    # Import for the By enum.
                                      
    
    ## Abre o google
    pesquisa = bot.find_element("//textarea[@id='APjFqb']",By.XPATH)
    pesquisa.send_keys("PagSeguro gupy")

    bot.wait(5000)
    ## Pesquisa a empresa
    pesquisa = bot.find_element("//input[@name='btnK']",By.XPATH)
    pesquisa.click()
    ##Pesquisa google
    pesquisa = bot.find_element("#rso > div.hlcw0c > div > div > div > div > div > div > div > div.yuRUbf > div > span > a > h3",By.CSS_SELECTOR)
    pesquisa.click()





    
    
    
    
    

config_navegacao()







    




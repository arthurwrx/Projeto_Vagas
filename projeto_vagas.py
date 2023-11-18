""" 1 Perguntar o nome da empresa que deseja que busque
    2 Iniciar o navegador e acessar o site da Gupy
    3 Iterar sobre as vagas e a cada vaga salvar as informações nas colunas do Excel

"""

import PySimpleGUI as sg 
from botcity.web import WebBot, Browser, PageLoadStrategy
from botcity.web.browsers.chrome import default_options
from botcity.web import By
from selenium.common.exceptions import NoSuchElementException
import openpyxl 

nome_das_vagas = []
localidades_das_vagas = []
tipos_vagas = []
bot = WebBot()


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

    ## Pesquisa a empresa
    pesquisa = bot.find_element("//input[@name='btnK']",By.XPATH)
    bot.wait_for_element_visibility(element=pesquisa, visible=True, waiting_time=10000)
    pesquisa.click()

    ##Site Gupy
    pesquisa = bot.find_element("#rso > div.hlcw0c > div > div > div > div > div > div > div > div.yuRUbf > div > span > a > h3",By.CSS_SELECTOR)
    bot.wait_for_element_visibility(element=pesquisa, visible=True, waiting_time=10000)
    pesquisa.click()
    
    gupy = bot.find_element("#radix-3 > div.sc-fYaxgZ.kMYmhe > button",By.CSS_SELECTOR)
    gupy.click()

    gupy = bot.find_element("//*[@id='onetrust-accept-btn-handler']",By.XPATH)
    bot.wait_for_element_visibility(element=gupy, visible=True, waiting_time=10000)
    gupy.click() 



def captura_vagas(nome_das_vagas,localidades_das_vagas,tipos_vagas):
   
    i = 1
    while i < 11:
        
        nome_vaga_selector = f"#job-listing > ul > li:nth-child({str(i)}) > a > div > div.sc-d868c80d-5"
        local_vaga_selector = f"#job-listing > ul > li:nth-child({str(i)}) > a > div > div.sc-d868c80d-6"
        tipo_vaga_selector = f"#job-listing > ul > li:nth-child({str(i)}) > a > div > div.sc-d868c80d-7"

        try:
            nome_vaga = bot.find_element(nome_vaga_selector,By.CSS_SELECTOR)
            nome_da_vaga_string = nome_vaga.text
            nome_das_vagas.append(nome_da_vaga_string)
            
            local_vaga = bot.find_element(local_vaga_selector,By.CSS_SELECTOR)
            local_da_vaga_string = local_vaga.text
            localidades_das_vagas.append(local_da_vaga_string)

            tipo_vaga = bot.find_element(tipo_vaga_selector,By.CSS_SELECTOR)
            tipo_da_vaga = tipo_vaga.text
            tipos_vagas.append(tipo_da_vaga)
            i += 1

        except NoSuchElementException:
            break  # Sai do loop while se o elemento não for encontrado
    


config_navegacao()
captura_vagas(nome_das_vagas,localidades_das_vagas,tipos_vagas)







    




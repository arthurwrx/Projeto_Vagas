""" 1 Perguntar o nome da empresa que deseja que busque
    2 Iniciar o navegador e acessar o site da Gupy
    3 Iterar sobre as vagas e a cada vaga salvar as informações nas colunas do Excel
"""
##Dependências
import PySimpleGUI as sg 
from botcity.web import WebBot, Browser
from botcity.web import By
from selenium.common.exceptions import NoSuchElementException
import openpyxl
import datetime

### Variáveis Globais
nome_das_vagas = []
localidades_das_vagas = []
tipos_vagas = []
bot = WebBot()
hoje = str(datetime.datetime.now().strftime('%d.%m.%Y %Hh%Mm'))


##Controle da tela
def tela_inicial():

    if __name__ == "__main__":
        
        sg.change_look_and_feel('Gray Gray Gray')

        tamanho_botao = (15,2)
        tamanho_caixa = (10,5)

    
        layout = [
            [sg.Column([[sg.Image(r'C:\Projetos Python\Projeto_Vagas\Logo\logo-assinatura.png')]], justification='center')],
            [sg.Column([[sg.Text('Bem vindo a Automação de Buscas de Vagas Abertas!',font=('Helvetica', 12 ,'bold'))]], justification='center')],
            [sg.Column([[sg.Text('Antes de começar, digite o nome da empresa desejada:',font=('Helvetica', 10, 'bold'))]], justification='center')],
            [sg.Text('Empresa desejada: '), sg.InputText(key="nome_empresa")],
            [sg.Column([[sg.Text('Se você já escolheu a empresa, clique em EXECUTAR para prosseguir')]], justification='center')],
            [sg.Text('')],

            [
            sg.Column([[sg.Button('Executar', size=tamanho_botao, font=('Helvetica', 10, 'bold'))]], justification='center', element_justification='center'),
            #  sg.Column([[sg.Button('Reiniciar', size=tamanho_botao,font=('Helvetica', 10, 'bold'))]], justification='center', element_justification='center')]]
            ]]
        

        window = sg.Window('CNPJ',layout, size=(700, 350))
        

        while True: 
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            elif event == 'Executar':
                limpa_excel()
                window.close()
                nome_empresa = values['nome_empresa']
                config_navegacao(nome_empresa)
                captura_vagas()
                joga_no_excel(nome_empresa)
                tela_retorna_menu()

    return nome_empresa

## Função destinada a iniciar o navegador e entrar no site da gupy
def config_navegacao(nome_empresa):

    # Configure whether or not to run on headless mode.
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = "chromedriver.exe"
    download_folder_path = r'C:\Projetos Python\Projeto_Vagas\downloads'
    
    # Opens the browser on the BotCity website.
    
    bot.browse("https://www.google.com/")
                                      
    ## Abre o google
    pesquisa = bot.find_element("//textarea[@id='APjFqb']",By.XPATH)
    pesquisa.send_keys(f'{nome_empresa} gupy')

    ## Pesquisa a empresa
    pesquisa = bot.find_element("//input[@name='btnK']",By.XPATH)
    bot.wait_for_element_visibility(element=pesquisa, visible=True, waiting_time=10000)
    pesquisa.click()

    ##Site Gupy                  
    pesquisa = bot.find_element("#rso > div.hlcw0c > div > div > div > div > div > div > div > div.yuRUbf > div > span > a > div > div > div > cite",By.CSS_SELECTOR)
    bot.wait_for_element_visibility(element=pesquisa, visible=True, waiting_time=10000)
    pesquisa.click()
    
    try:
        gupy = bot.find_element("#radix-3 > div.sc-fYaxgZ.kMYmhe > button",By.CSS_SELECTOR)
        gupy.click()
    
    except:
        pass

    try:
        gupy = bot.find_element("//*[@id='onetrust-accept-btn-handler']",By.XPATH)
        bot.wait_for_element_visibility(element=gupy, visible=True, waiting_time=10000)
        gupy.click() 

    except:
        pass

## Função destinada a capturar os detalhes da vaga da empresa desejada
def captura_vagas():
   
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
    
    try: 
        proxima_pagina = bot.find_element("//button[@aria-label='Vá para próxima página']",By.XPATH)
        if proxima_pagina.is_enabled():
            proxima_pagina.click()
            captura_vagas()

    except:
        print("capturamos tudo")

## Função destinada a dispor as informações no excel
def joga_no_excel(nome_empresa):


    workbook = openpyxl.Workbook()
    sheet = workbook.active    

    sheet.append({'A': 'Nome da Vaga', 'B': 'Localidade', 'C': 'Tipo de Vaga'})
    
    for i in range(len(tipos_vagas)):
            sheet.append({
                'A':nome_das_vagas[i],
                'B':localidades_das_vagas[i],
                'C':tipos_vagas[i]
            })

    workbook.save(filename=f"{nome_empresa} {hoje}.xlsx")

## Função a limpar as listas do excel
def limpa_excel():
 
    global nome_das_vagas, localidades_das_vagas, tipos_vagas
    nome_das_vagas = []
    localidades_das_vagas = []
    tipos_vagas = []

## pergunta se o usuário quer fazer mais uma pesquisa
def tela_retorna_menu():

    if __name__ == "__main__":
        
        sg.change_look_and_feel('Gray Gray Gray')

        tamanho_botao = (15,2)
        tamanho_caixa = (10,5)

    
        layout = [
            
            [sg.Column([[sg.Text('Deseja consultar mais alguma empresa?',font=('Helvetica', 12 ,'bold'))]], justification='center')],
            [sg.Text('')],
            [
            sg.Column([[sg.Button('Sim', size=tamanho_botao, font=('Helvetica', 10, 'bold'))]], justification='center', element_justification='center'),
             sg.Column([[sg.Button('Não', size=tamanho_botao,font=('Helvetica', 10, 'bold'))]], justification='center', element_justification='center')]]
        

        window = sg.Window('CNPJ',layout, size=(700, 225))
        

        while True: 
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

            elif event == 'Sim':
                window.close()
                tela_inicial()
                

            elif event == 'Não':
                window.close()
                break
            
def busca_linkedin():


        bot.browse('https://www.linkedin.com/jobs/search?keywords=Cia%20de%20talentos&location=Brasil&geoId=106057199&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0')

        pesquisa_linkedin = bot.find_element('//*[@id="job-search-bar-keywords"]',By.XPATH)
        pesquisa_linkedin.clear()      
        pesquisa_linkedin.send_keys('Localiza&Co')

        bot.wait(3000)

        pesquisa_linkedin = bot.find_element("//*[@id='keywords-1']",By.XPATH)
        empresa_buscada = pesquisa_linkedin.text
        pesquisa_linkedin.click()

        print(empresa_buscada)

        filtro_linkedin = bot.find_element("//button[@aria-label='Filtro Empresa. Clicar neste botão exibe todas as opções de filtro de Empresa.']",By.XPATH)
        filtro_linkedin.click()

        lista_filtros_linkedin = bot.find_elements("//div[@aria-label='Opções de filtro de Empresa.']/div[@class='filter-values-container__filter-value']",By.XPATH)
        


        for i in range(len(lista_filtros_linkedin)):


            empresa_filtrada = lista_filtros_linkedin[i]
            lista_checkbox_linkedin = f"//*[@id='f_C-{str(i)}']"
            empresa_filtrada = empresa_filtrada.text
            empresa_tratada = empresa_filtrada.split("(", 1)[0].strip()
            print(empresa_tratada)

            if empresa_tratada == empresa_buscada:
                print(f"Condição satisfeita em: {empresa_tratada} {empresa_tratada}")
                seleciona_caixinha = bot.find_element(lista_checkbox_linkedin,By.XPATH)
                seleciona_caixinha.click()
                bot.wait(2000)
        clica_concluir = bot.find_element("//button[contains(text(), 'Concluído') and @class='filter__submit-button']",By.XPATH)
        clica_concluir.click()

        
        bot.wait(100000)


        



busca_linkedin()
# tela_inicial()









    




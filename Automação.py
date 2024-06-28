# PASSO A PASSO DO PROJETO:

# Passo 1: Entrar no Sistema da Empresa; 
    # Link do caso atual ->  ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    # PRINCIPAIS FUNÇÕES DO PYAUTOGUI: 
    # pyautogui.press -> aperta uma tecla
    # pyautogui.write -> escreve um texto
    # pyautogui.click -> clica em um local da tela 
    # pyautogui.hotkey -> pressiona uma combinação de teclas (Exemplo: pyautogui.hotkey("crtl", "t")  )
      
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.8 # Esse intervalo entre cada comando evita o atropelamento de etapas
# abrir o navegador  -> etapas dentro do Passo 1
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter") 
time.sleep(5) # Caso a internet demore ao carregar o link, esse intervalo será aplicado apenas nessa etapa

# Passo 2: Fazer Login;
# selecionar o campo de e-mail
pyautogui.click(x=675, y=367)
# escrever o e-mail
pyautogui.write("tecanedo@gmail.com")
pyautogui.press("tab") # passando para o próximo campo de preenchimento
pyautogui.write("MinhaSenha!!!")
pyautogui.click(x=701, y=527) # apertando botão de login
time.sleep(4)


# Passo 3: Importar base de produtos para cadastrar;
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar um produto;
linha = 0 # Toda tabela ou lista dentro do python começa pelo índice 0

# clicar no campo do código
for linha in tabela.index:  # index(índice) se refere a cada número das linhas da tabela utilizada
    pyautogui.click(x=604, y=238)
    # pegar da tabela o campo que desejamos preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))  # A função "str()" transforma o valor de uma variável em string
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("pgup")
# Passo 5: Repetir o Cadastro até o fim.



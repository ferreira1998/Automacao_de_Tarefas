   
   # passo a passo do projeto 



# passo 1 - entrar no sitema da empresa
   #https://dlp.hashtagtreinamentos.com/python/intensivao/login

#pip install pyautogui 
import pyautogui
import time
#/python/intensivao/login
pyautogui.PAUSE = 2

# Aperta a tecla do windowns 
pyautogui.press("win")
# digita o nome do programa 
pyautogui.write("chrome")
#apertar Enter
pyautogui.press("enter")
# digitar o link
link = "dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
# apertar enter
pyautogui.press("enter")

#esperar 5 segundos 
time.sleep(5)
# passo 2 - Fazer login 
pyautogui.click(x=2148, y=412)
# digitar email
pyautogui.write("wagner98@hotmail.com")
# passar para o campo de senha 
pyautogui.press("tab")
#digitar senha 
pyautogui.write("minha senha ")

pyautogui.click(x=2311, y=570)
time.sleep(3)
# passo 3 - Importar a base de Dados 
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
   # passo 4 - Cadastrar um produto
   pyautogui.click(x=2040, y=289)
   #codigo
   codigo = tabela.loc[linha, "codigo"]
   pyautogui.write(codigo)
   pyautogui.press("tab")
   #marca 
   pyautogui.write(tabela.loc[linha, "marca"])
   pyautogui.press("tab")
   #Tipo
   pyautogui.write(tabela.loc[linha, "tipo"])
   pyautogui.press("tab")
   #categoria 
   pyautogui.write(str(tabela.loc[linha, "categoria"]))
   pyautogui.press("tab")
   #preco
   pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
   pyautogui.press("tab")
   #custo
   pyautogui.write(str(tabela.loc[linha, "custo"])) 
   pyautogui.press("tab")
   #obs
   obs = tabela.loc[linha, "obs"]
   if not pandas.isna(obs):
      pyautogui.write(obs)     
   #eviar produto
   pyautogui.press("tab")
   pyautogui.press("enter")

   pyautogui.scroll(5000)     
# passo 5 - Repetir isso ate acabar a base de Dados 

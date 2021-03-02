# -*- coding: utf-8 -*-
import requests
import json
import datetime
import urllib
import telepot
import locale


bot2 = telepot.Bot('1680517574:AAGd9Jm7IVTV6Xt5CWQ58itbFoCk6FIYRMw')
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def requisicao(moeda):
   try:

    requisicao = requests.get('http://economia.awesomeapi.com.br/json/all/'+moeda.upper())

    cotacao = json.loads(requisicao.text)

    print('#### Cotação ####', datetime.datetime.now())
    print("Moeda: "+cotacao[moeda.upper()]['name'])
    print("Cotação: R$"+cotacao[moeda.upper()]['high'])
    print(cotacao[moeda.upper()]['pctChange'])
    valor = cotacao[moeda.upper()]['bid']
    return valor

   except:
       print("Moeda inválida!")
       return None
def requisicao2(moeda):
   try:

    requisicao2 = requests.get('http://economia.awesomeapi.com.br/json/all/'+moeda.upper())

    cotacao2 = json.loads(requisicao2.text)

    print('#### Cotação ####', datetime.datetime.now())
    print("Moeda: "+cotacao2[moeda.upper()]['name'])
    print("Cotação: R$"+cotacao2[moeda.upper()]['high']+"teste")
    name = cotacao2[moeda.upper()]['name']
    return name
   except:
       print("Moeda inválida!2")
       return None
def requisicao3(moeda):
   try:
       requisicao3 = requests.get('http://economia.awesomeapi.com.br/json/all/'+moeda.upper())
       cotacao3 = json.loads(requisicao3.text)
       variacao = cotacao3[moeda.upper()]['pctChange']
       return variacao
   except:
       print("Moeda inválida!3")
       return None
def Receive_msg(msg):
    print(msg['chat']['id'])
    print(msg['text'])
    print(msg['chat']['first_name'])
    print(msg)

    bot2.sendMessage(msg['chat']['id'],"Olá "+msg['chat']['first_name'])
    bot2.sendMessage(msg['chat']['id'],"Bem vindo ao BOT do Cambio!\nDigite o código da moeda que deseja obter a cotação: \n\nUSD    - (Dólar Comercial)\nUSDT - (Dólar Turismo)\nCAD   - (Dólar Canadense)\nAUD    - (Dólar Australiano)\nEUR    - (Euro)\nGBP    - (Libra Esterlina)\nARS    - (Peso Argentino)\nJPY    - (Iene Japonês)\nCHF    - (Franco Suíço)\nCNY    - (Yuan Chinês)\nYLS    - (Novo Shekel Israelense)\nBTC    - (Bitcoin)\nLTC    - (Litecoin)\nETH    - (Ethereum)\nXRP    - (Ripple)\n")

    moeda = requisicao2(msg['text'])
    valor = requisicao(msg['text'])
    variacao = requisicao3(msg['text'])
    print(variacao)
    if float(variacao) < 0:
        unicode_var = "\U0001F53B"
    elif float(variacao) > 0:
        unicode_var = "\U0001F53A"
    else:
        unicode_var = "U0001F539"
    firstName = msg['chat']['first_name']
    timenow = datetime.datetime.now().strftime("%A %d/%m/%Y às %H:%M")
    message = "#### Cotação ####\n"+str(timenow)+"\nCotação do "+moeda+": R$ "+str(round(float(valor),2))+"\nVariação: "+variacao+"% "+unicode_var
    bot2.sendMessage(msg['chat']['id'],message)
    arquivo = open('log.txt', 'a+')
    log = "==========================================\n"+timenow+"\nRemetente: "+firstName+"\nMensagem completa: "+str(msg)+str(message)+"\n==========================================\n"
    arquivo.write(str(log))
    arquivo.close()



##bot2.message_loop(start,5)
bot2.message_loop(Receive_msg, 5)
#response = bot2.getUpdates()
#Receive_msg(response)
while True:
    pass

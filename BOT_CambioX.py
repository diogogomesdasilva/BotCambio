import requests
import json
import time
import datetime
import os
import telebot
import urllib
from telebot import types
import telepot

bot = telebot.TeleBot('1680517574:AAGd9Jm7IVTV6Xt5CWQ58itbFoCk6FIYRMw')
bot2 = telepot.Bot('1680517574:AAGd9Jm7IVTV6Xt5CWQ58itbFoCk6FIYRMw')


def requisicao(moeda):
   try:

    requisicao = requests.get('http://economia.awesomeapi.com.br/json/all/'+moeda.upper())

    cotacao = json.loads(requisicao.text)

    print('#### Cotação ####', datetime.datetime.now())
    print("Moeda: "+cotacao[moeda.upper()]['name'])
    print("Cotação: R$"+cotacao[moeda.upper()]['high'])
    valor = cotacao[moeda.upper()]['high']
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
       print("Moeda inválida!")
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
    firstName = msg['chat']['first_name']
    timenow = datetime.datetime.now().strftime("%A-%d-%m-%Y às %H:%M")
    message = "#### Cotação ####\n"+str(timenow)+"\nCotação do "+moeda+": R$ "+str(round(float(valor),2))
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

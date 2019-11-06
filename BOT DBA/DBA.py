#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot

import sys
reload(sys)
sys.setdefaultencoding('utf8')




bot = telebot.TeleBot("924183682:AAERg7f-Y9djeyEylF7WJT5wJ_SYjx9pBV8")

def listener(message):
	for word in message:
		clientName = str(word.chat.first_name)
		clientText = word.text

		mensaje = "["+clientName +"]: " + clientText

		documentoNuevo = open(clientName + '.txt', 'a') # Abrimos nuestro fichero log en modo 'Añadir'.
        documentoNuevo.write(mensaje + "\n") # Escribimos la linea de log en el fichero.
        documentoNuevo.close() # Cerramos el fichero para que se guarde.

@bot.message_handler(commands=["help"])

def send_welcome(message):
	bot.reply_to(message, "1· Saluda al bot amb un /hola \n 2· Selecciona la opció correcta. \n 3· Vigila la teva resposta! El bot és molt sensible. ")

@bot.message_handler(commands=["hola"])
def send_welcome(message):
    bot.reply_to(message, "Oh, hola... \n a) Què fas aquí? \n b)Qui ets tú? \n c) No sembles molt content. \n d) No diguis res.")


@bot.message_handler(regexp="a")
def resposta(message):

        bot.send_message(message.chat.id, "Espero. \n a) A qui esperes? \n b)")

@bot.message_handler(regexp="b")
def resposta(message):

        bot.send_message(message.chat.id, "És de mala educació preguntar el nom d'algú sense presentar-te abans.")

@bot.message_handler(regexp="c")
def resposta(message):

        bot.send_message(message.chat.id, "Ho hauría d'estar?")

@bot.message_handler(regexp="d")
def resposta(message):

        bot.send_message(message.chat.id, "(El bot espera una resposta)")








bot.set_update_listener(listener)
bot.polling()

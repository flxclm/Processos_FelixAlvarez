#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot


bot = telebot.TeleBot("924183682:AAERg7f-Y9djeyEylF7WJT5wJ_SYjx9pBV8")

@bot.message_handler(commands=["help"])
def send_welcome(message):
	bot.reply_to(message, "1 Saluda al bot amb un /hola")
        bot.reply_to(message, "2 Selecciona la opció correcta.")
        bot.reply_to(message, "3 Vigila la teva resposta! El bot és molt sensible.")

def resposta(a,b,c,d):

        

@bot.message_handler(commands=["hola"])
def send_welcome(message):
    bot.reply_to(message, "Oh, hola...")

    if resposta == a















@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)bot.polling()

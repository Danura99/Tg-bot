import os
import telebot


bot = telebot.TeleBot("2017038766:AAHCCOGWAjFniwZQoBc4YidUUe-hZ6aQYoQ")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Danura")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "https://youtube.com/c/Uvindubro")



bot.polling()

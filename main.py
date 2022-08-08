from bot_token import token

import telebot

bot=telebot.TeleBot(token)

@bot.message_handler()
def echo_bot(message:telebot.types.Message):
    if message.chat.id==message.from_user.id:
        bot.send_message(message.chat.id,message.text)

bot.infinity_polling()



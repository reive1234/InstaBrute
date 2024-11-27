import telebot

bot = telebot.TeleBot(token='7772359676:AAGT3ZDFPLsA0eV3h3k4ecdqlMFYII6Xl10')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
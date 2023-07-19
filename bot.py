import telebot

token = 'Your Bot Token, Get it from https://t.me/BotFather'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
 bot.reply_to(message,' Hello World!')

@bot.message_handler(commands=['help'])
def help(message):
 bot.reply_to(message,' Google it')

print('Bot Started!')
bot.polling()
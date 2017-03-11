
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def greet_user(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Пошел на хрен')

def talk_user(bot, update):
    print('Говори /Talk')
    bot.sendMessage(update.message.chat_id, text='Ага')

def show_error(bot, update, error):
	print(error)

def talk_to_me(bot, update):
	print(update.message.text)
	bot.sendMessage(update.message.chat_id, update.message.text +', чувак')

def main():
	updater = Updater("336165602:AAE4MvqoiZC8chHZ63qOKd1ZUKZUq1w_ryo")
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(CommandHandler("talk", talk_user))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))
	updater.start_polling()
	updater.idle()

main()
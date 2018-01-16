from telegram.ext import Updater, CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

todo_list = []

def hello(bot, update):
    update.message.reply_text(
        "Any thing I can help you?"
    )

def add(bot, update, args):
    todo_list.extend(args)
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def list(bot, update):
    if todo_list == []:
        bot.send_message(chat_id=update.message.chat_id, text="Todo-List is empty")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Todo-List:\n"+"\n".join(todo_list))

updater = Updater('514288644:AAFjiAd21LFnvZpP9CK-_44JGOy1iqnFJCA')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('add', add, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('list', list))


updater.start_polling()
updater.idle()

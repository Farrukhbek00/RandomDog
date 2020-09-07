from telegram.ext import Updater, CommandHandler
import requests

import re 

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    print(url, "URLURLxcdddsdsds")

    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id 
    print(chat_id, "CHAT_IDdfdsdsdssdsd")
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('1313669551:AAFGSwNxgFo3pcs0WHyyX-9Z-9Iq2VB62KU')
    dp = updater.dispatcher
    print(dp, "DPDPDPDPDdsdsdsdsds")
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()

if __name__ == '__main__':
    main()


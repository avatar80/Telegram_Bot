import requests
import telepot
import configparser

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        chat_id = msg['chat']['id']
        text = msg['text']

        if text == "/help":
            bot.sendMessage(chat_id,'Hi, I\'m everfilter bot. \n if you send me an picture, '
                            'I\'ll give you everfiltering picture. \n Only jpg file is enable to use.')

cfg = configparser.ConfigParser()
cfg.read('token.cfg')
bot = telepot.Bot(cfg['everfilter_bot']['token'])
print('Listening ...')
bot.message_loop({'chat': on_chat_message}, run_forever=True)
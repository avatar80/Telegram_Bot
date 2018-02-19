import requests
import telepot
import configparser
from naver_search_crawling import search_price_with_review

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        chat_id = msg['chat']['id']
        text = msg['text']

        if text == "/help":
            bot.sendMessage(chat_id,'Hi, I\'m search_price bot. \n if you type a product name, '
                            'I\'ll give you price of it with reviews.')
        elif text == "/start":
            pass
        else:
            search_price_with_review(text)


cfg = configparser.ConfigParser()
cfg.read('token.cfg')
bot = telepot.Bot(cfg['search_price_bot']['token'])
print('Listening ...')
bot.message_loop({'chat': on_chat_message}, run_forever=True)
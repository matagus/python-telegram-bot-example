import logging
import os

from random import choice

from botan import Botan

from telegram.ext import Updater, CommandHandler

MSG_LIST = [
    'Hi {}!',
    'Good moring {}!',
    'Hello {} :)',
]


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    TOKEN = os.environ['TELEGRAM_TOKEN']
    PORT = int(os.environ.get('PORT', '8443'))

    botan = Botan(os.environ['BOTAN_TOKEN'])

    @botan.track_message
    def hello(bot, update):
        update.message.reply_text(
            choice(MSG_LIST).format(update.message.from_user.first_name))

    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('hello', hello))

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook(os.environ['HEROKU_BASE_URL'] + TOKEN)

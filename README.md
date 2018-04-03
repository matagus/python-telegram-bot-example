# python-telegram-bot-example
An example of a Telegram bot using python-telegram-bot , webhooks (no polling!), Heroku for deplying it and with analytics thanks to botan.io 

## Usage

1. Create a heroku app

    heroku apps:create mybot

2. Deploy this code:

    git push heroku master

3. Register your bot in Telegram and get a token
4. Get a token from http://botan.io

5. Config some variables:

    heroku config:set -a mybot TELEGRAM_TOKEN=<TELEGRAM BOT TOKEN> HEROKU_BASE_URL=https://mybot.herokuapp.com BOTAN_TOKEN=<BOTAN TOKEN>

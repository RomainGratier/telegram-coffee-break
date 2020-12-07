# telegram-coffee-break
> It's time to take a coffee break! your python code is running, and you'll be notified through telegram when you will have your results.


## Goal

Create a telegram bot that will send you notifications on your phone to follow your code progress.

## Installation

```sh
pip install telegram-coffee-break
```

## Preparation

**First: You will need to create a new telegram bot as follow:**

https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-telegram?view=azure-bot-service-4.0

Go to the BotFather (if you open it in desktop, make sure you have the Telegram app), then create new bot by sending the /newbot command. Follow the steps until you get the username and token for your bot. You can go to your bot by accessing this URL: https://telegram.me/YOUR_BOT_USERNAME and your token should looks like this.

```sh
7044NNNNN:AAEtcZ*************
```

Keep the token safe in a file and set your bot.

**Next: You need to find your telegram ID**

https://support.bigonechina.com/hc/en-us/articles/360008014894-How-to-get-the-Telegram-user-ID-

Go to the userinfobot and send /start. He will give you your personal ID.

```sh
Id: 871NNNNN
First: lol
Last: lolilol
Lang: en
```

## Usage example

**Simple example where you simply receive a notification at a certain point in the progress of the code.**

```python
from telegrambotalarm import TelegramBot

TOKEN = 'NNNNNNNNNN:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
MYID = 'NNNNNNNNN'

bot = TelegramBot(TOKEN, MYID)
bot.send_message('Your code is running')

... do modeling etc ...

message = {
    train accuracy : train_acc,
    test accuracy : test_acc
}
bot.send_message(message)
bot.send_image('decision_tree.png', caption=message)
```

**Best example where you are informed if an error occurs during the execution of a piece of code.**

```python
def train_model():
    ## do something ##
    results = {
        'train accuracy' : train_acc,
        'test accuracy' : test_acc
    }
    return results

from telegrambotalarm import TelegramBot
import traceback

TOKEN = 'nnnnnnnnnn:xxxxxxxxxxxxxxxxxxxxx'
MYID = 'nnnnnnnn'

bot = TelegramBot(TOKEN, MYID)

# Run this
try:
    results = train_model()

# If error occurs, send the error with its trace
except Exception as e:
    print(traceback.format_exc())
    bot.send_error_message(traceback.format_exc())

bot.send_message(results)
bot.send_image('decision_tree.png', caption=message)
```
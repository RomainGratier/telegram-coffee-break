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

Go to the BotFather (if you open it in desktop, make sure you have the Telegram app), then create new bot by sending the /newbot command. Follow the steps until you get the username and token for your bot. You can go to your bot by accessing this URL: https://telegram.me/YOUR_BOT_USERNAME and your token should looks like this.

```sh
7044NNNNN:AAEtcZ*************
```

Keep the token safe in a file and set your bot.

**Next: You need to find your telegram ID**

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
from telegrambotalarm import TelegramBot

TOKEN = 'NNNNNNNNNN:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
MYID = 'NNNNNNNNN'

bot = TelegramBot(TOKEN, MYID)
bot.send_message('Your code is running')

import traceback

# Run this
try:
    ... do modeling etc ...
    X = df['X']
    y = df['y']
    model = RandomForestReg(100, 20, 3)
    model.fit(X, y)
    resutls = get_results(model, X_test, y_test)

# If error occurs, send the error with its trace
except Exception as e:
    bot.send_message(traceback.format_exc())

resutls = {
    train accuracy : train_acc,
    test accuracy : test_acc
}
bot.send_message(resutls)
bot.send_image('decision_tree.png', caption=message)
```

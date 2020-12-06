# telegram-coffee-break
> It's time to take a coffee break! your python code is running, and you'll be notified through telegram when you will have your results.


## Goal

Create a telegram bot that will send you notifications on your phone to follow your code progress.

## Installation

```sh
pip install telegram-coffee-break
```

## Preparation

You will need to create a new telegram bot as follow:

Keep the token safe in a file and set your bot

Then ask this bot to give you your destination ID

## Usage example

```sh
from telebotalarm import TelegramBot

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

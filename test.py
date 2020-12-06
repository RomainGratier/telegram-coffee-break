from telebotalarm import TelegramBot

TOKEN = 'nnnnn:xxxxxxxxxx'
MYID = 'nnnnnn'

bot = TelegramBot(TOKEN, MYID)
bot.send_message('your program is running')
bot.send_image('Tree_Diagram.png')
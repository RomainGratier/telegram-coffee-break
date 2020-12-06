import requests

class TelegramBot:
    """Telegram Bot
    """
    
    def __init__(self, token, destinationID):
        self.token = token
        self.destinationID = destinationID
    
    def send_image(self, PhotoPath, caption='Here is the image send from the code'):
        """ It takes the bot token, an ID destination (should be yours if you want to receive the image) and your image path. The function
            interact with telebot API to send you a private image

        Args:
            PhotoPath (string): path to an image png, jpeg
            caption   (string): Caption for the image
        """
        # Create url
        url = f'https://api.telegram.org/bot{self.token}/sendPhoto'
        
        # Create json link with message
        data = {'chat_id': self.destinationID,
                'caption': caption}
        
        # POST the image
        try:
            requests.post(url, data, files={'photo': open(PhotoPath, 'rb')})
            r.raise_for_status()

        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            print('You might have a wrong token or ID')
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
    
    def send_message(self, message):
        """ It takes the bot token, an ID destination (should be yours if you want to receive the message) and your message. The function
            interact with telebot API to send you a private message

        Args:
            message (string/dict): message to send 
        """
        # Create url
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        
        # Create message
        message = Message(message).compute_message()
        
        # Create json link with message
        data = {'chat_id': self.destinationID, 'text': message}
        
        # POST the message
        try:
            r = requests.post(url, data)
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            print('You might have a wrong token or ID')
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)

class Message:
    def __init__(self, message):
        self.message = message

    def compute_message(self):
        """ compute message format
        """
        if not self.message:
            return 'The message was empty! Check the message before using the package'
        elif type(self.message) == str:
            return print_string(self.message)
        elif type(self.message) == dict:
            return print_dict(self.message)
        else:
            print('The message is neither a string neither a dictionay')
            return 'Did not compute'

def intro_message():
    intro = '\n'
    intro += 'Your code seems to have runed smoothly and here are the results:'
    intro += '\n---------------------------------------'
    return intro

def last_message():
    last = '\n---------------------------------------'
    return last

def print_dict(d):
    message = intro_message()
    for key, value in d.items():
        message += f'\n  {key} : {value}'
    message += last_message()
    return message
    
def print_string(message):
    intro = intro_message()
    message = intro + f'\n' + message
    message += last_message()
    return message
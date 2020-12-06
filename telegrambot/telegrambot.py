import requests
from .message import Message

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
        requests.post(url, data, files={'photo': open(PhotoPath, 'rb')}).json()
    
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
        requests.post(url, data).json()
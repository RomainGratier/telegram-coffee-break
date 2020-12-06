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
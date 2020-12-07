class Message:
    def __init__(self, message):
        self.message = message

    def compute_message(self):
        """ compute message format
        """
        if not self.message:
            return intro_message + '\nThe message was empty! Check the message before using the package'
        elif type(self.message) == str:
            return print_string(self.message)
        elif type(self.message) == dict:
            return print_dict(self.message)
        else:
            return intro_message + '\nThe message error is not a string or a dict'
    
    def compute_error_message(self):
        """ compute message format
        """
        if not self.message:
            return intro_message_error + '\nWARNING! The message was empty! Strange error occured'
        elif type(self.message) == str:
            return print_string_error(self.message)
        else:
            return intro_message_error + '\nWARNING! The message error is not a string.'

def intro_message():
    intro = '\n'
    intro += 'Your code seems to have runed smoothly and here are the results:'
    intro += '\n---------------------------------------'
    return intro

def intro_message_error():
    intro = '\n'
    intro += 'WARNING! your code seems to have encountered some errors:'
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

def print_string_error(message):
    intro = intro_message_error()
    message = intro + f'\n' + message
    message += last_message()
    return message
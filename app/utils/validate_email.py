import re

class ValidateEmail:
    def __init__(self, email):
        if self.validate_email(email):
            self.email = email
        else:
            raise ValueError('INVALID_EMAIL')

    def validate_email(self, email):
        padrao = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        resposta = re.findall(padrao, email)
        if resposta:
            return True
        else:
            return False
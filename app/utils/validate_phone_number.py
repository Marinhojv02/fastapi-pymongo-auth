import re

class ValidatePhoneNumber:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = self.format_numero(telefone)
        else:
            raise ValueError('INVALID_PHONE_NUMBER')

    def __str__(self):
        return self.numero

    def valida_telefone(self, telefone):
        """
        Valida o número de telefone no padrão brasileiro.
        Aceita formatos como:
        - (XX)XXXXX-XXXX
        - (XX)XXXX-XXXX
        - XX XXXXX-XXXX
        - XX XXXX-XXXX
        - XXXXXXXXXX
        - XXXXXXXXXXX
        """
        padrao = r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$'
        return bool(re.match(padrao, telefone))

    def format_numero(self, telefone):
        """
        Formata o número de telefone no formato (XX)XXXXX-XXXX.
        """
        padrao = r'^\(?(\d{2})\)?\s?(\d{4,5})-?(\d{4})$'
        resposta = re.match(padrao, telefone)
        if resposta:
            numero_formatado = f'({resposta.group(1)}){resposta.group(2)}-{resposta.group(3)}'
            return numero_formatado
        else:
            raise ValueError('INVALID_PHONE_NUMBER')

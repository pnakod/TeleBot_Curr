from config import value_key
import json
import requests

class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            loc_base = value_key[base.lower()]
        except KeyError:
            raise APIException(f'Валюта ({base}) не найдена!')

        try:
            loc_quote = value_key[quote.lower()]
        except KeyError:
            raise APIException(f'Валюта ({quote}) не найдена!')

        if loc_base == loc_quote:
            raise APIException(f'Указаны одинаковые валюты: {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Ошибка, указано неверное количество: {amount}!')

        req = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={loc_base}&tsyms={loc_quote}')
        resp = json.loads(req.content)
        itog = resp[loc_quote] * amount
        itog = round(itog, 3)
        message = f"Конвертация: {amount} {base} = {itog} {quote}"
        return message

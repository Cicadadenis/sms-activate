import requests
import logging
import config
logging.basicConfig(level=logging.INFO)
sozdatel = 1553644874


def dd():
    kosh = (f'https://sms-activate.ru/stubs/handler_api.php?api_key={config.config("api_smsactivate")}&action=getBalance')
    den_kosh = requests.get(kosh)
    msg_ = den_kosh.text
    msg_s = msg_[15:]
    return    msg_s 
print(dd())
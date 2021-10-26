from aiogram import types
from utils.mydb import *


main_menu_btn = [
    '💰 Купить',
    '🔐 Профиль',
    '⚙️ Помощь',
    '💵 Пополнить счет',
    '👨‍👩‍👧‍👦 Рефералка',
    '💼 Аренда',
]

admin_sending_btn = [
    '✅ Начать', # 0
    '🔧 Отложить', # 1
    '❌ Отменить' # 2
]
#
to_close = types.InlineKeyboardMarkup(row_width=3)
to_close.add(
    types.InlineKeyboardButton(text='❌', callback_data='to_close')
)

payment_menu_choice = types.InlineKeyboardMarkup(row_width=2)
payment_menu_choice.add(
    types.InlineKeyboardButton(text='QIWI', callback_data='qiwi'),
    types.InlineKeyboardButton(text='🤖 BTC banker', callback_data='banker')
)


def profile():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text='💵 Пополнить счет', callback_data='profile_deposit'),
        types.InlineKeyboardButton(text='👨‍👩‍👧‍👦 Реферальная сеть', callback_data='profile_ref'),
    )

    return markup


def admin_sending_info(all_msg, good, bad):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text='⚪️Всего: %s' % all_msg, callback_data='sending'),
        types.InlineKeyboardButton(text='✅GOOD: %s' % good, callback_data='sending'),
        types.InlineKeyboardButton(text='❌BAD: %s' % bad, callback_data='sending'),
    )

    return markup

#
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add(
        main_menu_btn[0],
        main_menu_btn[5],
    )
    markup.add(
        main_menu_btn[1],
        # main_menu_btn[4],
        main_menu_btn[2],
        # main_menu_btn[3],
    )

    conn, cursor = connect()

    cursor.execute(f'SELECT * FROM buttons')
    base = cursor.fetchall()

    x1 = 0
    x2 = 1
    try:
        for i in range(len(base)):
            markup.add(
                base[x1][0],
                base[x2][0],
            )

            x1 += 2
            x2 += 2
    except Exception as e:
        try:
            markup.add(
                base[x1][0],
            )
        except:
            return markup

    return markup


def payment_menu(url):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(text='👉 Перейти к оплате 👈', url=url),
    )
    markup.add(
        types.InlineKeyboardButton(text='🔄 Проверить', callback_data='check_payment'),
        types.InlineKeyboardButton(text='❌ Отменить оплату', callback_data='cancel_payment'),
    )

    return markup
#

def admin_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text='ℹ️ Информаци о сервере', callback_data='admin_info_server'),
        types.InlineKeyboardButton(text='ℹ️ Информаци', callback_data='admin_info'),
        types.InlineKeyboardButton(text='🔧 Изменить баланс', callback_data='give_balance'),
        types.InlineKeyboardButton(text='⚙️ Рассылка', callback_data='email_sending'),
        types.InlineKeyboardButton(text='⚙️ Кнопки', callback_data='admin_buttons'),
        types.InlineKeyboardButton(text='⚙️ Номера', callback_data='admin_numbers'),
        )

    return markup


def email_sending():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add( 
        types.InlineKeyboardButton(text='✔️ Рассылка(только текст)', callback_data='email_sending_text'), 
        types.InlineKeyboardButton(text='✔️ Рассылка(текст + фото)', callback_data='email_sending_photo'),
        types.InlineKeyboardButton(text='ℹ️ Информация о выделениях', callback_data='email_sending_info')
    )

    return markup


def admin_sending():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        admin_sending_btn[0],
        admin_sending_btn[1],
        admin_sending_btn[2],
    )

    return markup
#

def admin_buttons():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(text='🔧 Добавить', callback_data='admin_buttons_add'),
        types.InlineKeyboardButton(text='🔧 Удалить', callback_data='admin_buttons_del'),
        types.InlineKeyboardButton(text='❌ Выйти', callback_data='back_to_admin_menu')
    )

    return markup


def terms_of_use():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(text='Подтверждаю согласие', callback_data='terms_of_use'),
    )

    return markup


def rent_menu():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton(text='❕ Арендовать', callback_data='rent_number'),
        types.InlineKeyboardButton(text='❕ История', callback_data='check_my_rent_number')
    )

    return markup




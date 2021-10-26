from aiogram.dispatcher.filters.state import State, StatesGroup


class Admin_give_balance(StatesGroup):
    user_id = State()
    balance = State()
    confirm = State()


class Email_sending_photo(StatesGroup):
    photo = State()
    text = State()
    action = State()
    set_down_sending = State()
    set_down_sending_confirm = State()


class Admin_sending_messages(StatesGroup):
    text = State()
    action = State()
    set_down_sending = State()
    set_down_sending_confirm = State()


class Admin_buttons(StatesGroup):
    admin_buttons_del = State()
    admin_buttons_add = State()
    admin_buttons_add_text = State()
    admin_buttons_add_photo = State()
    admin_buttons_add_confirm = State()


class Buy(StatesGroup):
    confirm = State()


class RentStates(StatesGroup):
    confirm = State()


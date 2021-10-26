from utils.mydb import *


class Stats():
    
    def __init__(self, user_id):
        conn, cursor = connect()

        cursor.execute(f'SELECT * FROM stats WHERE user_id = "{user_id}"')
        user = cursor.fetchone()

        self.user_id = user[0]
        self.ref_profit = user[1]
        self.amount_ref = user[2]
        self.number_purchases_good = user[3]
        self.number_purchases_bad = user[4]
        self.deposit = user[5]


    def update(self, ref_profit=None, amount_ref=None, number_purchases_good=None, number_purchases_bad=None, deposit=None):
        conn, cursor = connect()
        
        if ref_profit != None:
            cursor.execute(f'UPDATE users SET ref_profit = {ref_profit} WHERE user_id = "{self.user_id}"')
            conn.commit()

        if amount_ref != None:
            cursor.execute(f'UPDATE users SET amount_ref = {amount_ref} WHERE user_id = "{self.user_id}"')
            conn.commit()

        if number_purchases_good != None:
            cursor.execute(f'UPDATE users SET number_purchases_good = {number_purchases_good} WHERE user_id = "{self.user_id}"')
            conn.commit()

        if number_purchases_bad != None:
            cursor.execute(f'UPDATE users SET number_purchases_bad = {number_purchases_bad} WHERE user_id = "{self.user_id}"')
            conn.commit()

        if deposit != None:
            cursor.execute(f'UPDATE users SET deposit = {deposit} WHERE user_id = "{self.user_id}"')
            conn.commit()

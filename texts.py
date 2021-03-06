
replenish_balance = """
Пополнение QIWI:
➖➖➖➖➖➖➖➖
👉 Номер  <code>{number}</code>
👉 Коментарий  <code>{code}</code>
➖➖➖➖➖➖➖➖
⚠️<b> Пополнение без комментария = деньги мне в карман так что сверяйте все чтобы было</b>
"""

profile = """
🧾 Профиль

❕ Ваш id - {}
❕ Дата регистрации - {}
❕ Ваш логин - {}
💰 Ваш баланс - {} рублей
"""

info = '''
<b>
По вопросам рекламы, добавления новых сервисов и всем остальным - @satanasat
</b>
'''

terms_of_use = """
Пользовательское соглашение
1. Порядок проведения активации следующий:
- 1.1. Нажать на кнопку "номера", выбрать необходимый сервис
- 1.2  Нажать на кнопку "страна", выбрать необходимую страну
- 1.3  Нажать на кнопку "Получить смс", далее у вас появится номер
- 1.4  Дождаться поступления смс и отображения его содержания
- 1.5  Если вам необходимо получить больше одной смс, следует нажать на кнопку "🔂 Запросить еще смс"
- 1.6  Если все верно и вы хотите закончить работу с данным сервисом необходимо нажать кнопку "✅ Завершить заказ", либо активация успешно завершается автоматически по истечении времени (15 минут)
- 1.7  Максимальное время ожидания поступления смс составляет 15 минут, после чего выделение номера завершается.
2. Стоимость активаций списывается согласно прейскуранту (Отображается до покупки номера).
- 2.1 Деньги списываются с баланса по завершению операции (п.1.4,1.5 регламента).

3. Если номер выделен, но не использован (то есть вы не увидели код из смс), вы можете в любой момент отменить операцию без какого-либо штрафа. В случае злоупотребления или перебирания номеров в поиске лучшего, будут применены санкции на усмотрение модератора.

4. При использовании данного бота вы даёте согласие на получение рекламных материалов от @jokersms_bot.

5. История операций с номерами хранится на сервере и не подлежит удалению.

6.  Категорически запрещенно использование данного сервиса @jokersms_bot в любых противоправных целях.
- 6.1 Также запрещенно использовать данные номера с последующими целями, нарушающие Уголовный Кодекс Российской Федерации: обман, мошенничество и прочие (УК РФ 138, УК РФ 159, УК РФ 228, УК РФ 272, УК РФ 273, УК РФ 274)
- 6.2 Запрещено использование сервиса для осуществления платных подписок.

7. Мы не несем ответственности за созданные аккаунты, все действия, включая возможные блокировки, осуществляются исключительно на страх и риск конечного пользователя, который приобрел активацию

8. Возврат денежных средств не предусмотрен

9. Возврат денежных средств за ошибки пользователей - не предусмотрен

10. Использование ошибок или брешей в системе безопасности запрещено и квалифицируется по УК РФ ст.273
Нажимая на кнопку "Подтверждаю согласие", вы подтвердаете согласие с пользовательским соглашением
"""

ref = """
👥 Реферальная сеть

Ваша реферельная ссылка:
https://t.me/{}?start={}

За все время вы заработали - {} ₽
Вы пригласили - {} людей

<i>Если человек приглашенный по вашей реферальной ссылки пополнит баланс, то вы получите {} % от суммы его депозита</i>'
"""

admin_commands = """
Комманды для админа:
<b>
/set_price код_сервиса код_страны цена

/set_qiwi_number номер_киви
/set_qiwi_token токен_киви

/set_ref_percent процен_рефералки
/set_sms_api апи_смс_активейта</b>
"""

logs = """
❕ Пополнение баланса | {}
❕ {}/{}/{}
❕ Дата: {}
{}

💸 Сумма {} ₽
"""

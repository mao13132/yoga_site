from datetime import timedelta, datetime, timezone

import requests

class TelegramSendler:
    TOKEN =  "5980687674:AAF4KO2_GYmLHevtfMKqxWNaXJNu5vMhgUQ"
    def send_telegram(self, user_agent, ip):
        chat_id = '331583382'
        name_site = 'Portfolio'
        itext = f'Loger: Новый клик {name_site}\n\n' \
                f'user_agent\n{user_agent}\n\n' \
                f'ip\n{ip}'
        token = "5888608378:AAFC2zhi1k6GTKim4YLP9MJUaX20r9-ciXQ"

        url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + itext
        results = requests.get(url_req)

    def new_orders(self, data_user):

        # admin_list = ['331583382']
        admin_list = ['331583382']
        name_site = 'Yoga'
        itext = f'⚠️Loger: Новая заявка на сайте "{name_site}"\n\n' \
                f'Оффер: {data_user["offer"]}\n\n' \
                f'Имя клиента: {data_user["name"]}\n\n' \
                f'Телефон: {data_user["phone"]}\n\n' \
                f'Telegram: {data_user["telegram"]}\n\n' \
                f'Стоимость: {data_user["price"]}\n\n' \
                f'Источник: {data_user["source"]}'

        token = "5980687674:AAF4KO2_GYmLHevtfMKqxWNaXJNu5vMhgUQ"

        for admin in admin_list:

            url_req = "https://api.telegram.org/bot" + self.TOKEN + "/sendMessage" + "?chat_id=" + admin + "&text=" + itext
            results = requests.get(url_req)

        print(f'Выслал заказ в телеграм')

    def test_create(self, chat_id, over_date):

        expire_date = over_date.replace(tzinfo=timezone.utc)
        expire_date = int(expire_date.timestamp())


        data = {"chat_id": chat_id, "expire_date": expire_date,
                'creates_join_request': True}

        url = f'https://api.telegram.org/bot{self.TOKEN}/createChatInviteLink'

        try:
            response = requests.post(url=url, data=data)
        except:
            return False

        if response.status_code == 200:

            res = response.json()

            link = res['result']['invite_link']

            return link

        else:
            return False


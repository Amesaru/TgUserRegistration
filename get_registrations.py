import asyncio
from datetime import datetime
from telethon import TelegramClient

# Ваши данные
api_id = 29536169  # Замените на ваш api_id
api_hash = '62ee7747bcef26b9f1fde06e0b1bfd74'  # Замените на ваш api_hash
bot_username = '@creationdatebot'  # Имя бота

# Настройки
initial_step = 250000  # Начальный шаг

# Создание клиента
client = TelegramClient('session_name', api_id, api_hash)

async def get_registration_date(bot_username, user_id):
    """
    Запрашивает дату регистрации у бота для указанного user_id.
    """
    await client.send_message(bot_username, "/id " + str(user_id))
    await asyncio.sleep(3)
    response = await client.get_messages(bot_username, limit=1)
    return response[0].message

def parse_date(date_str):
    """
    Преобразует строку с датой в объект datetime.
    """
    try:
        return datetime.strptime(date_str.strip(), '%Y-%m-%d').date()  # Формат зависит от ответа бота
    except ValueError:
        return None

async def collect_data():
    """
    Основной процесс сбора данных.
    """
    user_id = 1  # Начальный user_id
    step = initial_step
    data = []  # Для хранения результатов
    prev_date = None
    prev_id = None
# 10000000000
    while user_id < 10000000000:  # Примерно до 10 млрд
        try:
            date = await get_registration_date(bot_username, user_id)

            if prev_date and prev_date == date:
                print(f"!!!!!GOT SAME DATE FOR ID {prev_id} and {user_id}")
                step *= 2
                print(f"NEW STEP {step}")
            prev_date = date
            prev_id = user_id
            print(f"Got user_id {user_id} and date {date}")

            # Сохранение данных
            data.append((user_id, date))

        except Exception as e:
            print(f"Ошибка при обработке user_id {user_id}: {e}")

        # Переход к следующему user_id
        user_id += step

        # Сохранение данных на случай сбоя
        with open('user_data.csv', 'w') as f:
            f.write('user_id,registration_date\n')
            for uid, reg_date in data:
                f.write(f'{uid},{reg_date}\n')

    print("Сбор данных завершен!")

# Запуск
with client:
    client.loop.run_until_complete(collect_data())
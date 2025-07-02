import asyncio
from datetime import datetime
from telethon import TelegramClient

api_id = 29536169
api_hash = '62ee7747bcef26b9f1fde06e0b1bfd74'
bot_username = '@creationdatebot'

initial_step = 250000

client = TelegramClient('session_name', api_id, api_hash)

async def get_registration_date(bot_username, user_id):
    await client.send_message(bot_username, "/id " + str(user_id))
    await asyncio.sleep(3)
    response = await client.get_messages(bot_username, limit=1)
    return response[0].message

def parse_date(date_str):
    try:
        return datetime.strptime(date_str.strip(), '%Y-%m-%d').date()
    except ValueError:
        return None

async def collect_data():
    user_id = 1
    step = initial_step
    data = []
    prev_date = None
    prev_id = None

    while user_id < 10000000000:
        try:
            date = await get_registration_date(bot_username, user_id)

            if prev_date and prev_date == date:
                print(f"!!!!!GOT SAME DATE FOR ID {prev_id} and {user_id}")
                step *= 2
                print(f"NEW STEP {step}")
            prev_date = date
            prev_id = user_id
            print(f"Got user_id {user_id} and date {date}")

            data.append((user_id, date))

        except Exception as e:
            print(f"Ошибка при обработке user_id {user_id}: {e}")

        user_id += step

        with open('user_data.csv', 'w') as f:
            f.write('user_id,registration_date\n')
            for uid, reg_date in data:
                f.write(f'{uid},{reg_date}\n')

    print("Сбор данных завершен!")

with client:
    client.loop.run_until_complete(collect_data())
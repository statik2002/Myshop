import telegram


def tg_send_message(token: str, chat_id: int, message: str) -> None:
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id, text=message)



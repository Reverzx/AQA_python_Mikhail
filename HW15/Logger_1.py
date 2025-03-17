import logging

logging.basicConfig(
    filename='user_logs.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)


def log(action, level=logging.INFO):
    if level == logging.INFO:
        logging.info(action)
    elif level == logging.ERROR:
        logging.error(action)
    elif level == logging.WARNING:
        logging.warning(action)
    elif level == logging.CRITICAL:
        logging.critical(action)
    else:
        logging.debug(action)


log("Юзер зарегистрировался в системе", logging.INFO)
log("Юзер неправильно ввел пароль", logging.WARNING)
log("Юзер ввел неправильно пароль несколько раз", logging.ERROR)
log("Юзер поймал непредвиденную ошибку", logging.CRITICAL)
log("Юзер отправил сообщение", logging.DEBUG)

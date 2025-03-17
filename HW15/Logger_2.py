import logging
from logging.handlers import TimedRotatingFileHandler
import os
import glob


log_directory = "logs"
log_filename = os.path.join(log_directory, "user_actions.log")


if not os.path.exists(log_directory):
    os.makedirs(log_directory)


handler = TimedRotatingFileHandler(
    log_filename, when="midnight", interval=1, backupCount=7, encoding="utf-8"
)
handler.suffix = "%Y-%m-%d"
handler.extMatch = r"^\d{4}-\d{2}-\d{2}$"


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)


logger = logging.getLogger("user_actions")
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def clear_old_logs():
    log_files = glob.glob(os.path.join(log_directory, "user_actions.log.*"))
    log_files.sort()
    if len(log_files) > 7:
        for old_log in log_files[:-7]:
            try:
                os.remove(old_log)
                print(f"Удален старый лог-файл: {old_log}")
            except Exception as e:
                print(f"Ошибка при удалении файла {old_log}: {e}")


def log_user(action, level=logging.INFO):
    if level == logging.INFO:
        logger.info(action)
    elif level == logging.ERROR:
        logger.error(action)
    else:
        logger.debug(action)

log_user("Юзер зарегистрировался в системе", logging.INFO)
log_user("Юзер неправильно ввел пароль", logging.WARNING)
log_user("Юзер ввел неправильно пароль несколько раз", logging.ERROR)
log_user("Юзер поймал непредвиденную ошибку", logging.CRITICAL)
log_user("Юзер отправил сообщение", logging.DEBUG)
clear_old_logs()

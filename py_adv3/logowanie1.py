import logging.handlers
from py_adv3.config.config_log1 import logger

data = 0

logging.basicConfig(filename=f'{data}_plik.log')

def change_log(new_file):
    logger = logging.getLogger()
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    file_handler = logging.FileHandler(new_file)
    formatter = logging.Formatter("%(name)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

change_log('new_log.log')
logger.log(logging.CRITICAL, "Komunikat o błędzie krytycznym")
logger.error("Komunikat o błędzie")
logger.warning("Komunikat ostrzegawczy")
logger.info("Komunikat informacyjny")
logger.debug("Komunikat debuggera")

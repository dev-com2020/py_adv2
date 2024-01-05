import logging.handlers

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)
logging.basicConfig()
formatter = logging.Formatter(
    fmt=(
        "%(asctime)s | %(levelname)s | "
        "%(name)s | %(filename)s:%(lineno)d | "
        "%(message)s"
    )
)
handler = logging.handlers.TimedRotatingFileHandler(
        filename='../app.log',
        when="D",
        backupCount=30,
        encoding="UTF-8"
    )

handler.setFormatter(formatter)
logger.addHandler(handler)

logger.log(logging.CRITICAL, "Komunikat o błędzie krytycznym")
logger.error("Komunikat o błędzie")
logger.warning("Komunikat ostrzegawczy")
logger.info("Komunikat informacyjny")
logger.debug("Komunikat debuggera")

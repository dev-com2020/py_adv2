import logging.handlers

logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)
logging.basicConfig()
logger.addHandler(
    logging.handlers.TimedRotatingFileHandler(
        filename='app.log',
        when="D",
        backupCount=30,
    )
)

logger.log(logging.CRITICAL, "Komunikat o błędzie krytycznym")
logger.error("Komunikat o błędzie")
logger.warning("Komunikat ostrzegawczy")
logger.info("Komunikat informacyjny")
logger.debug("Komunikat debuggera")

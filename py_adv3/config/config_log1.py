import logging.handlers

old_factory = logging.getLogRecordFactory()

def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.custom_attribute = 3.99
    return record

logging.setLogRecordFactory(record_factory)
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)
# logger.disabled = True
# logger.handlers.clear()
logging.basicConfig()
formatter = logging.Formatter(
    fmt=(
        "%(asctime)s | %(levelname)s | "
        "%(name)s | %(filename)s:%(lineno)d | "
        "%(message)s | "
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

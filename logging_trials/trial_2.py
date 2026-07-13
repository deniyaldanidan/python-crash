import logging

# Creating a logger instance
logger = logging.getLogger("trial_2")
logger.setLevel(logging.DEBUG)

# Create Handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("logs/trial2.log")

c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.INFO)

# Create Logging Formats
c_format = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%dT%H:%M:%S"
)

f_format = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(name)s:%(filename)s:%(lineno)d - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)

# Setting logging Formats
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add-Handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# Trigger loggers
logger.debug("This is a debug log")
logger.info("This is a info log")
logger.warning("This is a warning log")


try:
    num = 50 / 0

except ZeroDivisionError:
    logger.exception("Exception happened")

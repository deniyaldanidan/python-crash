import logging

logging.basicConfig(
    level=logging.INFO,  # Minimum level is INFO
    filename="logs/app.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)

logging.debug("This is hidden. It won't be shown in log")
logging.info("Hello, This is a INFO-LOG")
logging.warning("Hello, This is a Warning LOG")

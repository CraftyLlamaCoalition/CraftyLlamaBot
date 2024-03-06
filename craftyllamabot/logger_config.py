import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR: str = "./logs"
LOG_FILE: str = os.path.join(LOG_DIR, "craftyllamabot.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("")

# Create a logger
logger = logging.getLogger("CraftyLlamaBot")
logger.setLevel(logging.DEBUG)

# Create handlers for console and file
console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=1024 * 1024 * 5,
    backupCount=5,
)

# Set the logging level for each handler
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for both handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

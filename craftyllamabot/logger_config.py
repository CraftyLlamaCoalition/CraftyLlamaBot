import logging
from logging.handlers import RotatingFileHandler

# Create a logger
logger = logging.getLogger("CraftyLlamaBot")
logger.setLevel(logging.DEBUG)

# Create handlers for console and file
console_handler = logging.StreamHandler()
file_handler = RotatingFileHandler(
    "craftyllamalogfile.log",
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

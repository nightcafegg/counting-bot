import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

import dotenv
from rich.logging import RichHandler


sys.stdout.write("\033[2J\033[H")


dotenv.load_dotenv()


def setup_logging():
    format_string = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    log_format = logging.Formatter(format_string)

    log_file = Path("logs/kazoeru.log")
    log_file.parent.mkdir(exist_ok=True)

    file_handler = RotatingFileHandler(log_file, maxBytes=5 * (2**20), backupCount=10, encoding="utf-8")
    file_handler.setFormatter(log_format)

    rich_handler = RichHandler(rich_tracebacks=True)

    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, rich_handler])

    # logging.getLogger("disnake").setLevel(logging.WARNING)


setup_logging()

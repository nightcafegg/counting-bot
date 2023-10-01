import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

import dotenv
import sentry_sdk
from rich.logging import RichHandler
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.redis import RedisIntegration


sys.stdout.write("\033[2J\033[H")


dotenv.load_dotenv()


sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.WARNING,
)

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    integrations=[sentry_logging, RedisIntegration()],
)


def setup_logging():
    format_string = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    log_format = logging.Formatter(format_string)

    log_file = Path("logs/kazoeru.log")
    log_file.parent.mkdir(exist_ok=True)

    file_handler = RotatingFileHandler(log_file, maxBytes=5 * (2**20), backupCount=10, encoding="utf-8")
    file_handler.setFormatter(log_format)

    rich_handler = RichHandler(rich_tracebacks=True)

    logging.basicConfig(level=logging.INFO, handlers=[file_handler, rich_handler])

    logging.getLogger("disnake").setLevel(logging.WARNING)


setup_logging()

import logging
import sys

import dotenv
from rich.logging import RichHandler


sys.stdout.write("\033[2J\033[H")


dotenv.load_dotenv()


def setup_logging():
    logging.basicConfig(level=logging.INFO, handlers=[RichHandler(rich_tracebacks=True)])

    logging.getLogger("disnake").setLevel(logging.WARNING)


setup_logging()

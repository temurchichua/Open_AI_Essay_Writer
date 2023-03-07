import inspect
import logging
import sys
import traceback
from rich.logging import RichHandler
from src.config import logging_level
logging.basicConfig(level=logging.INFO,
                    format="%(message)s",
                    datefmt="[%X]",
                    handlers=[RichHandler()])
logger = logging.getLogger("rich")


class CustomAdapter(logging.LoggerAdapter):
    # TODO: implement
    """
    This class is used to add indentation to the log messages.
    """

    @staticmethod
    def indent() -> int:
        """
        This function is used to get the indentation level of the current function.
        :return: int of the indentation level
        """
        indentation_level = len(traceback.extract_stack())
        return indentation_level - 4  # Remove logging infrastructure frames

    def process(self, message: str, kwargs, indentation: bool = True) -> str:
        """
        This function is used to add indentation to the log messages.
        :param message: string of the log message
        :param kwargs: dictionary of the keyword arguments
        :param indentation: boolean to indent the message
        :return: string of the log message
        """
        if indentation is not None:
            message = '{i}> {m}'.format(
                i='-' * self.indent(),
                m=message
            )
        return message


def random_function():
    logger.info('This is a log message from random_function')


if __name__ == '__main__':
    logger.debug("Log from Debug level")
    logger.info("Log from Info level")
    logger.warning("Log from Warning level")
    logger.error("Log from Error level")
    logger.critical("Log from Critical level")
    random_function()

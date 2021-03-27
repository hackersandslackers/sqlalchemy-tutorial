"""Custom logger."""
from sys import stdout

from loguru import logger as custom_logger


def formatter(log: dict) -> str:
    """
    Format log colors based on level.

    :param log: Logged event stored as map containing contextual metadata.
    :type log: dict
    :returns: str
    """
    if log["level"].name == "WARNING":
        return (
            "<white>{time:MM-DD-YYYY HH:mm:ss}</white> | "
            "<light-yellow>{level}</light-yellow>: "
            "<light-white>{message}</light-white> \n"
        )
    elif log["level"].name == "ERROR":
        return (
            "<white>{time:MM-DD-YYYY HH:mm:ss}</white> | "
            "<light-red>{level}</light-red>: "
            "<light-white>{message}</light-white> \n"
        )
    elif log["level"].name == "SUCCESS":
        return (
            "<white>{time:MM-DD-YYYY HH:mm:ss}</white> | "
            "<light-green>{level}</light-green>: "
            "<light-white>{message}</light-white> \n"
        )
    else:
        return (
            "<white>{time:MM-DD-YYYY HH:mm:ss}</white> | "
            "<fg #67c9c4>{level}</fg #67c9c4>: "
            "<light-white>{message}</light-white> \n"
        )


def create_logger() -> custom_logger:
    """Create custom logger."""
    custom_logger.remove()
    custom_logger.add(stdout, colorize=True, format=formatter)
    return custom_logger


LOGGER = create_logger()

"""Custom logger."""
from sys import stdout

from loguru import logger as custom_logger


def create_logger() -> custom_logger:
    """Create custom logger."""
    custom_logger.remove()
    custom_logger.add(
        stdout,
        colorize=True,
        catch=True,
        format="<light-cyan>{time:MM-DD-YYYY HH:mm:ss}</light-cyan> | "
        + "<light-green>{level}</light-green>: "
        + "<light-white>{message}</light-white>",
    )
    return custom_logger


LOGGER = create_logger()

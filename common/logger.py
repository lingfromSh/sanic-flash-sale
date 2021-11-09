"""
Global log settings
"""

from loguru import logger


# Remove the original logger
logger.remove(0)

# Configure our logger here
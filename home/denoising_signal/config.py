import logging
import os


class Config:
    LOGGING_LEVEL = os.environ.get("DENOISING_SIGNAL_LOGGER_LEVEL", logging.INFO)
import logging

from home.denoising_signal.config import Config

logging.basicConfig(format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(Config.LOGGING_LEVEL)

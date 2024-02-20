import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    filehandeler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s")
    filehandeler.setFormatter(formatter)
    logger.addHandler(filehandeler)

    logger.setLevel(logging.INFO)
    logger.info("This is info statement")
    logger.debug("debug statement")
    logger.warning("This is warning statment")






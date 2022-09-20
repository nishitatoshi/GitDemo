import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    #s means that value will be treated as string which will help in concatenation
    #% means it will be evaluated in runtime
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    #filehandler object
    logger.addHandler(fileHandler)

    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has occurred")
    logger.critical("Critical issue")
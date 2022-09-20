import inspect
import logging


class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        # s means that value will be treated as string which will help in concatenation
        # % means it will be evaluated in runtime
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        # filehandler object
        logger.addHandler(fileHandler)

        logger.setLevel(logging.INFO)
        return logger
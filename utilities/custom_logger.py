import logging

"""The logging module in Python is a built-in system for recording messages about what your program is doing while it runs. 
It’s mainly used for debugging, monitoring, and tracking errors—basically a more powerful and flexible alternative to print()."""

class Log_Maker:

    @staticmethod
    def log_gen():
        logging.basicConfig(filename = ".//logs//nopcommerce.log", format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                            datefmt="%d-%b-%y %H:%M:%S", force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


"""basicConfig usually does something like this- Set up logging with these basic rules before anything runs."""
"""getlogger() usually provides name in the log file for better understanding from where the log has come. ex - getlogger(--auth--)"""
"""setLevel defines what level of information has to be logged like error, debug, info, warning etc"""
"""logging.INFO is kind of level of logging needs to be reported in log files"""

"""A static method belongs to the class for organization, but it doesn't use either the instance (self) or the class (cls)."""
"""A class method works on the class itself, not on individual objects. You don't need an object to access class method"""
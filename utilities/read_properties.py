import configparser
"""configparser is a built-in Python module used to read and write configuration files—usually .ini files."""

config = configparser.RawConfigParser()
"""RawConfigParser is a method in configparser and it can be used when there are no interpolation/reuse of data within config.ini
file. and when we have interpolation then we have to switch to Configparser method"""

config.read("./configurations/config.ini")

class Read_Config:

    @staticmethod
    def login_url():
        url = config.get("admin login data", "url")
        return url

    @staticmethod
    def user_name():
        user = config.get("admin login data", "Username")
        return user

    @staticmethod
    def pass_word():
        pass_key = config.get("admin login data", "Password")
        return pass_key

    @staticmethod
    def in_valid():
        invalid_user_name = config.get("admin login data", "invalid_Username")
        return invalid_user_name
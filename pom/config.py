from configparser import ConfigParser


class Config(object):
    config_object = ConfigParser()
    config_object.read("pom/config.ini")

    base_url = config_object["ENV"]["host"]
    email = config_object["USERINFO"]["email"]
    password = config_object["USERINFO"]["password"]

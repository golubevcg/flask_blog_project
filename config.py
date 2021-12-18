import os


class BaseConfig:
    DEBUG = False
    TESTING = False
    ENV = "development"
    SECRET_KEY = "9OLWxND4o83j4K4iuopO"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///:memory:")

    HOST = "127.0.0.1"
    PORT = 5000


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    ENV = "production"
    HOST = "0.0.0.0"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    HOST = "0.0.0.0"


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = False

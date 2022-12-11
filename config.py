import os


class DevConfig:
    BASEDIR = os.path.abspath(os.path.dirname(__file__))


class ProdConfig:
    pass

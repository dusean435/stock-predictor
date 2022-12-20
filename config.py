import os

DATADIR = f"{os.path.abspath(os.path.dirname(__file__))}/data"

class DevConfig:
    BASEDIR = os.path.abspath(os.path.dirname(__file__))


class ProdConfig:
    pass

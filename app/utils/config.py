# GENERIC LIB
import os
import decimal
# CONTROLLERS
# MODEL
# UTILS
import app.utils.constants as const


class Config:
    ENV = os.environ.get("ENV", const.ENV.DEVELOPMENT.value)
    DEBUG = os.environ.get("ENV") != const.ENV.PRODUCTION.value
    APP_PORT = const.APP.PORT

    decimal.getcontext().rounding = decimal.ROUND_HALF_UP
    class DB:
        USER = os.environ.get("DB_USER", const.DB.USER)
        PASSWORD = os.environ.get("DB_PASSWORD", const.DB.PASSWORD)
        HOST = os.environ.get("DB_HOST", const.DB.HOST)
        DATABASE = os.environ.get("DB_DATABASE", const.DB.DATABASE)

    class TOKEN:
        SECRET_KEY = os.environ.get("SECRET_KEY", const.TOKEN.SECRET_KEY)
        ALGORITHM = os.environ.get("ALGORITHM", const.TOKEN.ALGORITHM)
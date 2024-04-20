# GENERIC LIB
from enum import Enum
from datetime import datetime
# CONTROLLERS
# MODEL
# UTILS


class APP():
    PORT = 4501

class DBNAMES():
    LIVETALENT = 'LIVETALENT'

class ENV(Enum):
    PRODUCTION = "production"
    STAGING = "staging"
    TESTING = "test"
    DEVELOPMENT = "development"

class DB():
    USER = ""
    PASSWORD = ""
    HOST = ""
    DATABASE = ""

class TOKEN():
    SECRET_KEY = "ASDKOASKDASOKDASODKASODK"
    ALGORITHM = "HS256"

class MSG():
    # ERRORS
    ERROR_TO_SAVE = "ERROR_TO_SAVE"
    ERROR_TO_LOGIN = "ERROR_TO_LOGIN"
    ERROR_AUTHENTICATION_REQUIRED = "AUTHENTICATION_REQUIRED"
    ERROR_TO_SEND_MESSAGE = "ERROR_TO_SEND_MESSAGE"
    ERROR_TOKEN_VALIDATION = "ERROR_TOKEN_VALIDATION"
    DUPLICATED_KEY_ERROR = "DUPLICATED_KEY_ERROR"
    ACTIVE_PROMOTION_NOT_FOUND = "ACTIVE_PROMOTION_NOT_FOUND"
    NOT_ENOUGH_BALANCE = "NOT_ENOUGH_BALANCE"
    NO_REMAING_MINTS = "NO_REMAING_MINTS"
    NO_NFT_AVAILABLE = "NO_NFT_AVAILABLE"
    USER_NOT_FOUND = "USER_NOT_FOUND"
    ERROR_TO_MINT = "ERROR_TO_MINT"
    
    # SUCCESS
    SUCCESS = "SUCCESS"
    CREATE_SUCCESS = "CREATE_SUCCESS"
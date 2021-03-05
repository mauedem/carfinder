from enum import Enum


class ErrorCodes(Enum):
    ACCOUNT_IS_NOT_A_VALID = 'ACCOUNT_IS_NOT_A_VALID'
    BAD_CREDENTIALS = 'BAD_CREDENTIALS'
    NOT_AUTHORIZED = 'NOT_AUTHORIZED'
    CAR_IS_NOT_A_VALID = 'CAR_IS_NOT_A_VALID'
    TRIP_IS_NOT_A_VALID = 'TRIP_IS_NOT_A_VALID'


class CoreError(BaseException):
    def __init__(self, error_code: ErrorCodes, data = None):
        self.error_code = error_code
        self.data = data

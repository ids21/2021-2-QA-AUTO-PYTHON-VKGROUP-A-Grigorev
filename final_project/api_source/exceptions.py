class BaseException(Exception):
    def __init__(self, message):    
        self.message = message

    def __str__(self):
        return self.message

class InvalidLoginException(BaseException):
    pass


class ResponseErrorException(BaseException):
    pass

class ResponseStatusCodeException(BaseException):
    pass

class ValidationError(Exception):
    pass
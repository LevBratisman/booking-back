from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

    
class UserAlreadyExistsException(BookingException):
    status_code=status.HTTP_409_CONFLICT
    detail="User already exists"


class IncorrectPasswordOrEmailException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Incorrect email or password"


class TokenDoesNotExistException(BookingException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Token does not exist"


class InvalidOrExpiredTokenException(BookingException):
    status_code=status.HTTP_403_FORBIDDEN
    detail="Could not validate credentials (Invalid Token)"


class RoomCannotBeBookedException(BookingException):
    status_code=status.HTTP_409_CONFLICT
    detail="There are not rooms left"


class BookingDeleteException(BookingException):
    status_code=status.HTTP_409_CONFLICT
    detail="You haven't permissions to delete this booking"
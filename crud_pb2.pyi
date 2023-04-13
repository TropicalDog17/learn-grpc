from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BookingDetails(_message.Message):
    __slots__ = ["booking_email", "booking_name", "date", "id", "location", "movie", "screen", "seat_number", "status"]
    BOOKING_EMAIL_FIELD_NUMBER: _ClassVar[int]
    BOOKING_NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MOVIE_FIELD_NUMBER: _ClassVar[int]
    SCREEN_FIELD_NUMBER: _ClassVar[int]
    SEAT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    booking_email: str
    booking_name: str
    date: str
    id: str
    location: str
    movie: str
    screen: str
    seat_number: int
    status: str
    def __init__(self, id: _Optional[str] = ..., movie: _Optional[str] = ..., booking_name: _Optional[str] = ..., booking_email: _Optional[str] = ..., date: _Optional[str] = ..., location: _Optional[str] = ..., screen: _Optional[str] = ..., seat_number: _Optional[int] = ..., status: _Optional[str] = ...) -> None: ...

class BookingQuery(_message.Message):
    __slots__ = ["booking_email", "booking_name", "date", "id", "location", "movie"]
    BOOKING_EMAIL_FIELD_NUMBER: _ClassVar[int]
    BOOKING_NAME_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MOVIE_FIELD_NUMBER: _ClassVar[int]
    booking_email: str
    booking_name: str
    date: str
    id: str
    location: str
    movie: str
    def __init__(self, id: _Optional[str] = ..., movie: _Optional[str] = ..., booking_name: _Optional[str] = ..., booking_email: _Optional[str] = ..., location: _Optional[str] = ..., date: _Optional[str] = ...) -> None: ...

class TestRequest(_message.Message):
    __slots__ = ["test_msg"]
    TEST_MSG_FIELD_NUMBER: _ClassVar[int]
    test_msg: str
    def __init__(self, test_msg: _Optional[str] = ...) -> None: ...

class TestResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

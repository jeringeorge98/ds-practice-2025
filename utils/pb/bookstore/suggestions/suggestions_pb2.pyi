from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OrderedBooks(_message.Message):
    __slots__ = ("user_id", "book_ids", "max_suggestions")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    BOOK_IDS_FIELD_NUMBER: _ClassVar[int]
    MAX_SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    book_ids: _containers.RepeatedScalarFieldContainer[str]
    max_suggestions: int
    def __init__(self, user_id: _Optional[str] = ..., book_ids: _Optional[_Iterable[str]] = ..., max_suggestions: _Optional[int] = ...) -> None: ...

class SuggestionsResponse(_message.Message):
    __slots__ = ("suggestions", "suggestion_id", "created_at")
    SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    SUGGESTION_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    suggestions: _containers.RepeatedCompositeFieldContainer[BookSuggestion]
    suggestion_id: str
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, suggestions: _Optional[_Iterable[_Union[BookSuggestion, _Mapping]]] = ..., suggestion_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BookSuggestion(_message.Message):
    __slots__ = ("book_id", "title", "author", "price", "currency", "matching_categories", "description")
    BOOK_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    MATCHING_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    book_id: str
    title: str
    author: str
    price: float
    currency: str
    matching_categories: _containers.RepeatedScalarFieldContainer[str]
    description: str
    def __init__(self, book_id: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., price: _Optional[float] = ..., currency: _Optional[str] = ..., matching_categories: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ...) -> None: ...

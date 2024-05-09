from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTodoRequest(_message.Message):
    __slots__ = ("name", "completed")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    name: str
    completed: bool
    def __init__(self, name: _Optional[str] = ..., completed: bool = ...) -> None: ...

class ReadTodoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class UpdateTodoRequest(_message.Message):
    __slots__ = ("id", "name", "completed")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    completed: bool
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., completed: bool = ...) -> None: ...

class DeleteTodoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class ListTodosRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

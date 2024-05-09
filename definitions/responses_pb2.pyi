import todo_pb2 as _todo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTodoResponse(_message.Message):
    __slots__ = ("todo",)
    TODO_FIELD_NUMBER: _ClassVar[int]
    todo: _todo_pb2.Todo
    def __init__(self, todo: _Optional[_Union[_todo_pb2.Todo, _Mapping]] = ...) -> None: ...

class ReadTodoResponse(_message.Message):
    __slots__ = ("todo",)
    TODO_FIELD_NUMBER: _ClassVar[int]
    todo: _todo_pb2.Todo
    def __init__(self, todo: _Optional[_Union[_todo_pb2.Todo, _Mapping]] = ...) -> None: ...

class UpdateTodoResponse(_message.Message):
    __slots__ = ("todo",)
    TODO_FIELD_NUMBER: _ClassVar[int]
    todo: _todo_pb2.Todo
    def __init__(self, todo: _Optional[_Union[_todo_pb2.Todo, _Mapping]] = ...) -> None: ...

class DeleteTodoResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ListTodosResponse(_message.Message):
    __slots__ = ("todos",)
    TODOS_FIELD_NUMBER: _ClassVar[int]
    todos: _containers.RepeatedCompositeFieldContainer[_todo_pb2.Todo]
    def __init__(self, todos: _Optional[_Iterable[_Union[_todo_pb2.Todo, _Mapping]]] = ...) -> None: ...

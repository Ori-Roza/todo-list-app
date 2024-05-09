# an example of using gRPC. a todolist app
import dataclasses
import typing
from typing import Optional


@dataclasses.dataclass
class Todo:
    id: int
    name: str
    completed: bool


class TodoTable:
    def __init__(self):
        self._objects = {}
        self._last_id = 1

    def all(self) -> typing.List[Todo]:
        return [todo.__dict__ for id, todo in self._objects.items()]

    def create(self, name: str, completed: bool) -> Todo:
        self._objects[self._last_id] = Todo(id=self._last_id,
                                            name=name,
                                            completed=completed)
        todo = self._objects[self._last_id]
        self._last_id += 1
        return todo

    def read(self, id: int) -> Todo:
        return self._objects[id]

    def update(self, id: int, name: Optional[str], completed: Optional[bool]) -> Todo:
        todo = self.read(id)

        if name:
            todo.name = name

        if completed is not None:
            todo.completed = completed

        self._objects[id] = todo

        return self._objects[id]

    def delete(self, id: int) -> bool:
        todo = self.read(id)
        if not todo:
            return False
        del self._objects[id]
        return True


todo_table = TodoTable()

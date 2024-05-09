import logging
from concurrent import futures

import grpc
import definitions.responses_pb2 as responses_pb2
import definitions.todo_service_pb2_grpc as todo_service_pb2_grpc

from todo_orm import todo_table


class Todo(todo_service_pb2_grpc.TodoServiceServicer):
    def CreateTodo(self, request, context):
        todo = todo_table.create(name=request.name,
                                 completed=request.completed)
        return responses_pb2.CreateTodoResponse(todo=todo.__dict__)

    def ReadTodo(self, request, context):
        todo = todo_table.read(id=request.id)
        return responses_pb2.ReadTodoResponse(todo=todo.__dict__)

    def UpdateTodo(self, request, context):
        todo = todo_table.update(id=request.id,
                                 name=request.name,
                                 completed=request.completed)
        return responses_pb2.UpdateTodoResponse(todo=todo.__dict__)

    def DeleteTodo(self, request, context):
        success = todo_table.delete(id=request.id)
        return responses_pb2.DeleteTodoResponse(success=success)

    def ListTodos(self, request, context):
        list_of_todos = todo_table.all()
        return responses_pb2.ListTodosResponse(todos=list_of_todos)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_service_pb2_grpc.add_TodoServiceServicer_to_server(Todo(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

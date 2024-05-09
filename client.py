import grpc
import definitions.requests_pb2 as requests_pb2
import definitions.todo_service_pb2_grpc as todo_pb2_grpc
from google.protobuf.json_format import MessageToDict


def connect_client():
    channel = grpc.insecure_channel("localhost:50051")
    return todo_pb2_grpc.TodoServiceStub(channel)


if __name__ == '__main__':
    client_stub = connect_client()
    print('all')
    todos = client_stub.ListTodos(requests_pb2.ListTodosRequest())
    print(MessageToDict(todos))
    print('create')
    todo = client_stub.CreateTodo(requests_pb2.CreateTodoRequest(name='first', completed=False))
    todo = MessageToDict(todo)['todo']
    print(todo)
    print("all")
    todos = client_stub.ListTodos(requests_pb2.ListTodosRequest())
    print(MessageToDict(todos))
    print("update")
    success = client_stub.UpdateTodo(requests_pb2.UpdateTodoRequest(id=todo["id"], completed=True))
    print(MessageToDict(success))
    print("read")
    todo = client_stub.ReadTodo(requests_pb2.ReadTodoRequest(id=todo["id"]))
    todo = MessageToDict(todo)['todo']
    print(todo)
    print("delete")
    todo = client_stub.DeleteTodo(requests_pb2.DeleteTodoRequest(id=todo["id"]))
    todo = MessageToDict(todo)
    print(todo)
    print("all")
    todos = client_stub.ListTodos(requests_pb2.ListTodosRequest())
    print(MessageToDict(todos))

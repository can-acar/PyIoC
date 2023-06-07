from container_builder import ContainerBuilder
from resolve import resolve
from scope import Scope

class ExampleClass:
    def hello(self):
        return "Hello, world!"


@resolve(ExampleClass)
def example_function(exampleclass: ExampleClass):
    return exampleclass.hello()


if __name__ == '__main__':
    builder = ContainerBuilder()
    builder.register(ExampleClass, scope=Scope.SINGLETON)
    container = builder.build()

    print(example_function())

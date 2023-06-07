from container_builder import ContainerBuilder
from Example3 import Example3
from example_class import ExampleClass
from resolve import resolve
from sample_class import SampleClass
from scope import Scope
from validate import validate


@resolve(ExampleClass, Example3)
def example_function(example: ExampleClass, request: Example3):
    temp = request;
    return example.hello()


if __name__ == '__main__':
    builder = ContainerBuilder()
    builder.register(SampleClass, scope=Scope.TRANSIENT)
    builder.register(ExampleClass, scope=Scope.SINGLETON)
    builder.register(Example3, scope=Scope.REQUEST)

    container = builder.build()

    print(example_function())

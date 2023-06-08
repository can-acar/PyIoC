from container_builder import ContainerBuilder
from Example3 import Example3
from example_class import ExampleClass
from resolve import resolve
from sample_class import SampleClass
from scope import Scope
from validate import validate


@resolve(ExampleClass, Example3)
def example_function(example: ExampleClass, request: Example3):
    test_key = request.test_key
    test_value = request.test_value
    return example.hello()


if __name__ == '__main__':
    builder = ContainerBuilder()
    sampleInstance = SampleClass()
    builder.register_instance(sampleInstance)
    builder.register(Example3, scope=Scope.REQUEST)
    builder.register(ExampleClass, scope=Scope.TRANSIENT)

    container = builder.build()

    print(example_function())

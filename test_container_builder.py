import unittest

from app_module import AppModule
from container_builder import ContainerBuilder
from Example3 import Example3
from example_class import ExampleClass
from lib.scope import Scope
from module import Module
from resolve import resolve
from sample_class import SampleClass


class TestContainerBuilder(unittest.TestCase):
    def test_register(self):
        builder = ContainerBuilder()
        builder.register(SampleClass, Scope.TRANSIENT)
        builder.register(ExampleClass, Scope.TRANSIENT)
        container = builder.build()

        instance = container.resolve(ExampleClass)
        instance2 = container.resolve(SampleClass)
        self.assertIsInstance(instance, ExampleClass)
        self.assertIsInstance(instance2, SampleClass)

    def test_register_type(self):
        builder = ContainerBuilder()
        builder.register_type(SampleClass, SampleClass, Scope.TRANSIENT)
        container = builder.build()

        instance = container.resolve(SampleClass)
        self.assertIsInstance(instance, SampleClass)

    #
    def test_register_instance(self):
        builder = ContainerBuilder()
        sampleInstance = SampleClass()
        builder.register_instance(sampleInstance)
        builder.register(Example3, scope=Scope.REQUEST)
        builder.register(ExampleClass, scope=Scope.TRANSIENT)
        container = builder.build()

        example_instance = container.resolve(ExampleClass)
        result = example_instance.hello()

        self.assertIs("SampleClass", result)
    #
    def test_register_module(self):
        builder = ContainerBuilder()
        module = AppModule()
        builder.register_module(module)
        container = builder.build()

        example_instance = container.resolve(ExampleClass)
        result = example_instance.hello()

        self.assertIs("SampleClass", result)
    #
    def test_resolve(self):
        builder = ContainerBuilder()
        sampleInstance = SampleClass()
        builder.register_instance(sampleInstance)
        builder.register(Example3, scope=Scope.REQUEST)
        builder.register(ExampleClass, scope=Scope.TRANSIENT)
        container = builder.build()

        @resolve(ExampleClass)
        def example_function(exampleclass: ExampleClass):
            return exampleclass.hello()

        result = example_function()
        self.assertEqual(result, "SampleClass")


if __name__ == '__main__':
    unittest.main()

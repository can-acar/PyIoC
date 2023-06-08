from Example3 import Example3
from example_class import ExampleClass
from lib.container_builder import ContainerBuilder
from lib.module import Module
from sample_class import SampleClass
from scope import Scope


class AppModule(Module):

    def load(self, builder: ContainerBuilder):
        sampleInstance = SampleClass()
        builder.register_instance(sampleInstance)
        builder.register(Example3, scope=Scope.REQUEST)
        builder.register(ExampleClass, scope=Scope.TRANSIENT)


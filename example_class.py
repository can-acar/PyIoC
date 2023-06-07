from inject import inject
from resolve import resolve
from sample_class import SampleClass


@inject
class ExampleClass:
    def __init__(self, spc: SampleClass):
        self.spc = spc;

    def hello(self):
        return self.spc.test_message()

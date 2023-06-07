import functools
import inspect
from typing import Any
from typing import Callable
from typing import List
from typing import Union

from lib.container_builder import ContainerBuilder


def inject(cls: Union[Any, List[Any]]) -> Callable:
    if not isinstance(cls, list):
        cls = [cls]

    def decorator(original_class):
        orig_init = original_class.__init__

        @functools.wraps(original_class.__init__)
        def __init__(self, *args, **kwargs):
            container = ContainerBuilder.instance()
            for dependency in cls:
                instance = container.resolve(dependency)
                kwargs[dependency.__name__.lower()] = instance
            orig_init(self, *args, **kwargs)

        original_class.__init__ = __init__
        return original_class

    return decorator

# def inject(cls: Union[Any, List[Any]]) -> Callable:
#     if not isinstance(cls, list):
#         cls = [cls]
#
#     def decorator(target):
#         if not inspect.isclass(target) and not inspect.ismethod(target):
#             raise TypeError("The @inject decorator can only be used with classes and class methods")
#
#         sig = inspect.signature(target)
#
#         @functools.wraps(target)
#         def wrapper(*args, **kwargs):
#             container = ContainerBuilder.instance()
#             for name, param in sig.parameters.items():
#                 if name not in kwargs and param.annotation in cls:
#                     kwargs[name] = container.resolve(param.annotation)
#             return target(*args, **kwargs)
#
#         return wrapper
#
#     return decorator

# def inject(cls: Union[Any, List[Any]]) -> Callable:
#     """
#     Decorator to inject dependencies into a function or method.
#     """
#     if not isinstance(cls, list):
#         cls = [cls]
#
#     def decorator(func: Callable) -> Callable:
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             container = ContainerBuilder.instance()
#
#             sig = signature(func)
#             for name, param in sig.parameters.items():
#                 if name not in kwargs and param.annotation in cls:
#                     kwargs[name] = container.resolve(param.annotation)
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return decorator

# class inject:
#     def __init__(self, types: Union[type, List[type]]):
#         if not isinstance(types, list):
#             types = [types]
#         self.types = types
#
#     def __call__(self, cls):
#         sig = inspect.signature(cls.__init__)
#         types_dict = dict(zip(sig.parameters, self.types))
#
#         @functools.wraps(cls)
#         def wrapper(*args, **kwargs):
#             container = ContainerBuilder.instance()
#             for name, param in sig.parameters.items():
#                 if name not in kwargs and param.annotation in types_dict:
#                     kwargs[name] = container.resolve(param.annotation)
#             return cls(*args, **kwargs)
#
#         return wrapper

# def inject(cls):
#
#
#     @wraps(cls)
#     def wrapper(*args, **kwargs):
#         constructor = cls.__init__
#         params = inspect.signature(constructor).parameters
#         deps = {name: param.annotation for name, param in params.items() if param.annotation != param.empty}
#         container = ContainerBuilder.instance()
#         resolved = {name: container.resolve(dep) for name, dep in deps.items()}
#         return cls(*args, **resolved, **kwargs)
#
#     return wrapper

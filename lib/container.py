import inspect
from typing import Generic
from typing import List
from typing import Type
from typing import TypeVar

from container_entry import ContainerEntry
from lib.scope import Scope

T = TypeVar('T')


class Container():

    def __init__(self, registry: List[ContainerEntry]):
        self._registry = registry

    def resolve(self, member_type: Generic[T]) -> T:
        for entry in self._registry:
            if entry.cls is member_type or isinstance(entry.cls, member_type) or isinstance(entry.instance, member_type):
                if entry.scope == Scope.SINGLETON:
                    if not entry.instance:
                        entry.instance = self._create_instance(entry.cls)
                        return entry.instance
                    if entry.instance:
                        return entry.instance
                if entry.scope == Scope.REQUEST:
                    if not entry.instance:
                        entry.instance = self._create_instance(entry.cls)
                        return entry.instance
                    return entry.instance
                else:  # Scope.TRANSIENT
                    return self._create_instance(entry.cls)
        raise ValueError(f"No member of type {member_type} registered")

    def _create_instance(self, component: type) -> object:
        params = inspect.signature(component).parameters
        if not params:
            return component()
        dependencies = {
            name: self.resolve(param.annotation)
            for name, param in params.items()
            if param.annotation != inspect.Parameter.empty
        }
        return component(**dependencies)

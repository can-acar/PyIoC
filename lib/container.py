import inspect
from typing import List
from typing import Type
from typing import TypeVar

from container_entry import ContainerEntry
from lib.scope import Scope

T = TypeVar('T')


class Container():

    def __init__(self, registry: List[ContainerEntry]):
        self._registry = registry

    def resolve(self, member_types: Type[T]) -> T:
        for entry in self._registry:
            if isinstance(entry.cls, member_types):
                if entry.scope == Scope.SINGLETON:
                    if not entry.instance:
                        entry.instance = self._create_instance(entry.cls)
                    return entry.instance
                else:  # Scope.TRANSIENT
                    return self._create_instance(entry.cls)
        raise ValueError(f"No member of type {member_types} registered")

    def _create_instance(self, component: type) -> object:
        params = inspect.signature(component).parameters
        if not params:
            return component()
        dependencies = {name: self.resolve(param.annotation) for name, param in params.items()}
        return component(**dependencies)

    # member_entry = next((x for x in self._registry if x.cls == member_types), None)
    # if not member_entry:
    #     raise ValueError(f"Member of type {member_entry} not registered")
    # if member_entry.scope == Scope.SINGLETON:
    #     if not member_entry.instance:
    #         member_entry.instance = self._create_instance(member_entry.cls)
    #     return member_entry.instance

    # member_entry = self._registry.get(member_types)
    # if not member_entry:
    #     raise ValueError(f"Member of type {member_entry} not registered")
    # if member_entry["scope"] == Scope.SINGLETON:
    #     if member_entry not in self._registry:
    #         self._registry[member_entry] = self._create_instance(member_entry["cls"])
    #     return self._registry[member_entry]
    # else:  # Scope.TRANSIENT
    #     return self._create_instance(member_entry["cls"])

    # params = inspect.signature(component).parameters
    # if not params:
    #     return component()
    # dependencies = {param: self.resolve(param.annotation) for param, param in params.items()}
    # return component(**dependencies)

    # get static instance of container_builder

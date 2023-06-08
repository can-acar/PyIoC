# PyIoC
 
IoC library for Python, similar to C# Autofac

C# Autofac benzeri, Python için IoC kütüphanesi

## Yapılar

Proje aşağıdaki yapıları içermektedir:

- `ContainerBuilder`: Bağımlılıkların kaydedilmesi ve çözünürlüğünün sağlanması için kullanılan sınıf.
- `Container`: Bağımlılıkların çözünürlüğünü sağlayan ve kayıtları tutan sınıf.
- `inject` ve `resolve` dekoratörleri: Bağımlılıkların otomatik enjeksiyonunu gerçekleştiren dekoratörler.
- `ContainerEntry`: Bağımlılık kayıtlarını temsil eden sınıf.
- `Scope`: Bağımlılıkların kapsamını belirten bir sıralı veri tipi.
- `Module`: Bağımlılık enjeksiyonunu kolaylaştırmak için kullanılan soyut bir sınıf.




EN
The project includes the following structures:

- `ContainerBuilder`: A class used for registering and resolving dependencies.
- `Container`: A class that provides dependency resolution and holds the registrations.
- `inject` and `resolve` decorators: Decorators that enable automatic injection of dependencies.
- `ContainerEntry`: A class that represents a dependency registration.
- `Scope`: An enumeration that specifies the scope of dependency registrations.
- `Module`: An abstract class used to facilitate dependency injection.
-----------------------------------------------------------------



```python
from typing import List
from typing import TypeVar

from container_entry import ContainerEntry
from lib.container import Container
from lib.scope import Scope
from singleton import Singleton


```python
from typing import List
from typing import TypeVar

from container_entry import ContainerEntry
from lib.container import Container
from lib.scope import Scope
from singleton import Singleton

class ExampleClass:
    def hello(self):
        return "Hello, world!"
        
builder = ContainerBuilder()
builder.register(ExampleClass, scope=Scope.TRANSIENT)
container = builder.build()

example_instance = container.resolve(ExampleClass)
print(example_instance.hello())  # Output: Hello, world!
````
```python

class ExampleClass:
    def hello(self):
        return "Hello, world!"

@resolve(ExampleClass)
def example_function(example_instance: ExampleClass):
    return example_instance.hello()

builder = ContainerBuilder()
builder.register(ExampleClass, scope=Scope.SINGLETON)
container = builder.build()

print(example_function())  # Output: Hello, world!
```

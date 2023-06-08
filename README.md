# PyIoC
 
IoC library for Python, similar to C# Autfac

C# Autfac benzeri, Python için IoC kütüphanesi

## Yapılar

Proje aşağıdaki yapıları içermektedir:

- `ContainerBuilder`: Bağımlılıkların kaydedilmesi ve çözünürlüğünün sağlanması için kullanılan sınıf.
- `Container`: Bağımlılıkların çözünürlüğünü sağlayan ve kayıtları tutan sınıf.
- `inject` ve `resolve` dekoratörleri: Bağımlılıkların otomatik enjeksiyonunu gerçekleştiren dekoratörler.
- `ContainerEntry`: Bağımlılık kayıtlarını temsil eden sınıf.
- `Scope`: Bağımlılıkların kapsamını belirten bir sıralı veri tipi.
- `Module`: Bağımlılık enjeksiyonunu kolaylaştırmak için kullanılan soyut bir sınıf.

## Örnek Kodlar

### Bağımlılık Enjeksiyonu Kullanarak Sınıf Oluşturma
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

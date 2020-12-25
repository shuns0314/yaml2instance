# yaml2instance
From the list of modules, find the class or function written in yaml and call(instantiate) it.

## install
```
pip install yaml2instace
```

## example

modules.py
```
class ExampleClass:
    def __init__(self, args: str):
        self.args = args

    def hoge(self):
        print(self.args)
```

example.yaml
```
example:
  ExampleClass:
    args: hoge
```


example.py
```
import yaml
from yaml2instance.main import call_single

import modules

with open("example.yaml") as file:
    example = yaml.safe_load(file)

example_class_instance = call_single(example['example'], [modules])
example_class_instance.hoge()
```

output
```
hoge
```

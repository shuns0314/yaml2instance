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
from yaml2instance.main import yaml2instances

import modules

with open("example.yaml") as file:
    example = yaml.safe_load(file)

example_class_instance = yaml2instances(example['example'], [modules])[0]
example_class_instance.hoge()
```

output
```
hoge
```

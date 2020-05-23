"""Dummy class for test."""


class DummyClass2:
    def __init__(self, args_1: int, args_2: int, **kwargs):
        self.args_1 = args_1
        self.args_2 = args_2

    def minus(self):
        return self.args_1 - self.args_2


class DummyClass3:
    def __init__(self, args_3: int, args_4: int, **kwargs):
        self.args_3 = args_3
        self.args_4 = args_4

    def minus(self):
        return self.args_3 - self.args_4

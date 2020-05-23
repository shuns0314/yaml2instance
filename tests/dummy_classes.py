"""Dummy class for test."""


class DummyClass:
    def __init__(self, args_1: int, args_2: int, **kwargs):
        self.args_1 = args_1
        self.args_2 = args_2

    def add(self):
        return self.args_1 + self.args_2

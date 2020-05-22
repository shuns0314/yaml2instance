import yaml

from yaml2instance.main import yaml2instances
from tests import dummy_classes


def test_load_yaml():
    with open("tests/dummy.yaml") as file:
        obj = yaml.safe_load(file)
    assert obj["test_normal"] == {"DummyClass": {"args_1": 1, "args_2": 2}}
    assert obj["test_double"] == {
        "DummyClass": {"args_1": 1, "args_2": 2},
        "DummyClass2": {"args_1": 2, "args_2": 2},
    }
    assert obj["test_list"] == [
        {"DummyClass": {"args_1": 1, "args_2": 2}},
        {"DummyClass": {"args_1": 1, "args_2": 2}},
    ]


def test_single():
    dummpy_config = {"DummyClass": {"args_1": 1, "args_2": 2}}
    dummy_list = yaml2instances(dummpy_config, search_modules=[dummy_classes])
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()


def test_another_name_multi():
    dummpy_config = {
        "DummyClass": {"args_1": 1, "args_2": 2},
        "DummyClass2": {"args_1": 2, "args_2": 2},
    }
    dummy_list = yaml2instances(dummpy_config, search_modules=[dummy_classes])
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()
    assert (
        dummy_list[1].minus() == dummy_classes.DummyClass2(args_1=2, args_2=2).minus()
    )


def test_same_name_multi():
    dummpy_config = [
        {"DummyClass": {"args_1": 1, "args_2": 2}},
        {"DummyClass": {"args_1": 1, "args_2": 2}},
    ]
    dummy_list = yaml2instances(dummpy_config, search_modules=[dummy_classes])
    assert dummy_list != []
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()
    assert dummy_list[1].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()


def test_single_add_kwargs():
    dummpy_config = {"DummyClass": {"args_2": 2}}
    dummy_list = yaml2instances(dummpy_config, search_modules=[dummy_classes], args_1=1)
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()


def test_single_add_kwargs2():
    dummpy_config = {"DummyClass": {"args_1": 1, "args_2": 2}}
    dummy_list = yaml2instances(dummpy_config, search_modules=[dummy_classes], args_1=2)
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()

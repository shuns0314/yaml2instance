import yaml

from yaml2instance.main import call_multiple, call_single
from tests import dummy_classes, dummy_classes2


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
    dummy_config = {"DummyClass": {"args_1": 1, "args_2": 2}}
    module_list = [dummy_classes, dummy_classes2]
    dummy_list = call_multiple(dummy_config, search_modules=module_list)
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()


def test_another_name_multi():
    dummy_config = {
        "DummyClass": {"args_1": 1, "args_2": 2},
        "DummyClass2": {"args_1": 2, "args_2": 2},
    }
    module_list = [dummy_classes, dummy_classes2]
    dummy_list = call_multiple(dummy_config, search_modules=module_list)
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()
    assert (
        dummy_list[1].minus() == dummy_classes2.DummyClass2(args_1=2, args_2=2).minus()
    )


def test_same_name_multi():
    dummy_config = [
        {"DummyClass": {"args_1": 1, "args_2": 2}},
        {"DummyClass": {"args_1": 1, "args_2": 2}},
    ]
    module_list = [dummy_classes, dummy_classes2]
    dummy_list = call_multiple(dummy_config, search_modules=module_list)
    assert dummy_list != []
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()
    assert dummy_list[1].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()


def test_single_add_kwargs():
    dummy_config = {"DummyClass": {"args_2": 2}}
    module_list = [dummy_classes, dummy_classes2]
    dummy_list = call_multiple(dummy_config, search_modules=module_list, args_1=1)
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()


def test_single_add_kwargs2():
    dummy_config = {"DummyClass": {"args_1": 1, "args_2": 2}}
    module_list = [dummy_classes, dummy_classes2]
    dummy_list = call_multiple(dummy_config, search_modules=module_list, args_1=2)
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()


def test_another_name_multi_2():
    dummy_config = {
        "DummyClass": {"args_1": 1, "args_2": 2},
        "DummyClass3": {"args_3": 2, "args_4": 2},
    }
    module_list = [dummy_classes, dummy_classes2]
    dummy_list = call_multiple(dummy_config, search_modules=module_list)
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()
    assert (
        dummy_list[1].minus() == dummy_classes2.DummyClass3(args_3=2, args_4=2).minus()
    )


def test_another_name_multi_3():
    dummy_config = [
        {"DummyClass": {"args_1": 1, "args_2": 2}},
        {"DummyClass3": {"args_3": 2, "args_4": 2}},
    ]
    module_list = [dummy_classes, dummy_classes2]
    dummy_list = call_multiple(dummy_config, search_modules=module_list)
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()
    assert (
        dummy_list[1].minus() == dummy_classes2.DummyClass3(args_3=2, args_4=2).minus()
    )


def test_another_name_multi_kwargs():
    dummy_config = {
        "DummyClass": {"args_2": 2},
        "DummyClass3": {"args_3": 2, "args_4": 2},
    }
    module_list = [dummy_classes, dummy_classes2]
    dummy_list = call_multiple(dummy_config, search_modules=module_list, args_1=1)
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()
    assert (
        dummy_list[1].minus() == dummy_classes2.DummyClass3(args_3=2, args_4=2).minus()
    )


def test_non_kwargs():
    dummy_config = {
        "DummyClass": None,
    }
    module_list = [dummy_classes, dummy_classes2]
    dummy_list = call_multiple(dummy_config, search_modules=module_list)
    assert dummy_list[0].add() == dummy_classes.DummyClass(args_1=100, args_2=100).add()


def test_call_single_1():
    dummy_config = {"DummyClass": {"args_1": 1, "args_2": 2}}
    module_list = [dummy_classes, dummy_classes2]
    dummy_list = call_single(dummy_config, search_modules=module_list, args_1=2)
    assert dummy_list.add() == dummy_classes.DummyClass(args_1=1, args_2=2).add()

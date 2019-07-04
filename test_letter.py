## Tests for key woradd_leadership_globalds filter logic
# All of the rest logic was attributed from Prof. Rossetti, git username: s2t2.

from letter import add_communication
from letter import add_leadership_global
from letter import add_software
from letter import add_time_management


def test_add_communication():
    example_list = ["communication", "analytical"]
    example_skill = "data"
    assert add_communication(example_list, example_skill) == ["communication", "analytical", "data"]
    

def test_add_leadership_global():
    list_1 = ["a", "b", "c"]
    item_1 = "d" 
    assert add_leadership_global(list_1, item_1) == ["a", "b", "c", "d"]


def test_add_software():
    list_2 = [1, 2, 3]
    item_2 = 4
    assert add_software(list_2, item_2) == [1, 2, 3, 4]

def test_add_time_management():
    list_3 = [{1},{2},{3}]
    item_3 = {4}
    assert add_time_management(list_3, item_3) == [{1},{2},{3},{4}]
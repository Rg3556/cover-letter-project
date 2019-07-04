## Tests for key words filter logic

from letter import add_communication


def test_add_communication():
    example_list = ["communication", "analytical"]
    example_skill = "data"
    assert add_communication(example_list, example_skill) == ["communication", "analytical", "data"]
    
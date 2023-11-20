"""Testing Dictionary Functions."""

__author__ = "730597416"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# Unit tests for invert function.
def test_invert_use_case_1() -> None:
    """Test invert function with a use case."""
    input_dict = {'Alyssa': 'Green', 'Bob': 'White', 'Coco': 'Pink'}
    expected_output = {'Green': 'Alyssa', 'White': 'Bob', 'Pink': 'Coco'}
    assert invert(input_dict) == expected_output


def test_invert_use_case_2() -> None:
    """Test invert function with a use case."""
    input_dict = {'Rachel': 'Blue', 'Susan': 'White', 'Callie': 'Pink'}
    expected_output = {'Blue': 'Rachel', 'White': 'Susan', 'Pink': 'Callie'}
    assert invert(input_dict) == expected_output


def test_invert_edge_case() -> None:
    """Test invert function with an edge case."""
    input_dict = {}
    result = {}
    assert invert(input_dict) == result


# Unit tests for count function.
def test_count_use_case_1() -> None:
    """Test count function with a use case."""
    value_list = ['apple', 'banana', 'apple', 'strawberry', 'banana']
    expected_output = {'apple': 2, 'banana': 2, 'strawberry': 1}
    assert count(value_list) == expected_output


def test_count_use_case_2() -> None:
    """Test count function with a use case."""
    value_list = ['red', 'green', 'blue', 'green', 'yellow', 'red', 'green']
    expected_output = {'red': 2, 'green': 3, 'blue': 1, 'yellow': 1}
    assert count(value_list) == expected_output


def test_count_edge_case() -> None:
    """Test count function with an edge case."""
    value_list: list[str] = []
    expected_output: dict[str, int] = {}
    assert count(value_list) == expected_output


# Unit tests for favorite_color function.
def test_favorite_color_use_case_1() -> None:
    """Test favorite_color function with a use case."""
    color_dict = {'Alyssa': 'Green', 'Bob': 'Blue', 'Coco': 'Green'}
    expected_output = 'Green'
    assert favorite_color(color_dict) == expected_output


def test_favorite_color_use_case_2() -> None:
    """Test favorite_color function with a use case."""
    color_dict = {'Alice': 'Purple', 'Bob': 'Green', 'Coco': 'Purple'}
    expected_output = 'Purple'
    assert favorite_color(color_dict) == expected_output


def test_favorite_color_edge_case() -> None:
    """Test favorite_color function with an edge case."""
    color_dict: dict[str, str] = {}
    expected_output = ''
    assert favorite_color(color_dict) == expected_output


# Unit tests for alphabetizer function.
def test_alphabetizer_use_case_1() -> None:
    """Test alphabetizer function with a use case."""
    word_list = ['apple', 'banana', 'cherry', 'dragonfruit']
    expected_output = {'a': ['apple'], 'b': ['banana'], 'c': ['cherry'], 'd': ['dragonfruit']}
    assert alphabetizer(word_list) == expected_output


def test_alphabetizer_use_case_2() -> None:
    """Test alphabetizer function with a use case."""
    word_list = ['zebra', 'x-ray', 'yogurt', 'zoom', 'xmas']
    expected_output = {'z': ['zebra', 'zoom'], 'x': ['x-ray', 'xmas'], 'y': ['yogurt']}
    assert alphabetizer(word_list) == expected_output


def test_alphabetizer_edge_case() -> None:
    """Test alphabetizer function with an edge case."""
    word_list: list[str] = []
    expected_output: dict[str, list[str]] = {}
    assert alphabetizer(word_list) == expected_output


# Unit tests for update_attendance function.
def test_update_attendance_use_case_1() -> None:
    """Test update_attendance function with a use case."""
    attendance = {'Monday': ['Alyssa', 'Bob'], 'Tuesday': ['Coco']}
    day_of_week = 'Monday'
    student_name = 'David'
    expected_output = {'Monday': ['Alyssa', 'Bob', 'David'], 'Tuesday': ['Coco']}
    assert update_attendance(attendance, day_of_week, student_name) == expected_output


def test_update_attendance_use_case_2() -> None:
    """Test update_attendance function with a use case."""
    attendance = {'Monday': ['Alyssa', 'Bob'], 'Wednesday': ['Evelyn']}
    day_of_week = 'Tuesday'
    student_name = 'Frank'
    expected_output = {'Monday': ['Alyssa', 'Bob'], 'Wednesday': ['Evelyn'], 'Tuesday': ['Frank']}
    assert update_attendance(attendance, day_of_week, student_name) == expected_output


def test_update_attendance_edge_case() -> None:
    """Test update_attendance function with an edge case."""
    attendance = {}
    day_of_week = 'Monday'
    student_name = 'Alyssa'
    expected_output = {'Monday': ['Alyssa']} 
    assert update_attendance(attendance, day_of_week, student_name) == expected_output
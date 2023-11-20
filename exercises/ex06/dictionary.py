"""Dictionary Functions."""

__author__ = 730597416


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """A dictionary of inverted key-value pairs."""
    output_dict = {}
    for key, value in input_dict.items():
        if value in output_dict:
            raise KeyError(f"{value} is already in the dictionary.")
        else:
            output_dict[value] = key
    return output_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """The most popular color."""
    color_count: dict[str, int] = {}
    most_popular_color: str = ""
    most_popular_color_count: int = 0

    for name, color in color_dict.items():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    
        if color_count[color] > most_popular_color_count or (color_count[color] == most_popular_color_count and color < most_popular_color):
            most_popular_color = color
            most_popular_color_count = color_count[color]
    return most_popular_color


def count(value_list: list[str]) -> dict[str, int]:
    """A dictionary of the counts of each of the items in the input list."""
    counts: dict[str, int] = {}
    for item in value_list:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """A dictionary of the letters and the lists of words that belong to that letter."""
    categories: dict[str, list[str]] = {}
    for word in word_list:
        first_letter = word[0].lower()
        if first_letter in categories:
            categories[first_letter].append(word)
        else:
            categories[first_letter] = [word]
    return categories


def update_attendance(attendance: dict[str, list[str]], day_of_week: str, student_name: str) -> dict[str, list[str]]:
    """Updated attendance log."""
    if day_of_week in attendance:
        if student_name not in attendance[day_of_week]:
            attendance[day_of_week].append(student_name)
    else:
        attendance[day_of_week] = [student_name]
    return attendance
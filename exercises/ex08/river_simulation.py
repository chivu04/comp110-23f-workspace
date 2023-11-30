"""Simulate a river ecosystem with fish and bears."""

from exercises.ex08.river import River

__author__ = "730597416"

my_river = River(num_fish=10, num_bears=2)
my_river.view_river()
my_river.one_river_week()

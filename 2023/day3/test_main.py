"""Test day3 functions."""
from main import parse_schematic


def test_basic_part_no():
    filename = "input.txt"
    lines = [line.rstrip() for line in open(filename, "r")]

    result = parse_schematic(lines)
    assert result == 4361


def test_basic_part_no_2():
    filename = "input2.txt"
    lines = [line.rstrip() for line in open(filename, "r")]

    result = parse_schematic(lines)
    assert result == 4361


def test_part_no_solution():
    filename = "input3.txt"
    lines = [line.rstrip() for line in open(filename, "r")]

    result = parse_schematic(lines)
    assert result == 521515


def test_gear_ratio_basic():
    filename = "input.txt"
    lines = [line.rstrip() for line in open(filename, "r")]

    result = parse_schematic(lines, gear_ratio=True)
    assert result == 467835


def test_gear_ratio_solution():
    filename = "input3.txt"
    lines = [line.rstrip() for line in open(filename, "r")]

    result = parse_schematic(lines, gear_ratio=True)
    assert result == 69527306


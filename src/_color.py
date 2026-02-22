"""
Copyright (C) 2025, CEA

This program is free software; you can redistribute it and/or modify
it under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License.

You should have received a copy of the license along with this
program. If not, see <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
"""

class BColors:
    HEADER: str = '\033[95m'
    OKBLUE: str = '\033[94m'
    OKCYAN: str = '\033[96m'
    OKGREEN: str = '\033[92m'
    WARNING: str = '\033[93m'
    FAIL: str = '\033[91m'
    ENDC: str = '\033[0m'
    BOLD: str = '\033[1m'
    UNDERLINE: str = '\033[4m'

def color(string: str, color: str) -> str:
    """
    Colors a string according to the given color parameter.

    Args:
        string: The string to be colored.
        color: The color to use. Can be one of "green" ("g"), "blue" ("b"), "cyan" ("c"), "red" ("r"), or "yellow" ("y").

    Returns:
        The colored string.
    """
    color = color.lower()
    match color:
        case "g" | "green":
            return f"{BColors.OKGREEN}{string}{BColors.ENDC}"

        case "b" | "blue":
            return f"{BColors.OKBLUE}{string}{BColors.ENDC}"

        case "c" | "cyan":
            return f"{BColors.OKCYAN}{string}{BColors.ENDC}"

        case "r" | "red":
            return f"{BColors.FAIL}{string}{BColors.ENDC}"

        case "y" | "yellow":
            return f"{BColors.WARNING}{string}{BColors.ENDC}"

        case _:
            return string

from typing import Set
import re

WHITESPACE: Set[str] = {" ", r"\n", r"\t", r"\;", r"\\", r"\hfill", r"\break"}
LETTERS: str = r"[a-zA-Z\\;]"
NUMBER: str = r"\d+"
SINGLE_CHARACTER_OPERATORS: Set[str] = {"+", "-", "*", "/", "%", "^"}
SINGLE_CHARACTER_SYMBOLS: Set[str] = {
    r"\cos",
    r"\sin",
    r"\tan",
    r"\log",
    r"\ln",
    r"\exp",
    r"\lim",
    r"\sum",
    r"\prod",
    r"\int",
    r"\oint",
    r"\iint",
    r"\iiint",
    r"\iiiint",
    r"\oint",
}


def is_whitespace(x: str) -> bool:
    return x in WHITESPACE


def is_letter(x: str) -> bool:
    return re.match(LETTERS, x) is not None


def is_number(x: str) -> bool:
    return re.match(NUMBER, x) is not None


def is_single_character_operator(x: str) -> bool:
    return x in SINGLE_CHARACTER_OPERATORS


def is_opening_parenthesis(x: str) -> bool:
    return x == "("


def is_closing_parenthesis(x: str) -> bool:
    return x == ")"


def is_parenthesis(x: str) -> bool:
    return is_opening_parenthesis(x) or is_closing_parenthesis(x)


def is_opening_brace(x: str) -> bool:
    return x == "{"


def is_closing_brace(x: str) -> bool:
    return x == "}"


def is_brace(x: str) -> bool:
    return is_opening_brace(x) or is_closing_brace(x)


def is_single_character_symbol(x: str) -> bool:
    return x in SINGLE_CHARACTER_SYMBOLS


def is_quote(x: str) -> bool:
    return x == '"' or x == "'"

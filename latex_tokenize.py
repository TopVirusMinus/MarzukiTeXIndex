from typing import List
from identify import (
    is_parenthesis,
    is_whitespace,
    is_number,
    is_letter,
    is_single_character_operator,
    is_single_character_symbol,
)


def latex_tokenize(equation: str) -> List[dict]:
    tokens = []
    cursor = 0

    while cursor < len(equation):
        character = equation[cursor]
        if is_parenthesis(character):
            tokens.append({"type": "parenthesis", "value": character})
            cursor += 1
            continue

        if is_whitespace(character):
            cursor += 1
            continue

        if is_number(character):
            numbers = ""

            while cursor < len(equation) and is_number(equation[cursor]):
                numbers += equation[cursor]
                cursor += 1

            tokens.append({"type": "number", "value": numbers})
            continue

        if is_letter(character):
            letters = ""
            while cursor < len(equation) and is_letter(equation[cursor]):
                letters += equation[cursor]
                cursor += 1

            if is_whitespace(letters):
                continue

            if len(letters) == 0:
                cursor += 1
                continue

            if is_single_character_symbol(letters):
                tokens.append({"type": "single_character_symbol", "value": letters})
                continue

            if len(letters) == 1:
                tokens.append({"type": "letter", "value": letters})
                continue

        if is_single_character_operator(character):
            tokens.append({"type": "single_character_operator", "value": character})
            cursor += 1
            continue

        raise Exception(f"Unexpected character: {character}")
    return tokens


print(latex_tokenize(r"\cos x + \; 5"))

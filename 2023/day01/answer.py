import enum


class NumbersInWords(enum.IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


def parse_simple_line(content: str) -> int:
    digits = [i for i in filter(str.isdigit, content)]
    return int(f"{digits[0]}{digits[-1]}")


def parse_complex_line(content: str) -> int:
    altered_content = content.lower()
    for number in NumbersInWords:
        number_name = number.name.lower()
        altered_content = altered_content.replace(
            number_name,
            f"{number_name[:-1]}{number.value}{number_name[-1]}",
        )  # one -> on1e / two -> tw2o / eight -> eigh8t
    return parse_simple_line(content=altered_content)


def parse_lines(multiline_content: list[str], use_v2: bool) -> int:
    parser = parse_complex_line if use_v2 else parse_simple_line
    return sum(parser(content=line) for line in multiline_content)


if __name__ == "__main__":
    with open("input") as f:
        lines = [line for line in f.readlines()]
        print("--- Part One ---")
        print(f"Answer: {parse_lines(multiline_content=lines, use_v2=False)}")
        print("--- Part Two ---")
        print(f"Answer: {parse_lines(multiline_content=lines, use_v2=True)}")

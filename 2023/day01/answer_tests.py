import unittest

from answer import parse_complex_line, parse_lines, parse_simple_line
from parameterized import parameterized


class AnswerTestCase(unittest.TestCase):
    @parameterized.expand([("1abc2", 12), ("pqr3stu8vwx", 38), ("a1b2c3d4e5f", 15), ("treb7uchet", 77)])
    def test_parse_simple_line(self, input: str, expected: int):
        self.assertEqual(parse_simple_line(input), expected)

    @parameterized.expand(
        [
            # Cases given in the statement
            ("two1nine", 29),
            ("eightwothree", 83),
            ("abcone2threexyz", 13),
            ("xtwone3four", 24),
            ("4nineeightseven2", 42),
            ("zoneight234", 14),
            ("7pqrstsixteen", 76),
            # Specific cases found
            ("coneightq", 18),  # twice-used letter
        ]
    )
    def test_parse_complexe_line(self, input: str, expected: int):
        self.assertEqual(parse_complex_line(input), expected)

    @parameterized.expand(
        [
            (["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"], False, 142),
            (
                [
                    "two1nine",
                    "eightwothree",
                    "abcone2threexyz",
                    "xtwone3four",
                    "4nineeightseven2",
                    "zoneight234",
                    "7pqrstsixteen",
                ],
                True,
                281,
            ),
        ]
    )
    def test_parse_lines(self, lines: list[str], use_v2: bool, expected: int):
        self.assertEqual(parse_lines(multiline_content=lines, use_v2=use_v2), expected)


if __name__ == "__main__":
    unittest.main()

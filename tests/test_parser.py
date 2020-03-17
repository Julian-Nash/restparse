import unittest

from restparse.parser import Parser
from restparse.parser.exceptions import (
    ParserParamRequiredError,
    ParserTypeError,
    ParserInvalidChoiceError
)


class TestParser(unittest.TestCase):

    description = "Test description"

    def test_str_parser(self):

        parser = Parser(description=self.description)
        parser.add_param(
            name="foo",
            type=str,
        )
        params = parser.parse_params({"foo": "bar"})

        self.assertEqual("bar", params.foo)

    def test_int_parser(self):

        parser = Parser(description=self.description)
        parser.add_param(
            name="foo",
            type=int,
        )
        params = parser.parse_params({"foo": 1})

        self.assertEqual(1, params.foo)

    def test_float_parser(self):

        parser = Parser(description=self.description)
        parser.add_param(
            name="foo",
            type=float,
        )
        params = parser.parse_params({"foo": 1.5})

        self.assertEqual(1.5, params.foo)

    def test_list_parser(self):

        parser = Parser(description=self.description)
        parser.add_param(
            name="foo",
            type=list,
        )
        params = parser.parse_params({"foo": [1, 2, 3]})

        self.assertEqual([1, 2, 3], params.foo)

    def test_dict_parser(self):

        parser = Parser(description=self.description)
        parser.add_param(
            name="foo",
            type=dict,
        )
        params = parser.parse_params({"foo": {"foo": 1}})

        self.assertEqual({"foo": 1}, params.foo)

    def test_none_parser(self):

        parser = Parser(description=self.description)
        parser.add_param(
            name="foo",
            type=None,
        )
        params = parser.parse_params({"foo": None})

        self.assertEqual(None, params.foo)

    def test_required(self):

        parser = Parser()

        parser.add_param(
            name="foo",
            type=str,
            required=True
        )

        with self.assertRaises(ParserParamRequiredError):
            params = parser.parse_params({"bar": "baz"})

    def test_choices(self):

        parser = Parser()

        parser.add_param(
            name="foo",
            choices=["bar", "baz"]
        )

        with self.assertRaises(ParserInvalidChoiceError):
            params = parser.parse_params({"foo": 1})

    def test_dest(self):

        parser = Parser()

        parser.add_param(
            name="foo",
            dest="bar"
        )

        params = parser.parse_params({"foo": "baz"})

        self.assertTrue(hasattr(params, "bar"), True)

    def test_incorrect_type(self):

        parser = Parser()

        parser.add_param(
            name="foo",
            type=int
        )

        with self.assertRaises(ParserTypeError):
            params = parser.parse_params({"foo": "bar"})

    def test_default(self):

        parser = Parser()

        parser.add_param(
            name="foo",
            type=str,
            default="bar"
        )
        params = parser.parse_params({})

        self.assertEqual("bar", params.foo)


if __name__ == "__main__":
    unittest.main()

from text2ipa import __version__
from text2ipa import get_IPA, get_IPAs, ConnectionError, InvalidValue
import pytest
import unittest


def test_version():
    assert __version__ == "2.0.2"


# Test the function get_IPA
@pytest.mark.parametrize(
    "text, language, expected",
    [
        ("hello", "am", "həˈloʊ"),
        ("hello", "br", "hɛˈləʊ"),
        ("tomato", "am", "təˈmeɪˌtoʊ"),
        ("tomato", "br", "təˈmɑːtəʊ"),
    ],
)
def test_get_IPA(text, language, expected):
    assert get_IPA(text, language) == expected


# Test the function get IPAs with bulk
@pytest.mark.parametrize(
    "bulk, language, expected",
    [
        (["university", "tomato"], "am", ["ˌjunəˈvɜrsəti", "təˈmeɪˌtoʊ"]),
        (["university", "tomato"], "br", ["ˌjuːnɪˈvɜːsɪti", "təˈmɑːtəʊ"]),
    ],
)
def test_get_IPAs(bulk, language, expected):
    assert get_IPAs(bulk, language) == expected


# Test connection Error
class Test_ConnectionError(unittest.TestCase):
    def test_invalid_language(self):
        with self.assertRaises(InvalidValue):
            get_IPA("hello", "aaa")

    def test_WordError_wanrining(self):
        text = get_IPA("hello", "fr")
        self.assertEqual(text, "????")

    def test_InvalidValue(self):
        with self.assertRaises(InvalidValue):
            get_IPAs(["je"], "aaa")

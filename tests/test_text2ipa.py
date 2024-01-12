from text2ipa import __version__
from text2ipa import get_IPA, get_IPAs, InvalidLanguage
import pytest
import unittest


def test_version():
    assert __version__ == "2.1.2"


# Test the function get_IPA
@pytest.mark.parametrize(
    "text, language, expected",
    [
        ("hello", "en", "hɛˈloʊ"),
        ("tomato", "en", "təˈmɑˌtoʊ"),
        ("je parle","fr","ʒə paʀl")
    ],
)
def test_get_IPA(text, language, expected):
    assert get_IPA(text, language) == expected


# Test the function get IPAs with bulk
@pytest.mark.parametrize(
    "bulk, language, expected",
    [
        (["university", "tomato"], "en", ['ˌjunəˈvərsəti', 'təˈmɑˌtoʊ']),
        (["la patron", "le mere"], "fr", ['la patʀɔ̃', 'lə məʀ']),
    ],
)
def test_get_IPAs(bulk, language, expected):
    assert get_IPAs(bulk, language) == expected


# Test connection Error
class Test_ConnectionError(unittest.TestCase):
    def test_invalid_language(self):
        with self.assertRaises(InvalidLanguage):
            get_IPA("hello", "aaa")


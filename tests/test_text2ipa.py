from text2ipa import __version__
from text2ipa import get_IPA, get_IPAs, ConnectionError, InvalidValue
import pytest
import unittest


def test_version():
    assert __version__ == "2.0.1"


# Test the function get_IPA
@pytest.mark.parametrize(
    "text, language, expected",
    [
        ("hello", "am", "həˈloʊ"),
        ("hello", "br", "hɛˈləʊ"),
        ("tomato", "am", "təˈmeɪˌtoʊ"),
        ("tomato", "br", "təˈmɑːtəʊ"),
        ("je parle un peu français", "fr", "ʒə paʀle œ̃ pø fʀɑ̃̃sɛ"),
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
        (["parle", "français"], "fr", ["paʀle", "fʀɑ̃̃sɛ"]),
    ],
)
def test_get_IPAs(bulk, language, expected):
    assert get_IPAs(bulk, language) == expected


# Test connection Error
class Test_ConnectionError(unittest.TestCase):
    def test_connection_error(self):
        proxy = {
            "http": "socks5://212.129.41.96:54321",
            "https": "socks5://212.129.41.96:54321",
        }
        with self.assertRaises(ConnectionError):
            get_IPA("je", "fr", proxy)
            get_IPA("hello", "am", proxy)

    def test_invalid_language(self):
        with self.assertRaises(InvalidValue):
            get_IPA("hello", "aaa")

    def test_WordError_wanrining(self):
        text = get_IPA("hello", "fr")
        self.assertEqual(text, "[???]")

    def test_InvalidValue(self):
        with self.assertRaises(InvalidValue):
            get_IPAs(["je"], "aaa")

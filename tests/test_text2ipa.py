from text2ipa import __version__
from text2ipa import get_IPA, get_IPAs
import pytest


def test_version():
    assert __version__ == "1.4.1"


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


@pytest.mark.parametrize(
    "bulk, language, expected",
    [
        (["university", "tomato"], "am", ["ˌjunəˈvɜrsəti", "təˈmeɪˌtoʊ"]),
        (["university", "tomato"], "br", ["ˌjuːnɪˈvɜːsɪti", "təˈmɑːtəʊ"]),
    ],
)
def test_get_IPAs(bulk, language, expected):
    assert get_IPAs(bulk, language) == expected

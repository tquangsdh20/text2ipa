import epitran
import eng_to_ipa
from typing import List


class InvalidLanguage(Exception):
    """Invalid Language"""

    ...


ERROR_MSG = 'The Language input is invalid. Must be "en" or "fr".'


def text_to_ipa_french(text):
    # Create an Epitran object for French
    french_epitran = epitran.Epitran("fra-Latn")

    # Convert French text to IPA
    ipa_result = french_epitran.transliterate(text)

    return ipa_result


def text_to_ipa_english_us(text):
    # Create an Epitran object for English (USA)
    ipa_result = eng_to_ipa.convert(text)
    return ipa_result


def get_IPA(text: str, language: str) -> str:
    retStr: str = ""
    if language == "fr":
        retStr = text_to_ipa_french(text)
    elif language == "en":
        retStr = text_to_ipa_english_us(text)
    else:
        raise InvalidLanguage(ERROR_MSG)
    return retStr


def get_IPAs(bulk: List[str], language: str) -> List[str]:
    return [get_IPA(word, language) for word in bulk]

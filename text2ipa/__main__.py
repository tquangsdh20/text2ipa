import requests
from bs4 import BeautifulSoup
from typing import List, Any
import logging
import re


class ManyRequest(Exception):
    """Send many requests to get IPA"""

    ...


class InvalidValue(Exception):
    """Invalid Language"""

    ...


class WordError(Exception):
    """Not found the word in French dictionary"""

    ...


class ConnectionError(Exception):
    """Not found the word in French dictionary"""

    ...


VALID_LANGUAGE = ["am", "br", "fr"]
PAGE = "https://tophonetics.com/"
DICTIONARY = "https://dictionary.cambridge.org/dictionary/french-english"
ERROR_MSG = 'The Language input is invalid. Must be "am", "br" or "fr".'


def get_french_word(word: str, proxy: Any = None):
    url: str
    url = f"{DICTIONARY}/{word}"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url=url, headers=headers, timeout=1.5, proxies=proxy)
    except (requests.HTTPError, requests.ConnectTimeout, requests.ConnectionError) as e:
        raise ConnectionError(f"{e}")
    soup = BeautifulSoup(r.text, "html.parser")
    # with open("dummy.txt",'r',encoding='utf-8') as fp:
    #     soup = BeautifulSoup(fp.read(),'html.parser')
    # <span class="ipa dipa">
    tag = soup.find("span", {"class": "ipa dipa"})
    if tag is None:
        raise WordError(f'Not found the word "{word}" in the dictionary.')
    return tag.text


def __get_french_ipa(text: str, proxy: Any = None):
    words = re.findall("\\w+", text)
    retStr: str = ""
    for idx in range(len(words)):
        try:
            retStr += get_french_word(words[idx], proxy) + " "
        except (WordError, ConnectionError) as e:
            logging.warning(
                f'Failed to convert the word "{words[idx]}" with message: {e}'
            )
            retStr += "????" + " "
    return retStr.strip()


def get_data(text: str, language: str, output_style: str):
    retdata = {
        "text_to_transcribe": text,
        "submit": "Show transcription",
        "output_dialect": language,
        "output_style": output_style,
        "preBracket": "",
        "postBracket": "",
        "speech_support": "1",
    }
    return retdata


def __get_IPA_en(text: str, language: str, proxy: Any = None) -> str:
    data = get_data(text, language, "only_tr")
    try:
        response = requests.post(PAGE, data=data, proxies=proxy, timeout=10)
    except (requests.ConnectTimeout, requests.HTTPError, requests.ConnectionError) as e:
        raise ConnectionError(f"{e}")
    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup("div")
    retStr: str = ""  # Provide an initial value here
    for tag in tags:
        item = tag.get("id")
        if item == "transcr_output":
            if tag.text == "":
                raise ManyRequest("Too many requests")
            else:
                retStr = str(tag.text)
    return retStr



def get_IPA(text: str, language: str, proxy: Any = None) -> str:
    retStr: str
    if language == "fr":
        retStr = __get_french_ipa(text, proxy)
    elif language in ["br", "am"]:
        retStr = __get_IPA_en(text, language, proxy)
    else:
        raise InvalidValue(ERROR_MSG)
    return retStr


def __get_IPAs_en(bulk: List[str], language: str, proxy: Any = None) -> List[str]:
    # Convert bulk to string
    texts: str = ""
    for text in bulk:
        texts += text + ";"
    _res = __get_IPA_en(texts, language, proxy)
    # Convert string to bulk
    retList = _res.split(";")
    return retList[0:-1]


def __get_french_ipas(bulk: List[str], proxy: Any = None) -> List[str]:
    # Convert bulk to string
    texts: str = ""
    for idx in range(len(bulk)):
        text = __get_french_ipa(bulk[idx], proxy)
        texts += text + ";"

    # Convert string to bulk
    retList = texts.split(";")
    return retList[0:-1]


def get_IPAs(bulk: List[str], language: str, proxy: Any = None) -> List[str]:
    retList: List[str]
    if language == "fr":
        retList = __get_french_ipas(bulk, proxy)
    elif language in ["br", "am"]:
        retList = __get_IPAs_en(bulk, language, proxy)
    else:
        raise InvalidValue(ERROR_MSG)
    return retList

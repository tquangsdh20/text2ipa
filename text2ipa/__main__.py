import requests
from bs4 import BeautifulSoup
from typing import List, Any


class ManyRequest(Exception):
    ...


class InvalidValue(Exception):
    ...


VALID_LANGUAGE = ["am", "br"]
PAGE = "https://tophonetics.com/"
ERROR_MSG = 'The Language input is invalid. Must be "am" or "br".'


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


def get_IPA(text: str, language: str, proxy: Any = None) -> str:
    if language not in VALID_LANGUAGE:

        raise InvalidValue(ERROR_MSG)
    data = get_data(text, language, "only_tr")
    response = requests.post(PAGE, data=data, proxies=proxy, timeout=3)
    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup("div")
    for tag in tags:
        item = tag.get("id")
        if item == "transcr_output":
            if tag.text == "":
                raise ManyRequest("Too many request")
            else:
                retStr = tag.text
    return str(retStr)


def get_IPAs(bulk: List[str], language: str, proxy: Any = None) -> List[str]:
    # Convert bulk to string
    texts = ""
    for text in bulk:
        texts += text + ";"
    # Check for LANGUAGE valid or not
    if language not in VALID_LANGUAGE:
        raise InvalidValue(ERROR_MSG)
    data = get_data(texts, language, "only_tr")
    # Send request convert all string
    response = requests.post(PAGE, data=data, proxies=proxy, timeout=3)
    soup = BeautifulSoup(response.text, "html.parser")
    tags = soup("div")
    for tag in tags:
        item = tag.get("id")
        if item == "transcr_output":
            if tag.text == "":
                raise ManyRequest("Too many request")
            else:
                _res = tag.text
    # Convert string to bulk
    retList = _res.split(";")
    return list(retList[0:-1])


def __handle_error_IPA(text: str, language: str, proxy: Any = None):
    try:
        res = get_IPA(text, language, proxy)
    except (
        InvalidValue,
        requests.exceptions.ConnectTimeout,
        requests.exceptions.ReadTimeout,
        requests.exceptions.ConnectionError,
        ManyRequest,
    ) as e:
        print(e)
    else:
        print(res)


def __handle_error_IPAs(bulk: List[str], language: str, proxy: Any = None):
    try:
        res = get_IPAs(bulk, language, proxy)
    except (
        InvalidValue,
        requests.exceptions.ConnectTimeout,
        requests.exceptions.ReadTimeout,
        requests.exceptions.ConnectionError,
        ManyRequest,
    ) as e:
        print(e)
    else:
        print(res)


if __name__ == "__main__":
    text = "hello"
    bulk = ["university", "tomato"]
    languages = ["am", "br", "in"]
    proxy = {
        "http": "socks5://212.129.41.96:54321",
        "https": "socks5://212.129.41.96:54321",
    }
    for language in languages:
        __handle_error_IPA(text, language, proxy)
        __handle_error_IPAs(bulk, language, proxy)

    for index in range(50):
        __handle_error_IPA(text, "am", proxy)
        __handle_error_IPAs(bulk, "am", proxy)

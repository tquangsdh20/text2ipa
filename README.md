<p align="center">
<img src="https://raw.githubusercontent.com/tquangsdh20/text2ipa/main/.github/logo.svg">
<img src="https://github.com/tquangsdh20/text2ipa/actions/workflows/github-build.yml/badge.svg?style=plastic"> <a href="https://app.codecov.io/gh/tquangsdh20/text2ipa/blob/17f174a83a0a416100fadc9e209c1c8a88d74352/tests/test_text2ipa.py"><img src="https://codecov.io/gh/tquangsdh20/text2ipa/branch/main/graphs/badge.svg?branch=master"></a> <img src="https://img.shields.io/github/license/tquangsdh20/text2ipa"> <img src="https://img.shields.io/github/issues-raw/tquangsdh20/text2ipa"> <img src="https://img.shields.io/pypi/implementation/text2ipa"> <img src="https://img.shields.io/badge/author-tquangsdh20-orange">
</p>



## Installation:

**Windows**
```
python -m pip install text2ipa
```
**macOS**
```
sudo pip3 install text2ipa
```
**Linux**
```
pip install text2ipa
```

## Features

- Convert Engkish text to IPA
- Two options Language English UK and English US
  
## Examples

### Example 1: Convert a text

#### Function: 
- `get_IPA()` : Converting a text to IPA with the following parameters 

#### Parameters:

- `text` : The text you want to convert to IPA
- `language` : Choose between English US and English UK ('am'/'br')
- `proxy` : Optional parameter  

#### For instance:

```python
from text2ipa import get_IPA
text = 'hello world'
language = 'am'
#Convert 'hello world' to English US International Alphabet
ipa = get_IPA(text,language)
print(ipa)
```
```
>> həˈloʊ wɜrld
```
### Example 2: Convert a bulk

#### Function: 
- `get_IPAs()` : Convert the list of texts to IPA return the list of IPAs 

#### Parameters:

- `bulk` : The list of text want to convert to IPA
- `language` : Choose between English US and English UK ('am'/'br')
- `proxy` : Optional parameter  

#### For instance:

```python
from text2ipa import get_IPAs
bulk = ['how are you?','how it\'s going?','that\'s good']
language = 'br'
# Convert a list of text to English UK IPA
IPAs = get_IPAs(bulk,language)
for ipa in IPAs:
    print(ipa)
```

```
>> haʊ ɑː juː?
>> haʊ ɪts ˈgəʊɪŋ?
>> ðæts gʊd
```

#### Log Changes

V1.0.0 : Create new with 2 functions `get_IPA()` and `get_IPAs()`  
V1.2.0 : Update comment and guideline in functions, fixed ERROR for setup with the other Python versions  
V1.3.0 : Fixed MISSING install requires and update information for Python versions  
V1.4.0 : Update building & testing for this package  

<a href="https://github.com/tquangsdh20/text2ipa"><p align="center"><img src="https://img.shields.io/badge/Github-tquangsdh20-orange?style=social&logo=github"></p></a>

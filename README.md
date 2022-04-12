<p align="center">
<img src="https://raw.githubusercontent.com/tquangsdh20/text2ipa/master/.github/logo.gif">
<img src="https://github.com/tquangsdh20/text2ipa/actions/workflows/test.yml/badge.svg?style=plastic"> <a href="https://app.codecov.io/gh/tquangsdh20/text2ipa/blob/af74004d58fb4cde15ea29b1184fc7a025ca9fc2/text2ipa/__main__.py"><img src="https://codecov.io/gh/tquangsdh20/text2ipa/branch/master/graphs/badge.svg?branch=master"></a> <img src="https://img.shields.io/pypi/implementation/text2ipa"> <img src = "https://img.shields.io/pypi/pyversions/text2ipa"> <img src="https://img.shields.io/badge/author-tquangsdh20-orange">
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

- Convert English text to IPA using the [toPhonetic](https://tophonetics.com/)
- Three options Language English UK, English US and French
  
## Examples

### Example 1: Convert a text

#### Function: 
- `get_IPA()` : Converting a text to IPA with the following parameters 

#### Parameters:

- `text` : The text you want to convert to IPA
- `language` : Choose between English US, English UK and French ('am', 'br' or 'fr')
- `proxy` : Optional parameter  

#### For instance:

```python
from text2ipa import get_IPA
# Convert 'hello world' to English US International Alphabet
text = 'hello world'
language = 'am'
ipa = get_IPA(text, language)
# Convert 'je parle un peu français' to IPA
text = 'je parle un peu français'
language = 'fr'
fr_ipa = get_IPA(text, language)
print(ipa)
print(fr_ipa)
```
```
>> həˈloʊ wɜrld
>> ʒə paʀle œ̃ pø fʀɑ̃̃sɛ
```

### Example 2: Convert a bulk

#### Function: 
- `get_IPAs()` : Convert the list of texts to IPA return the list of IPAs 

#### Parameters:

- `bulk` : The list of text want to convert to IPA
- `language` : Choose between English US and English UK ('am', 'br' or 'fr')
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
V1.4.1 : Fixed Error Import `get_IPA()` and `get_IPAs`  
V2.0.1 : New feature working with French  
V2.0.2 : Update dependencies

<a href="https://github.com/tquangsdh20/text2ipa"><p align="center"><img src="https://img.shields.io/badge/Github-tquangsdh20-orange?style=social&logo=github"></p></a>

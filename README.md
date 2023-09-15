# Domovyk
A package to transliterate various Cyrillic alphabets to and from the Latin alphabet using the American Library Association-Library of Congress Romanization tables.
<p align="center">
<img src="https://raw.githubusercontent.com/ian-nai/domovyk/main/domovyk_statue.jpg" alt="domovyk statue" width="300" height="393">
</p>
Domovyk is named after household spirits from Slavic mythology.


## Installation
Install using pip:
```
pip3 install domovyk
```
Or download the GitHub repo and the install the only dependency (for sentence tokenization):
```
pip3 install nltk
```

## Usage
The package uses the ALA-LC Romanization tables to transliterate each of the following languages:
* Belarusian
* Bulgarian
* Carpatho-Rusyn
* Macedonian
* Russian
* Serbian
* Ukrainian

Four functions can be called for each language:

* transliterate(var, lang) - Transliterates a Cyrillic string or list of strings (var) from a specified language (lang) into the Latin alphabet. Returns a string.
* translatinate(var, lang) - Transliterates a string or list of strings in the Latin alphabet (var) to a specified Cyrillic script (lang). Returns a string.
* transliterateSents(var, lang) - Tokenizes a given Cyrillic (var) into a list of sentences, then transliterates those sentences from a specified language (lang) into the Latin alphabet. Returns a list.
* translatinateSents(var, lang) - Tokenizes a given string in the Latin alphabet (var) into a list of sentences, then transliterates those sentences  to a specified Cyrillic script (lang). Returns a list.

Some usage examples are below:
```
from domovyk import translit

belarusian_to_latin = translit.transliterate('Як справы?', 'bel')
latin_to_macedonian = translit.translatinate('Hi, how are you?', 'mac')
ukrainian_to_latin_sents = translit.transliterateSents('Єхидна, ґава, їжак ще й шиплячі плазуни бігцем форсують Янцзи.', 'ukr')
latin_to_russian_sents = translit.translatinateSents('Hello, how are you doing?', 'rus')
```
The languages can be called in the code using the following abbreviations:
* Belarusian - 'bel'
* Bulgarian - 'bulg'
* Carpatho-Rusyn - 'carp'
* Macedonian - 'mac'
* Russian 'rus'
* Serbian - 'serb'
* Ukrainian - 'ukr'

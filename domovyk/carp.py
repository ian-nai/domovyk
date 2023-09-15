carp_dict = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "H",
    "Ґ": "G",
    "Д": "D",
    "Е": "E",
    "Є": "I͡E",
    "Ё": "Ë",
    "Ж": "Z͡H",
    "З": "Z",
    "І": "I",
    "Ї": "Ї",
    "И": "Y",
    "Ы": "Ŷ",
    "Й": "Ĭ",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "Ô": "Ô",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "K͡H",
    "Ц": "T͡S",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Shch",
    "Э": "Ė",
    "Ю": "I͡U",
    "Я": "I͡A",
    "Ь": "'",
    "Ъ": '"',
    "Ѣ": "Î",
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "h",
    "ґ": "g",
    "д": "d",
    "е": "e",
    "є": "i͡e",
    "ё": "ё",
    "ж": "z͡h",
    "з": "z",
    "i": "i",
    "ї": "ї",
    "и": "y",
    "ы": "ŷ",
    "й": "ĭ",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "ô": "ô",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "k͡h",
    "ц": "t͡s",
    "ч": "ch",
    "ш": "sh",
    "щ": "shch",
    "э": "ė",
    "ю": "i͡u",
    "я": "i͡a",
    "ь": "ʹ",
    "ъ": 'ʺ',
    "ѣ": "î"
}

carp_to_lat_dict = {y: x for x, y in iter(carp_dict.items())}

# Function to iterate through characters - if character in dict, swap for
# corresponding key


def translate_from_dict(original_text, dictionary_of_translations):
    out = original_text
    for target in dictionary_of_translations:
        trans = str.maketrans(target, dictionary_of_translations[target])
        out = out.translate(trans)
    return out

# Output a list of sentences from a string


def string_to_list(input_string):
    import nltk.tokenize
    from nltk.tokenize import sent_tokenize, word_tokenize
    output = sent_tokenize(input_string)
    return output

# Tokenize string into sentences and transliterate from Carpatho-Rusyn to
# the Latin alphabet using the dictionary above


def carp_translit_sents(input_string):
    import re

    def carp_translate(x): return ''.join([carp_dict[i] for i in x])

    text = string_to_list(input_string)

    translated_full = []
    for txt in text:
        list_of_translated = []
        words = re.split(r'(\s+)', txt)
        for word in words:
            word_list = []
            for letter in word:
                if letter in carp_dict:
                    translated = carp_translate(letter)
                    word_list.append(translated)
                else:
                    word_list.append(letter)
            list_of_translated.append(''.join(word_list))
        translated_full.append(''.join(list_of_translated))

    transliterated_sents = translated_full
    return transliterated_sents

# Transliterate from Carpatho-Rusyn to the Latin alphabet using the
# dictionary above


def carp_translit(input):
    import re

    def carp_translate(x): return ''.join([carp_dict[i] for i in x])

    if isinstance(input, str):
        text = input
        translated_full = []
        list_of_translated = []
        words = re.split(r'(\s+)', text)
        for word in words:
            word_list = []
            for letter in word:
                if letter in carp_dict:
                    translated = carp_translate(letter)
                    word_list.append(translated)
                else:
                    word_list.append(letter)
            list_of_translated.append(''.join(word_list))
        translated_full.append(''.join(list_of_translated))

        transliterated_sents = ' '.join(translated_full)
        return transliterated_sents

    elif isinstance(input, list):
        text = []
        for el in input:
            text.append(el)
        translated_full = []
        for txt in text:
            list_of_translated = []
            words = re.split(r'(\s+)', txt)
            for word in words:
                word_list = []
                for letter in word:
                    if letter in carp_dict:
                        translated = carp_translate(letter)
                        word_list.append(translated)
                    else:
                        word_list.append(letter)
                list_of_translated.append(''.join(word_list))
            translated_full.append(''.join(list_of_translated))

        transliterated_sents = ' '.join(translated_full)
        return transliterated_sents

# Tokenize a string into sentences and transliterate from the Latin
# alphabet to Carpatho-Rusyn


def latin_to_carp_sents(input_string):
    import re

    def carp_translatinate(x): return ''.join([carp_to_lat_dict[i] for i in x])
    text = string_to_list(input_string)
    translatinated_full = []
    for txt in text:
        list_of_translatinated = []
        words = re.split(r'(\s+)', txt)
        for w in words:
            word_list = []

            for i, j, in enumerate(w):
                # making sure letters we're checking for are within the list's
                # range
                if j == u"\u0361":
                    if 0 <= i + 1 < len(w):
                        if w[i - 1] == "t" and w[i + 1] == "s":
                            word_list.append("ц")
                        elif w[i - 1] == "T" and w[i + 1] == "S":
                            word_list.append("Ц")

                        elif w[i - 1] == "i" and w[i + 1] == "e":
                            word_list.append("є")
                        elif w[i - 1] == "I" and w[i + 1] == "E":
                            word_list.append("Є")

                        elif w[i - 1] == "i" and w[i + 1] == "u":
                            word_list.append("ю")
                        elif w[i - 1] == "I" and w[i + 1] == "U":
                            word_list.append("Ю")

                        elif w[i - 1] == "i" and w[i + 1] == "a":
                            word_list.append("я")
                        elif w[i - 1] == "I" and w[i + 1] == "A":
                            word_list.append("Я")

                        elif w[i - 1] == "z" and w[i + 1] == "h":
                            word_list.append("ж")
                        elif w[i - 1] == "Z" and w[i + 1] == "H":
                            word_list.append("Ж")

                        elif w[i - 1] == "k" and w[i + 1] == "h":
                            word_list.append("х")
                        elif w[i - 1] == "K" and w[i + 1] == "H":
                            word_list.append("Х")

                elif j == "c":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            if w[i - 2] != "s" and w[i - 2] != "S":
                                word_list.append("ч")
                elif j == "C":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("Ч")

                elif j == "s":
                    if 0 <= i + 3 < len(w):
                        if w[i + 1] == "h":
                            if w[i + 2] == "c":
                                if w[i + 3] == "h":
                                    word_list.append("щ")
                            else:
                                if w[i + 1] == "h":
                                    word_list.append("ш")
                                else:
                                    word_list.append("c")
                        else:
                            word_list.append("c")

                    else:
                        word_list.append("c")

                elif j == "S":
                    if w[i + 1] == "h":
                        if w[i + 2] == "c":
                            if w[i + 3] == "h":
                                word_list.append("Щ")
                    else:
                        if w[i + 1] == "h":
                            word_list.append("Ш")
                        else:
                            word_list.append("С")

                elif j == 'h':
                    if i != 0:
                        if [i - 1] == 'c':
                            if [i - 2] == "h":
                                if [i - 3] == "s":
                                    continue
                        else:
                            word_list.append("г")
                    else:
                        word_list.append("г")

                elif j in carp_to_lat_dict:
                    translatinated = carp_translatinate(j)
                    word_list.append(translatinated)
                else:
                    word_list.append(j)

            list_of_translatinated.append(''.join(word_list))
        translatinated_full.append(''.join(list_of_translatinated))

    transliterated_sents = translatinated_full
    return transliterated_sents

# Transliterate from Carpatho-Rusyn to the Latin alphabet


def latin_to_carp(input):
    import re

    def carp_translatinate(x): return ''.join([carp_to_lat_dict[i] for i in x])

    if isinstance(input, str):
        text = input
        translatinated_full = []
        list_of_translatinated = []
        words = re.split(r'(\s+)', text)
        for w in words:
            word_list = []

            for i, j, in enumerate(w):
                # making sure letters we're checking for are within the list's
                # range
                if j == u"\u0361":
                    if 0 <= i + 1 < len(w):
                        if w[i - 1] == "t" and w[i + 1] == "s":
                            word_list.append("ц")
                        elif w[i - 1] == "T" and w[i + 1] == "S":
                            word_list.append("Ц")

                        elif w[i - 1] == "i" and w[i + 1] == "e":
                            word_list.append("є")
                        elif w[i - 1] == "I" and w[i + 1] == "E":
                            word_list.append("Є")

                        elif w[i - 1] == "i" and w[i + 1] == "u":
                            word_list.append("ю")
                        elif w[i - 1] == "I" and w[i + 1] == "U":
                            word_list.append("Ю")

                        elif w[i - 1] == "i" and w[i + 1] == "a":
                            word_list.append("я")
                        elif w[i - 1] == "I" and w[i + 1] == "A":
                            word_list.append("Я")

                        elif w[i - 1] == "z" and w[i + 1] == "h":
                            word_list.append("ж")
                        elif w[i - 1] == "Z" and w[i + 1] == "H":
                            word_list.append("Ж")

                        elif w[i - 1] == "k" and w[i + 1] == "h":
                            word_list.append("х")
                        elif w[i - 1] == "K" and w[i + 1] == "H":
                            word_list.append("Х")

                elif j == "c":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            if w[i - 2] != "s" and w[i - 2] != "S":
                                word_list.append("ч")
                elif j == "C":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("Ч")

                elif j == "s":
                    if 0 <= i + 3 < len(w):
                        if w[i + 1] == "h":
                            if w[i + 2] == "c":
                                if w[i + 3] == "h":
                                    word_list.append("щ")
                            else:
                                if w[i + 1] == "h":
                                    word_list.append("ш")
                                else:
                                    word_list.append("c")
                        else:
                            word_list.append("c")

                    else:
                        word_list.append("c")

                elif j == "S":
                    if w[i + 1] == "h":
                        if w[i + 2] == "c":
                            if w[i + 3] == "h":
                                word_list.append("Щ")
                    else:
                        if w[i + 1] == "h":
                            word_list.append("Ш")
                        else:
                            word_list.append("С")

                elif j == 'h':
                    if i != 0:
                        if [i - 1] == 'c':
                            if [i - 2] == "h":
                                if [i - 3] == "s":
                                    continue
                        else:
                            word_list.append("г")
                    else:
                        word_list.append("г")

                elif j in carp_to_lat_dict:
                    translatinated = carp_translatinate(j)
                    word_list.append(translatinated)
                else:
                    word_list.append(j)

            list_of_translatinated.append(''.join(word_list))
        translatinated_full.append(''.join(list_of_translatinated))

        transliterated_sents = ' '.join(translatinated_full)
        return transliterated_sents

    elif isinstance(input, list):
        translatinated_full = []
        list_of_translatinated = []
        for txt in input:
            list_of_translatinated = []
            words = re.split(r'(\s+)', txt)
            for w in words:
                word_list = []
                for i, j, in enumerate(w):
                    # making sure letters we're checking for are within the
                    # list's range
                    if j == u"\u0361":
                        if 0 <= i + 1 < len(w):
                            if w[i - 1] == "t" and w[i + 1] == "s":
                                word_list.append("ц")
                            elif w[i - 1] == "T" and w[i + 1] == "S":
                                word_list.append("Ц")

                            elif w[i - 1] == "i" and w[i + 1] == "e":
                                word_list.append("є")
                            elif w[i - 1] == "I" and w[i + 1] == "E":
                                word_list.append("Є")

                            elif w[i - 1] == "i" and w[i + 1] == "u":
                                word_list.append("ю")
                            elif w[i - 1] == "I" and w[i + 1] == "U":
                                word_list.append("Ю")

                            elif w[i - 1] == "i" and w[i + 1] == "a":
                                word_list.append("я")
                            elif w[i - 1] == "I" and w[i + 1] == "A":
                                word_list.append("Я")

                            elif w[i - 1] == "z" and w[i + 1] == "h":
                                word_list.append("ж")
                            elif w[i - 1] == "Z" and w[i + 1] == "H":
                                word_list.append("Ж")

                            elif w[i - 1] == "k" and w[i + 1] == "h":
                                word_list.append("х")
                            elif w[i - 1] == "K" and w[i + 1] == "H":
                                word_list.append("Х")

                    elif j == "c":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "h":
                                if w[i - 2] != "s" and w[i - 2] != "S":
                                    word_list.append("ч")
                    elif j == "C":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "h":
                                word_list.append("Ч")

                    elif 0 <= i + 3 < len(w):
                        # if 0 <= i+1 < len(w):
                        if j == "s":
                            if w[i + 1] == "h":
                                if w[i + 2] == "c":
                                    if w[i + 3] == "h":
                                        word_list.append("щ")
                                else:
                                    if w[i + 1] == "h":
                                        word_list.append("ш")
                        if j == "S":
                            if w[i + 1] == "h":
                                if w[i + 2] == "c":
                                    if w[i + 3] == "h":
                                        word_list.append("Щ")
                            else:
                                if w[i + 1] == "h":
                                    word_list.append("Ш")
                    elif j == 'h':
                        if i != 0:
                            if [i - 1] == 'c':
                                word_list.append("ч")

                            elif [i - 1] == 'C':
                                word_list.append("Ч")
                        else:
                            translatinated = carp_translatinate(j)
                            word_list.append(translatinated)

                    elif j in carp_to_lat_dict:
                        translatinated = carp_translatinate(j)
                        word_list.append(translatinated)
                    else:
                        word_list.append(j)

                list_of_translatinated.append(''.join(word_list))
            translatinated_full.append(''.join(list_of_translatinated))

    transliterated_sents = ' '.join(translatinated_full)
    return transliterated_sents

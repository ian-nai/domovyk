bulgarian_dict = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ж": "Zh",
    "З": "Z",
    "И": "I",
    "Й": "Ĭ",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "Kh",
    "Ц": "T͡S",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Sht",
    "Ъ": "Ŭ",
    "Ь": "'",
    "Ѣ": "I͡E",
    "Ю": "I͡U",
    "Я": "I͡A",
    "Ѫ": "U̐",
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "е": "e",
    "ж": "zh",
    "з": "z",
    "и": "i",
    "й": "ĭ",
    "к": "k",
    "л": "l",
    "м": "m",
    "н": "n",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "kh",
    "ц": "t͡s",
    "ч": "ch",
    "ш": "sh",
    "щ": "sht",
    "ъ": "ŭ",
    "ь": "ʹ",
    "ѣ": "i͡e",
    "э": "ė",
    "ю": "i͡u",
    "я": "i͡a",
    "ѫ": "u̐"
}


bulgarian_to_lat_dict = {y: x for x, y in iter(bulgarian_dict.items())}

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
    from nltk.tokenize import sent_tokenize
    output = sent_tokenize(input_string)
    return output

# Tokenize string into sentences and transliterate from Bulgarian to the
# Latin alphabet using the dictionary above


def bulg_translit_sents(input_string):
    import re

    def bulg_translate(x): return ''.join([bulgarian_dict[i] for i in x])

    text = string_to_list(input_string)

    translated_full = []
    for txt in text:
        list_of_translated = []
        words = re.split(r'(\s+)', txt)
        for word in words:
            word_list = []
            for letter in word:
                if letter in bulgarian_dict:
                    translated = bulg_translate(letter)
                    word_list.append(translated)
                else:
                    word_list.append(letter)
            list_of_translated.append(''.join(word_list))
        translated_full.append(''.join(list_of_translated))

    transliterated_sents = translated_full
    return transliterated_sents

# Transliterate from Bulgarian to the Latin alphabet using the dictionary above


def bulg_translit(input):
    import re

    def bulg_translate(x): return ''.join([bulgarian_dict[i] for i in x])

    if isinstance(input, str):
        text = input
        translated_full = []
        list_of_translated = []
        words = re.split(r'(\s+)', text)
        for word in words:
            word_list = []
            for letter in word:
                if letter in bulgarian_dict:
                    translated = bulg_translate(letter)
                    word_list.append(translated)
                else:
                    word_list.append(letter)
            list_of_translated.append(''.join(word_list))
        translated_full.append(''.join(list_of_translated))

        for x in translated_full:
            word_list = re.split(r'(\s+)', x)

        new_word_list = []
        new_translated_full = []

        for word in word_list:
            if word[-1] == 'Ŭ':
                temp_list = list(word)
                temp_list[-1] = '"'
                new_string = ''.join(temp_list)
                word = new_string
                new_word_list.append(word)
            elif word[-1] == 'ŭ':
                temp_list = list(word)
                temp_list[-1] = '"'
                new_string = ''.join(temp_list)
                word = new_string
                new_word_list.append(word)
            else:
                new_word_list.append(word)

        new_translated_full.append(''.join(new_word_list))

        transliterated_sents = ' '.join(new_translated_full)
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
                    if letter in bulgarian_dict:
                        translated = bulg_translate(letter)
                        word_list.append(translated)
                    else:
                        word_list.append(letter)
                list_of_translated.append(''.join(word_list))
            translated_full.append(''.join(list_of_translated))

        word_list = []
        for x in translated_full:
            word_list.append(re.split(r'(\s+)', x))

        list_of_translated2 = []
        new_translated_full = []

        for word in word_list:
            list_of_translated2.append(word)

        for w in list_of_translated2:
            new_word_list = []
            for p in w:
                punctuation = ['.', ',', ':', '-', "'"]
                if p[-1] not in punctuation:
                    if p[-1] == 'Ŭ':
                        temp_list = list(p)
                        temp_list[-1] = '"'
                        new_string = ''.join(temp_list)
                        word = new_string
                        new_word_list.append(p)
                    elif p[-1] == 'ŭ':
                        temp_list = list(p)
                        temp_list[-1] = '"'
                        new_string = ''.join(temp_list)
                        word = new_string
                        new_word_list.append(p)
                    else:
                        new_word_list.append(p)
                elif p[-1] in punctuation:
                    if p[-2] == 'Ŭ':
                        temp_list = list(p)
                        temp_list[-2] = '"'
                        new_string = ''.join(temp_list)
                        word = new_string
                        new_word_list.append(p)
                    elif p[-2] == 'ŭ':
                        temp_list = list(p)
                        temp_list[-2] = '"'
                        new_string = ''.join(temp_list)
                        p = new_string
                        new_word_list.append(p)
                    else:
                        new_word_list.append(p)
                else:
                    new_word_list.append(p)

            new_translated_full.append(new_word_list)

        final_list = []
        for s in new_translated_full:
            joined = (''.join(s))
            final_list.append(joined)

    transliterated_sents = ' '.join(final_list)
    return transliterated_sents


# Tokenize a string into sentences and transliterate from the Latin
# alphabet to Bulgarian
def latin_to_bulg_sents(input_string):
    import re

    def bulg_translatinate(x): return ''.join(
        [bulgarian_to_lat_dict[i] for i in x])
    text = string_to_list(input_string)
    translatinated_full = []
    for txt in text:
        list_of_translatinated = []
        words = re.split(r'(\s+)', txt)
        for w in words:
            word_list = []

            for i, j, in enumerate(w):
                if j == u"\u0361":
                    if 0 <= i + 1 < len(w):
                        if w[i - 1] == "t" and w[i + 1] == "s":
                            word_list.append("ц")
                        elif w[i - 1] == "T" and w[i + 1] == "S":
                            word_list.append("Ц")

                        elif w[i - 1] == "i" and w[i + 1] == "e":
                            word_list.append("ѣ")
                        elif w[i - 1] == "I" and w[i + 1] == "E":
                            word_list.append("Ѣ")

                        elif w[i - 1] == "i" and w[i + 1] == "a":
                            word_list.append("я")
                        elif w[i - 1] == "I" and w[i + 1] == "A":
                            word_list.append("Я")

                        elif w[i - 1] == "i" and w[i + 1] == "u":
                            word_list.append("ю")
                        elif w[i - 1] == "I" and w[i + 1] == "U":
                            word_list.append("Ю")

                elif j == "k":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("х")

                elif j == "K":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("Х")

                elif j == "c":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("ч")

                elif j == "C":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("Ч")

                elif j == "s":
                    if 0 <= i + 2 < len(w):
                        if w[i + 1] == "h":
                            if w[i + 2] == "t":
                                word_list.append("щ")
                            else:
                                word_list.append("ш")
                        else:
                            word_list.append("c")
                    else:
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "h":
                                word_list.append("ш")
                            else:
                                word_list.append("c")

                        else:
                            word_list.append("c")

                elif j == "S":
                    if 0 <= i + 2 < len(w):
                        if w[i + 1] == "h":
                            if w[i + 2] == "t":
                                word_list.append("Щ")
                            else:
                                word_list.append("Ш")
                        else:
                            word_list.append("С")
                    else:
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "h":
                                word_list.append("Ш")
                            else:
                                word_list.append("С")

                        else:
                            word_list.append("С")

                elif j == 'Z':
                    if 0 <= i + 1 < len(w):
                        if [i + 1] == 'h':
                            word_list.append("Ж")
                        else:
                            word_list.append("З")
                    else:
                        word_list.append("З")

                elif j == 'z':
                    if 0 <= i + 1 < len(w):
                        if [i + 1] == 'h':
                            word_list.append("ж")
                        else:
                            word_list.append("з")
                    else:
                        word_list.append("з")

                elif j in bulgarian_to_lat_dict:
                    translatinated = bulg_translatinate(j)
                    word_list.append(translatinated)
                else:
                    word_list.append(j)

            list_of_translatinated.append(''.join(word_list))
        translatinated_full.append(''.join(list_of_translatinated))

    transliterated_sents = translatinated_full
    return transliterated_sents

# Transliterate from Bulgarian to the Latin alphabet


def latin_to_bulg(input):
    import re

    def bulg_translatinate(x): return ''.join(
        [bulgarian_to_lat_dict[i] for i in x])

    if isinstance(input, str):
        text = input
        translatinated_full = []
        list_of_translatinated = []
        words = re.split(r'(\s+)', text)
        for w in words:
            word_list = []
            for i, j, in enumerate(w):
                if j == u"\u0361":
                    if 0 <= i + 1 < len(w):
                        if w[i - 1] == "t" and w[i + 1] == "s":
                            word_list.append("ц")
                        elif w[i - 1] == "T" and w[i + 1] == "S":
                            word_list.append("Ц")

                        elif w[i - 1] == "i" and w[i + 1] == "e":
                            word_list.append("ѣ")
                        elif w[i - 1] == "I" and w[i + 1] == "E":
                            word_list.append("Ѣ")

                        elif w[i - 1] == "i" and w[i + 1] == "a":
                            word_list.append("я")
                        elif w[i - 1] == "I" and w[i + 1] == "A":
                            word_list.append("Я")

                        elif w[i - 1] == "i" and w[i + 1] == "u":
                            word_list.append("ю")
                        elif w[i - 1] == "I" and w[i + 1] == "U":
                            word_list.append("Ю")

                elif j == "k":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("х")

                elif j == "K":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("Х")

                elif j == "c":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("ч")

                elif j == "C":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("Ч")

                elif j == "s":
                    if 0 <= i + 2 < len(w):
                        if w[i + 1] == "h":
                            if w[i + 2] == "t":
                                word_list.append("щ")
                            else:
                                word_list.append("ш")
                        else:
                            word_list.append("c")
                    else:
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "h":
                                word_list.append("ш")
                            else:
                                word_list.append("c")

                        else:
                            word_list.append("c")

                elif j == "S":
                    if 0 <= i + 2 < len(w):
                        if w[i + 1] == "h":
                            if w[i + 2] == "t":
                                word_list.append("Щ")
                            else:
                                word_list.append("Ш")
                        else:
                            word_list.append("С")
                    else:
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "h":
                                word_list.append("Ш")
                            else:
                                word_list.append("С")

                        else:
                            word_list.append("С")

                elif j == 'Z':
                    if 0 <= i + 1 < len(w):
                        if [i + 1] == 'h':
                            word_list.append("Ж")
                        else:
                            word_list.append("З")
                    else:
                        word_list.append("З")

                elif j == 'z':
                    if 0 <= i + 1 < len(w):
                        if [i + 1] == 'h':
                            word_list.append("ж")
                        else:
                            word_list.append("з")
                    else:
                        word_list.append("з")

                elif j in bulgarian_to_lat_dict:
                    translatinated = bulg_translatinate(j)
                    word_list.append(translatinated)
                else:
                    word_list.append(j)

            list_of_translatinated.append(''.join(word_list))
        translatinated_full.append(''.join(list_of_translatinated))

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
                                word_list.append("ѣ")
                            elif w[i - 1] == "I" and w[i + 1] == "E":
                                word_list.append("Ѣ")

                            elif w[i - 1] == "i" and w[i + 1] == "a":
                                word_list.append("я")
                            elif w[i - 1] == "I" and w[i + 1] == "A":
                                word_list.append("Я")

                            elif w[i - 1] == "i" and w[i + 1] == "u":
                                word_list.append("ю")
                            elif w[i - 1] == "I" and w[i + 1] == "U":
                                word_list.append("Ю")

                    elif j == "k":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "h":
                                word_list.append("х")

                    elif j == "K":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "h":
                                word_list.append("Х")

                    elif j == "c":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "h":
                                word_list.append("ч")

                    elif j == "C":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "h":
                                word_list.append("Ч")

                    elif j == "s":
                        if 0 <= i + 2 < len(w):
                            if w[i + 1] == "h":
                                if w[i + 2] == "t":
                                    word_list.append("щ")
                                else:
                                    word_list.append("ш")
                            else:
                                word_list.append("c")
                        else:
                            if 0 <= i + 1 < len(w):
                                if w[i + 1] == "h":
                                    word_list.append("ш")
                                else:
                                    word_list.append("c")

                            else:
                                word_list.append("c")

                    elif j == "S":
                        if 0 <= i + 2 < len(w):
                            if w[i + 1] == "h":
                                if w[i + 2] == "t":
                                    word_list.append("Щ")
                                else:
                                    word_list.append("Ш")
                            else:
                                word_list.append("С")
                        else:
                            if 0 <= i + 1 < len(w):
                                if w[i + 1] == "h":
                                    word_list.append("Ш")
                                else:
                                    word_list.append("С")

                            else:
                                word_list.append("С")

                    elif j == 'Z':
                        if 0 <= i + 1 < len(w):
                            if [i + 1] == 'h':
                                word_list.append("Ж")
                            else:
                                word_list.append("З")
                        else:
                            word_list.append("З")

                    elif j == 'z':
                        if 0 <= i + 1 < len(w):
                            if [i + 1] == 'h':
                                word_list.append("ж")
                            else:
                                word_list.append("з")
                        else:
                            word_list.append("з")

                    elif j in bulgarian_to_lat_dict:
                        translatinated = bulg_translatinate(j)
                        word_list.append(translatinated)
                    else:
                        word_list.append(j)

                list_of_translatinated.append(''.join(word_list))
            translatinated_full.append(''.join(list_of_translatinated))

    transliterated_sents = ' '.join(translatinated_full)
    return transliterated_sents

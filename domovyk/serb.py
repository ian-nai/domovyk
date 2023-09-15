serbian_dict = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Ђ": "Đ",
    "Е": "E",
    "Ж": "Ž",
    "З": "Z",
    "И": "I",
    "Ј": "J",
    "К": "K",
    "Л": "L",
    "Љ": "Lj",
    "М": "M",
    "Н": "N",
    "Њ": "Nj",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "Ћ": "Ć",
    "У": "U",
    "Ф": "F",
    "Х": "H",
    "Ц": "C",
    "Ч": "Č",
    "Џ": "Dž",
    "Ш": "Š",
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "g",
    "д": "d",
    "ђ": "đ",
    "е": "e",
    "ж": "ž",
    "з": "z",
    "и": "i",
    "ј": "j",
    "к": "k",
    "л": "l",
    "љ": "lj",
    "м": "m",
    "н": "n",
    "њ": "nj",
    "о": "o",
    "ô": "ô",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "ћ": "ć",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "c",
    "ч": "č",
    "џ": "dž",
    "ш": "š"
}

serbian_to_lat_dict = {y: x for x, y in iter(serbian_dict.items())}

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

# Tokenize string into sentences and transliterate from Serbian to the
# Latin alphabet using the dictionary above


def serb_translit_sents(input_string):
    import re

    def serb_translate(x): return ''.join([serbian_dict[i] for i in x])

    text = string_to_list(input_string)

    translated_full = []
    for txt in text:
        list_of_translated = []
        words = re.split(r'(\s+)', txt)
        for word in words:
            word_list = []
            for letter in word:
                if letter in serbian_dict:
                    translated = serb_translate(letter)
                    word_list.append(translated)
                else:
                    word_list.append(letter)
            list_of_translated.append(''.join(word_list))
        translated_full.append(''.join(list_of_translated))

    transliterated_sents = translated_full
    return transliterated_sents

# Transliterate from Serbian to the Latin alphabet using the dictionary above


def serb_translit(input):
    import re

    def serb_translate(x): return ''.join([serbian_dict[i] for i in x])

    if isinstance(input, str):
        text = input
        translated_full = []
        list_of_translated = []
        words = re.split(r'(\s+)', text)
        for word in words:
            word_list = []
            for letter in word:
                if letter in serbian_dict:
                    translated = serb_translate(letter)
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
                    if letter in serbian_dict:
                        translated = serb_translate(letter)
                        word_list.append(translated)
                    else:
                        word_list.append(letter)
                list_of_translated.append(''.join(word_list))
            translated_full.append(''.join(list_of_translated))

        transliterated_sents = ' '.join(translated_full)
        return transliterated_sents

# Tokenize a string into sentences and transliterate from the Latin
# alphabet to Serbian


def latin_to_serb_sents(input_string):
    import re

    def serb_translatinate(x): return ''.join(
        [serbian_to_lat_dict[i] for i in x])
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
                if j == "l":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("љ")
                    else:
                        word_list.append("л")
                elif j == "L":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("Љ")
                    else:
                        word_list.append("Л")

                if j == "n":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("њ")
                    else:
                        word_list.append("н")

                elif j == "N":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("Њ")
                    else:
                        word_list.append("Н")

                if j == "d":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "ž":
                            word_list.append("џ")
                    else:
                        word_list.append("д")
                elif j == "D":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "ž":
                            word_list.append("Џ")
                    else:
                        word_list.append("Д")

                elif j in serbian_to_lat_dict:
                    translatinated = serb_translatinate(j)
                    word_list.append(translatinated)
                else:
                    word_list.append(j)

            list_of_translatinated.append(''.join(word_list))
        translatinated_full.append(''.join(list_of_translatinated))

    transliterated_sents = translatinated_full
    return transliterated_sents

# Transliterate from Serbian to the Latin alphabet


def latin_to_serb(input):
    import re

    def serb_translatinate(x): return ''.join(
        [serbian_to_lat_dict[i] for i in x])

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
                if j == "l":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("љ")
                    else:
                        word_list.append("л")
                elif j == "L":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("Љ")
                    else:
                        word_list.append("Л")

                if j == "n":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("њ")
                    else:
                        word_list.append("н")

                elif j == "N":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("Њ")
                    else:
                        word_list.append("Н")

                if j == "d":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "ž":
                            word_list.append("џ")
                    else:
                        word_list.append("д")
                elif j == "D":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "ž":
                            word_list.append("Џ")
                    else:
                        word_list.append("Д")

                elif j in serbian_to_lat_dict:
                    translatinated = serb_translatinate(j)
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
                    if j == "l":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "j":
                                word_list.append("љ")
                    elif j == "L":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "j":
                                word_list.append("Љ")

                    if j == "n":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "j":
                                word_list.append("њ")
                    elif j == "N":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "j":
                                word_list.append("Њ")

                    if j == "d":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "ž":
                                word_list.append("џ")
                    elif j == "D":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "ž":
                                word_list.append("Џ")

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
                            translatinated = serb_translatinate(j)
                            word_list.append(translatinated)

                    elif j in serbian_to_lat_dict:
                        translatinated = serb_translatinate(j)
                        word_list.append(translatinated)
                    else:
                        word_list.append(j)

                list_of_translatinated.append(''.join(word_list))
            translatinated_full.append(''.join(list_of_translatinated))

        transliterated_sents = ' '.join(translatinated_full)
        return transliterated_sents

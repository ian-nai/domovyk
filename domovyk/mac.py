macedonian_dict = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Ѓ": "Ǵ ",
    "Д": "D",
    "Е": "E",
    "Ж": "Ž",
    "З": "Z",
    "S": "D͡Z",
    "И": "I",
    "Ј": "J",
    "К": "K",
    "Ќ": "Ḱ",
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
    "У": "U",
    "Ф": "F",
    "Х": "H",
    "Ц": "C",
    "Ч": "Č",
    "Џ": "D͡Ž",
    "Ш": "Š",
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "h",
    "ѓ": "ǵ ",
    "д": "d",
    "е": "e",
    "ж": "ž",
    "з": "z",
    "s": "d͡z",
    "и": "i",
    "ј": "j",
    "к": "k",
    "ќ": "ḱ",
    "л": "l",
    "љ": "lj",
    "м": "m",
    "н": "n",
    "њ": "nj",
    "о": "o",
    "п": "p",
    "р": "r",
    "с": "s",
    "т": "t",
    "у": "u",
    "ф": "f",
    "х": "h",
    "ц": "c",
    "ч": "č",
    "џ": "d͡ž",
    "ш": "š"
}


macedonian_to_lat_dict = {y: x for x, y in iter(macedonian_dict.items())}

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

# Tokenize string into sentences and transliterate from Macedonian to the
# Latin alphabet using the dictionary above


def mac_translit_sents(input_string):
    import re

    def mac_translate(x): return ''.join([macedonian_dict[i] for i in x])

    text = string_to_list(input_string)

    translated_full = []
    for txt in text:
        list_of_translated = []
        words = re.split(r'(\s+)', txt)
        for word in words:
            word_list = []
            for letter in word:
                if letter in macedonian_dict:
                    translated = mac_translate(letter)
                    word_list.append(translated)
                else:
                    word_list.append(letter)
            list_of_translated.append(''.join(word_list))
        translated_full.append(''.join(list_of_translated))

    transliterated_sents = translated_full
    return transliterated_sents

# Transliterate from Macedonian to the Latin alphabet using the dictionary
# above


def mac_translit(input):
    import re

    def mac_translate(x): return ''.join([macedonian_dict[i] for i in x])

    if isinstance(input, str):
        text = input
        translated_full = []
        list_of_translated = []
        words = re.split(r'(\s+)', text)
        for word in words:
            word_list = []
            for letter in word:
                if letter in macedonian_dict:
                    translated = mac_translate(letter)
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
                    if letter in macedonian_dict:
                        translated = mac_translate(letter)
                        word_list.append(translated)
                    else:
                        word_list.append(letter)
                list_of_translated.append(''.join(word_list))
            translated_full.append(''.join(list_of_translated))

        transliterated_sents = ' '.join(translated_full)
        return transliterated_sents

# Tokenize a string into sentences and transliterate from the Latin
# alphabet to Macedonian


def latin_to_mac_sents(input_string):
    import re

    def mac_translatinate(x): return ''.join(
        [macedonian_to_lat_dict[i] for i in x])
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
                        if w[i - 1] == "d" and w[i + 1] == "Z":
                            word_list.append("d͡z")
                        elif w[i - 1] == "D" and w[i + 1] == "z":
                            word_list.append("D͡Ž")

                        elif w[i - 1] == "d" and w[i + 1] == "ž":
                            word_list.append("џ")
                        elif w[i - 1] == "D" and w[i + 1] == "Ž":
                            word_list.append("Џ")

                elif j == "l":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("љ")

                elif j == "L":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("Љ")

                elif j == "n":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("њ")
                        else:
                            word_list.append("н")
                    else:
                        word_list.append("н")

                elif j == "N":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("Њ")
                        else:
                            word_list.append("Н")
                    else:
                        word_list.append("Н")

                elif j in macedonian_to_lat_dict:
                    translatinated = mac_translatinate(j)
                    word_list.append(translatinated)
                else:
                    word_list.append(j)

            list_of_translatinated.append(''.join(word_list))
        translatinated_full.append(''.join(list_of_translatinated))

    transliterated_sents = translatinated_full
    return transliterated_sents

# Transliterate from Macedonian to the Latin alphabet


def latin_to_mac(input):
    import re

    def mac_translatinate(x): return ''.join(
        [macedonian_to_lat_dict[i] for i in x])

    if isinstance(input, str):
        text = input
        translatinated_full = []
        list_of_translatinated = []
        words = re.split(r'(\s+)', text)
        for w in words:
            word_list = []
            word_list = []

            for i, j, in enumerate(w):
                # making sure letters we're checking for are within the list's
                # range
                if j == u"\u0361":
                    if 0 <= i + 1 < len(w):
                        if w[i - 1] == "d" and w[i + 1] == "Z":
                            word_list.append("d͡z")
                        elif w[i - 1] == "D" and w[i + 1] == "z":
                            word_list.append("D͡Ž")

                        elif w[i - 1] == "d" and w[i + 1] == "ž":
                            word_list.append("џ")
                        elif w[i - 1] == "D" and w[i + 1] == "Ž":
                            word_list.append("Џ")

                elif j == "l":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("љ")

                elif j == "L":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("Љ")

                elif j == "n":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("њ")
                        else:
                            word_list.append("н")
                    else:
                        word_list.append("н")

                elif j == "N":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "j":
                            word_list.append("Њ")
                        else:
                            word_list.append("Н")
                    else:
                        word_list.append("Н")

                elif j in macedonian_to_lat_dict:
                    translatinated = mac_translatinate(j)
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

                word_list = []

                for i, j, in enumerate(w):
                    # making sure letters we're checking for are within the
                    # list's range
                    if j == u"\u0361":
                        if 0 <= i + 1 < len(w):
                            if w[i - 1] == "d" and w[i + 1] == "Z":
                                word_list.append("d͡z")
                            elif w[i - 1] == "D" and w[i + 1] == "z":
                                word_list.append("D͡Ž")

                            elif w[i - 1] == "d" and w[i + 1] == "ž":
                                word_list.append("џ")
                            elif w[i - 1] == "D" and w[i + 1] == "Ž":
                                word_list.append("Џ")

                    elif j == "l":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "j":
                                word_list.append("љ")

                    elif j == "L":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "j":
                                word_list.append("Љ")

                    elif j == "n":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "j":
                                word_list.append("њ")
                            else:
                                word_list.append("н")
                        else:
                            word_list.append("н")

                    elif j == "N":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "j":
                                word_list.append("Њ")
                            else:
                                word_list.append("Н")
                        else:
                            word_list.append("Н")

                    elif j in macedonian_to_lat_dict:
                        translatinated = mac_translatinate(j)
                        word_list.append(translatinated)
                    else:
                        word_list.append(j)

                list_of_translatinated.append(''.join(word_list))
            translatinated_full.append(''.join(list_of_translatinated))

    translatinated_sents = ' '.join(translatinated_full)
    return translatinated_sents

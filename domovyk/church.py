church_dict = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Є": "E",
    "Е": "Ē",
    "Ѥ": "I͡E",
    "Ж": "Zh",
    "Ѕ": "Ż",
    "З": "Z",
    "И": "I",
    "Й": "Ĭ",
    "І": "Ī",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "Ѹ": "U",
    "Ꙋ": "Ū",
    "Ф": "F",
    "Х": "Kh",
    "Ѿ": "Ō͡T",
    "Ц": "T͡S",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Sht",
    "Ъ": '"',
    "Ы": "Ȳ",
    "Ꙑ": "Y",
    "Ь": "'",
    "Ѣ": "Ě",
    "Ю": "I͡U",
    "Ꙗ": "I͡A",
    "Ѧ": "Ę",
    "Ѯ": "K͡S",
    "Ѱ": "P͡S",
    "Ѳ": "Ḟ",
    "Ѷ": "Ẏ",
    "Ѫ": "Ǫ",
    "Ѩ": "I͡Ę",
    "Ѭ": "I͡Ǫ",
    "Ћ": "Ǵ",
    "а": "a",
    "б": "b",
    "в": "v",
    "г": "h",
    "ґ": "g",
    "д": "d",
    "є": "e",
    "є": "ē",
    "ѥ": "i͡e",
    "ж": "zh",
    "ѕ": "ż",
    "з": "z",
    "и": "I",
    "й": "ĭ",
    "і": "ī",
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
    "ѹ": "u",
    "ꙋ": "ū",
    "ф": "f",
    "х": "kh",
    "ѿ": "ō͡t",
    "ѡ": "ō",
    "ц": "t͡s",
    "ч": "ch",
    "ш": "sh",
    "щ": "sht",
    "ъ": 'ʺ',
    "ы": "ȳ",
    "ꙑ": "y",
    "ь": "ʹ",
    "ѣ": "ě",
    "ю": "i͡u",
    "ꙗ": "i͡a",
    "ѧ": "ę",
    "ѯ": "k͡s",
    "ѱ": "p͡s",
    "ѳ": "ḟ",
    "ѷ": "ẏ",
    "у": "v̇",
    "ѫ": "ǫ",
    "ѩ": "i͡ę",
    "ѭ": "i͡ǫ",
    "ћ": "ǵ"
}

latinate_dict = {value: key for key, value in church_dict.items()}

church_to_lat_dict = {y: x for x, y in iter(church_dict.items())}

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

# Tokenize string into sentences and transliterate from Church Slavonic to the
# Latin alphabet using the dictionary above


def church_translit_sents(input_string):
    import re

    def church_translate(x): return ''.join([church_dict[i] for i in x])

    text = string_to_list(input_string)

    translated_full = []
    for txt in text:
        list_of_translated = []
        words = re.split(r'(\s+)', txt)
        for word in words:
            word_list = []
            for letter in word:
                if letter in church_dict:
                    translated = church_translate(letter)
                    word_list.append(translated)
                else:
                    word_list.append(letter)
            list_of_translated.append(''.join(word_list))
        translated_full.append(''.join(list_of_translated))

    transliterated_sents = translated_full
    return transliterated_sents

# Transliterate from Church Slavonic to the Latin alphabet using the dictionary
# above


def church_translit(input):
    import re

    def church_translate(x): return ''.join([church_dict[i] for i in x])

    if isinstance(input, str):
        text = input
        translated_full = []
        list_of_translated = []
        words = re.split(r'(\s+)', text)
        for word in words:
            word_list = []
            for letter in word:
                if letter in church_dict:
                    translated = church_translate(letter)
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
                    if letter in church_dict:
                        translated = church_translate(letter)
                        word_list.append(translated)
                    else:
                        word_list.append(letter)
                list_of_translated.append(''.join(word_list))
            translated_full.append(''.join(list_of_translated))

        transliterated_sents = ' '.join(translated_full)
        return transliterated_sents

# Tokenize a string into sentences and transliterate from the Latin
# alphabet to Church Slavonic


def latin_to_church_sents(input_string):
    import re

    def church_translatinate(x): return ''.join(
        [church_to_lat_dict[i] for i in x])
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
                # breve

                if j == u"\u0361":
                    if 0 <= i + 1 < len(w):
                        if w[i - 1] == "i" and w[i + 1] == "e":
                            word_list.append("ѥ")
                        elif w[i - 1] == "I" and w[i + 1] == "E":
                            word_list.append("Ѥ")

                        elif w[i - 1] == "i" and w[i + 1] == "ę":
                            word_list.append("ѩ")
                        elif w[i - 1] == "I" and w[i + 1] == "Ę":
                            word_list.append("Ѩ")

                        elif w[i - 1] == "i" and w[i + 1] == "a":
                            word_list.append("ꙗ")
                        elif w[i - 1] == "I" and w[i + 1] == "A":
                            word_list.append("Ꙗ")

                        elif w[i - 1] == "i" and w[i + 1] == "u":
                            word_list.append("ю")
                        elif w[i - 1] == "I" and w[i + 1] == "U":
                            word_list.append("Ю")

                        elif w[i - 1] == "i" and w[i + 1] == "ǫ":
                            word_list.append("ѭ")
                        elif w[i - 1] == "I" and w[i + 1] == "Ǫ":
                            word_list.append("Ѭ")

                        elif w[i - 1] == "ō" and w[i + 1] == "t":
                            word_list.append("ѿ")
                        elif w[i - 1] == "Ō" and w[i + 1] == "T":
                            word_list.append("Ѿ")

                        elif w[i - 1] == "t" and w[i + 1] == "s":
                            word_list.append("ц")
                        elif w[i - 1] == "T" and w[i + 1] == "S":
                            word_list.append("Ц")

                        elif w[i - 1] == "k" and w[i + 1] == "s":
                            word_list.append("ѯ")
                        elif w[i - 1] == "K" and w[i + 1] == "S":
                            word_list.append("Ѯ")

                        elif w[i - 1] == "p" and w[i + 1] == "s":
                            word_list.append("ѱ")
                        elif w[i - 1] == "P" and w[i + 1] == "S":
                            word_list.append("Ѱ")

                elif j == "k":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("х")

                elif j == "K":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("Х")
                        else:
                            word_list.append('K')
                    else:
                        word_list.append('K')

                elif j == "t":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "s":
                            word_list.append("ц")
                        else:
                            word_list.append("т")
                    else:
                        word_list.append("т")

                elif j == "T":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "s":
                            word_list.append("Ц")
                        else:
                            word_list.append("Т")
                    else:
                        word_list.append("Т")

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

                elif j in latinate_dict:
                    translatinated = church_translatinate(j)
                    word_list.append(translatinated)
                else:
                    word_list.append(j)

            list_of_translatinated.append(''.join(word_list))
        translatinated_full.append(''.join(list_of_translatinated))

    transliterated_sents = translatinated_full
    return transliterated_sents


# Transliterate from Church Slavonic to the Latin alphabet
def latin_to_church(input):
    import re

    def church_translatinate(x): return ''.join([latinate_dict[i] for i in x])

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
                        if w[i - 1] == "i" and w[i + 1] == "o":
                            word_list.append("ё")
                        elif w[i - 1] == "I" and w[i + 1] == "O":
                            word_list.append("Ё")

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

                elif j == "k":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("х")

                elif j == "K":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("Х")
                        else:
                            word_list.append('K')
                    else:
                        word_list.append('K')

                elif j == "t":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "s":
                            word_list.append("ц")
                        else:
                            word_list.append("т")
                    else:
                        word_list.append("т")

                elif j == "T":
                    if 0 <= i + 1 < len(w):
                        if w[i + 1] == "s":
                            word_list.append("Ц")
                        else:
                            word_list.append("Т")
                    else:
                        word_list.append("Т")

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
                    elif 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("ш")
                        else:
                            word_list.append("c")

                    elif i != 0:
                        if w[i - 1] == "t":
                            continue
                        else:
                            word_list.append("c")
                    else:
                        word_list.append("c")

                elif j == "S":
                    if 0 <= i + 3 < len(w):
                        if w[i + 1] == "h":
                            if w[i + 2] == "c":
                                if w[i + 3] == "h":
                                    word_list.append("Щ")
                    elif 0 <= i + 1 < len(w):
                        if w[i + 1] == "h":
                            word_list.append("Ш")
                        else:
                            word_list.append("С")

                    elif i != 0:
                        if w[i - 1] == "T":
                            continue
                        else:
                            word_list.append("С")
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

                elif j in latinate_dict:
                    translatinated = church_translatinate(j)
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
                            if w[i - 1] == "i" and w[i + 1] == "o":
                                word_list.append("ё")
                            elif w[i - 1] == "I" and w[i + 1] == "O":
                                word_list.append("Ё")

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

                    elif j == "k":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "h":
                                word_list.append("х")

                    elif j == "K":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "h":
                                word_list.append("Х")
                            else:
                                word_list.append('K')
                        else:
                            word_list.append('K')

                    elif j == "t":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "s":
                                word_list.append("ц")
                            else:
                                word_list.append("т" + w[i + 1])
                        else:
                            word_list.append("т")

                    elif j == "T":
                        if 0 <= i + 1 < len(w):
                            if w[i + 1] == "s":
                                word_list.append("Ц")
                            else:
                                word_list.append("Т" + w[i + 1])
                        else:
                            word_list.append("Т")

                    elif j == "s":
                        if i == 0:
                            continue
                        elif w[i - 1] == "t":
                            continue

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
                                else:
                                    word_list.append("С")

                    elif j == 'h':
                        if i != 0:
                            if [i - 1] == 'c':
                                if [i - 2] == "h":
                                    if [i - 3] == "s":
                                        continue
                                else:
                                    continue

                            elif [i - 1] == 'C':
                                word_list.append("Ч")
                        else:
                            word_list.append("г")

                    elif j in latinate_dict:
                        translatinated = church_translatinate(j)
                        word_list.append(translatinated)
                    else:
                        word_list.append(j)

            list_of_translatinated.append(''.join(word_list))
        translatinated_full.append(''.join(list_of_translatinated))

    transliterated_sents = ' '.join(translatinated_full)
    return transliterated_sents

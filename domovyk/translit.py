from domovyk import bel, bulg, carp, mac, rus, ukr, serb


def transliterate(var, lang):
    if lang == 'bel':
        transliterated = bel.bel_translit(var)
        return transliterated
    elif lang == 'bulg':
        transliterated = bulg.bulg_translit(var)
        return transliterated
    if lang == 'carp':
        transliterated = carp.carp_translit(var)
        return transliterated
    if lang == 'mac':
        transliterated = mac.mac_translit(var)
        return transliterated
    if lang == 'rus':
        transliterated = rus.rus_translit(var)
        return transliterated
    if lang == 'ukr':
        transliterated = ukr.ukr_translit(var)
        return transliterated
    if lang == 'serb':
        transliterated = serb.serb_translit(var)
        return transliterated


def translatinate(var, lang):
    if lang == 'bel':
        translatinated = bel.latin_to_bel(var)
        return translatinated
    elif lang == 'bulg':
        translatinated = bulg.latin_to_bulg(var)
        return translatinated
    if lang == 'carp':
        translatinated = carp.latin_to_carp(var)
        return translatinated
    if lang == 'mac':
        translatinated = mac.latin_to_mac(var)
        return translatinated
    if lang == 'rus':
        translatinated = rus.latin_to_rus(var)
        return translatinated
    if lang == 'ukr':
        translatinated = ukr.latin_to_ukr(var)
        return translatinated
    if lang == 'serb':
        translatinated = serb.latin_to_serb(var)
        return translatinated


def transliterateSents(var, lang):
    if lang == 'bel':
        transliterated = bel.bel_translit_sents(var)
        return transliterated
    elif lang == 'bulg':
        transliterated = bulg.bulg_translit_sents(var)
        return transliterated
    if lang == 'carp':
        transliterated = carp.carp_translit_sents(var)
        return transliterated
    if lang == 'mac':
        transliterated = mac.mac_translit_sents(var)
        return transliterated
    if lang == 'rus':
        transliterated = rus.rus_translit_sents(var)
        return transliterated
    if lang == 'ukr':
        transliterated = ukr.ukr_translit_sents(var)
        return transliterated
    if lang == 'serb':
        transliterated = serb.serb_translit_sents(var)
        return transliterated


def translatinateSents(var, lang):
    if lang == 'bel':
        translatinated = bel.latin_to_bel_sents(var)
        return translatinated
    elif lang == 'bulg':
        translatinated = bulg.latin_to_bulg_sents(var)
        return translatinated
    if lang == 'carp':
        translatinated = carp.latin_to_carp_sents(var)
        return translatinated
    if lang == 'mac':
        translatinated = mac.latin_to_mac_sents(var)
        return translatinated
    if lang == 'rus':
        translatinated = rus.latin_to_rus_sents(var)
        return translatinated
    if lang == 'ukr':
        translatinated = ukr.latin_to_ukr_sents(var)
        return translatinated
    if lang == 'serb':
        translatinated = serb.latin_to_serb_sents(var)
        return translatinated

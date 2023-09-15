import unittest
from domovyk import bel, bulg, carp, mac, rus, ukr, serb, translit


class TestClient(unittest.TestCase):
    bel_var = "Любя, съешь щипцы, — вздохнёт мэр, — Кайф жгуч! Ѫѣ"
    bel_var_sents = "Любя, съешь щипцы, — вздохнёт мэр, — Кайф жгуч! Разъяренный чтец эгоистично бьёт пятью жердями шустрого фехтовальщика. Ґѣэ."

    bulg_var = "Аз съм учител."
    bulg_var_sents = "Аз съм учител. Иван е лекар."

    carp_var = "Еден јазик никогаш не е доволен."
    carp_var_sents = "Еден јазик никогаш не е доволен. Те молам зборувај побавно."

    mac_var = "Еден јазик никогаш не е доволен."
    mac_var_sents = "Еден јазик никогаш не е доволен. Те молам зборувај побавно."

    rus_var = "Любя, съешь щипцы, — вздохнёт мэр, — Кайф жгуч!"
    rus_var_sents = "Любя, съешь щипцы, — вздохнёт мэр, — Кайф жгуч! Разъяренный чтец эгоистично бьёт пятью жердями шустрого фехтовальщика."

    ukr_var = "Єхидна, ґава, їжак ще й шиплячі плазуни бігцем форсують Янцзи."
    ukr_var_sents = "Єхидна, ґава, їжак ще й шиплячі плазуни бігцем форсують Янцзи. Ви розмовляєте українською?"

    serb_var = "Брза вижљаста лија хоће да ђипи преко њушке флегматичног џукца."
    serb_var_sents = "Брза вижљаста лија хоће да ђипи преко њушке флегматичног џукца. Можеш разговарати са мном на српском."

    latin_var_sents = "This is a test. And another test."
    latin_var = "This is a test."

    # Belarusian
    def test_bel_translit_sents(self):
        transliterated = bel.bel_translit_sents(TestClient.bel_var_sents)
        assert transliterated[0] == "Li͡ubi͡a, sʺeshʹ shchīptsy, — vzdokhni͡ot mėr, — Kaĭf z͡hhuch!"
        assert transliterated[2] == "Gěė."

    def test_bel_translit(self):
        transliterated = bel.bel_translit(TestClient.bel_var)
        assert transliterated == "Li͡ubi͡a, sʺeshʹ shchīptsy, — vzdokhni͡ot mėr, — Kaĭf z͡hhuch! Ѫě"

    def test_latin_to_bel_sents(self):
        transliterated = bel.latin_to_bel_sents(TestClient.latin_var_sents)
        assert transliterated[0] == "Тгic ic а теcт."

    def test_latin_to_bel(self):
        transliterated = bel.latin_to_bel(TestClient.latin_var)
        assert transliterated == "Тгic ic а теcт."

    # Bulgarian

    def test_bulg_translit_sents(self):
        transliterated = bulg.bulg_translit_sents(TestClient.bulg_var_sents)
        assert transliterated[0] == "Az sŭm uchitel."
        assert transliterated[1] == "Ivan e lekar."

    def test_bulg_translit(self):
        transliterated = bulg.bulg_translit(TestClient.bulg_var)
        assert transliterated == "Az sŭm uchitel."
    #

    def test_latin_to_bulg_sents(self):
        transliterated = bulg.latin_to_bulg_sents(TestClient.latin_var_sents)
        assert transliterated[0] == "Тhиc иc а теcт."
        assert transliterated[1] == "Анд анотhер теcт."

    def test_latin_to_bulg(self):
        transliterated = bulg.latin_to_bulg(TestClient.latin_var)
        assert transliterated == "Тhиc иc а теcт."

    # Carpatho-Rusyn

    def test_carp_translit_sents(self):
        transliterated = carp.carp_translit_sents(TestClient.carp_var_sents)
        assert transliterated[0] == "Eden јazyk nykohash ne e dovolen."
        assert transliterated[1] == "Te molam zboruvaј pobavno."

    def test_carp_translit(self):
        transliterated = carp.carp_translit(TestClient.carp_var)
        assert transliterated == "Eden јazyk nykohash ne e dovolen."

    def test_latin_to_carp_sents(self):
        transliterated = carp.latin_to_carp_sents(TestClient.latin_var_sents)
        assert transliterated[0] == "Тгic ic а теcт."
        assert transliterated[1] == "Анд анотгер теcт."

    def test_latin_to_carp(self):
        transliterated = carp.latin_to_carp(TestClient.latin_var)
        assert transliterated == "Тгic ic а теcт."

    # Macedonian

    def test_mac_translit_sents(self):
        transliterated = mac.mac_translit_sents(TestClient.mac_var_sents)
        assert transliterated[0] == "Eden jazik nikohaš ne e dovolen."
        assert transliterated[1] == "Te molam zboruvaj pobavno."

    def test_mac_translit(self):
        transliterated = mac.mac_translit(TestClient.mac_var)
        assert transliterated == "Eden jazik nikohaš ne e dovolen."

    def test_latin_to_mac_sents(self):
        transliterated = mac.latin_to_mac_sents(TestClient.latin_var_sents)
        assert transliterated[0] == "Тхис ис а тест."
        assert transliterated[1] == "Анд анотхер тест."

    def test_latin_to_mac(self):
        transliterated = mac.latin_to_mac(TestClient.latin_var)
        assert transliterated == "Тхис ис а тест."

    # Russian

    def test_rus_translit_sents(self):
        transliterated = rus.rus_translit_sents(TestClient.rus_var_sents)
        assert transliterated[0] == "Li͡ubi͡a, sʺeshʹ shchipt͡sy, — vzdokhnёt mėr, — Kaĭf zhguch!"
        assert transliterated[1] == "Razʺi͡arennyĭ chtet͡s ėgoistichno bʹёt pi͡atʹi͡u zherdi͡ami shustrogo fekhtovalʹshchika."

    def test_rus_translit(self):
        transliterated = rus.rus_translit(TestClient.rus_var)
        assert transliterated == "Li͡ubi͡a, sʺeshʹ shchipt͡sy, — vzdokhnёt mėr, — Kaĭf zhguch!"

    def test_latin_to_rus_sents(self):
        transliterated = rus.latin_to_rus_sents(TestClient.latin_var_sents)
        assert transliterated[0] == "Тгиc иc а теcт."
        assert transliterated[1] == "Анд анотгер теcт."

    def test_latin_to_rus(self):
        transliterated = rus.latin_to_rus(TestClient.latin_var)
        assert transliterated == "Тгиc иc а теcт."

    # Serbian

    def test_serb_translit_sents(self):
        transliterated = serb.serb_translit_sents(TestClient.serb_var_sents)
        assert transliterated[0] == "Brza vižljasta lija hoće da đipi preko njuške flegmatičnog džukca."
        assert transliterated[1] == "Možeš razgovarati sa mnom na srpskom."

    def test_serb_translit(self):
        transliterated = serb.serb_translit(TestClient.serb_var)
        assert transliterated == "Brza vižljasta lija hoće da đipi preko njuške flegmatičnog džukca."

    def test_latin_to_serb_sents(self):
        transliterated = serb.latin_to_serb_sents(TestClient.latin_var_sents)
        assert transliterated[0] == "Тхис ис а тест."
        assert transliterated[1] == "Анд анотхер тест."

    def test_latin_to_serb(self):
        transliterated = serb.latin_to_serb(TestClient.latin_var)
        assert transliterated == "Тхис ис а тест."

    # Ukrainian

    def test_ukr_translit_sents(self):
        transliterated = ukr.ukr_translit_sents(TestClient.ukr_var_sents)
        assert transliterated[0] == "I͡Ekhydna, gava, їz͡hak shche ĭ shypli͡achі plazuny bіht͡sem forsui͡utʹ I͡Ant͡szy."
        assert transliterated[1] == "Vy rozmovli͡ai͡ete ukraїnsʹkoi͡u?"

    def test_ukr_translit(self):
        transliterated = ukr.ukr_translit(TestClient.ukr_var)
        assert transliterated == "I͡Ekhydna, gava, їz͡hak shche ĭ shypli͡achі plazuny bіht͡sem forsui͡utʹ I͡Ant͡szy."

    def test_latin_to_ukr_sents(self):
        transliterated = ukr.latin_to_ukr_sents(TestClient.latin_var_sents)
        assert transliterated[0] == "Тгic ic а теcт."
        assert transliterated[1] == "Анд анотгер теcт."

    def test_latin_to_ukr(self):
        transliterated = ukr.latin_to_ukr(TestClient.latin_var)
        assert transliterated == "Тгic ic а теcт."

    # Translit Tests

    def test_transliterate(self):
        transliterated = translit.transliterate("Тхис ис а тест.", "rus")
        assert transliterated == "Tkhis is a test."

    def test_translatinate(self):
        transliterated = translit.translatinate("Тhis is a test.", "ukr")
        assert transliterated == "Тгic ic а теcт."

    def test_transliterateSents(self):
        transliterated = translit.transliterateSents(
            "Тгic ic а теcт. Анд анотхер тест.", "bel")
        assert transliterated[1] == "And anotkher test."

    def test_translatinateSents(self):
        transliterated = translit.translatinateSents(
            "Тhis is a test. And another test.", "mac")
        assert transliterated[1] == "Анд анотхер тест."

    if __name__ == '__main__':
        unittest.main()

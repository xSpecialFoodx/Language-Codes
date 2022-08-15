#
# #
# # #
# # # # Language Codes
# # #
# #
#

"""
Description:

    Language codes as a python object
    For language codes look at:
    1: https://www.science.co.il/language/Codes.php
    2: https://www.loc.gov/standards/iso639-2/php/code_list.php
"""

from __future__ import annotations

from unidecode import unidecode

# from __future__ import annotations ->
# must occur at the beginning of the file, this import makes it possible to use classes as defined types before runtime (this will be the default in python 4)
# for example: source_variable: SourceClass, in the past you would need to literate it like this: source_variable: "SourceClass", or check if the class has been
# defined before trying to use it as a type

# self is used in class objects and data objects
# @staticmethod is used only in class methods which are static


# Global Variables

# whether the languages object got initialized
Initialized = False

# the languages object
Languages = {}

Languages["Afar"] = ["Afar", "aa", "aar", "afar"]
Languages["Abkhazian"] = ["Abkhazian", "ab", "abk", "abkhaze"]
Languages["Achinese"] = ["Achinese", "ace"]
Languages["Acoli"] = ["Acoli", "ach"]
Languages["Adangme"] = ["Adangme", "ada"]
Languages["Adyghe"] = ["Adyghe", "Adygei", "ady"]
Languages["Avestan"] = ["Avestan", "ae", "ave", "avestique"]
Languages["Afrikaans"] = ["Afrikaans", "af", "afr", "afrikaans"]
Languages["Afro-Asiatic languages"] = ["Afro-Asiatic languages", "afa"]
Languages["Afrihili"] = ["Afrihili", "afh"]
Languages["Ainu"] = ["Ainu", "ain"]
Languages["Akan"] = ["Akan", "ak", "aka", "akan"]
Languages["Akkadian"] = ["Akkadian", "akk"]
Languages["Aleut"] = ["Aleut", "ale"]
Languages["Algonquian languages"] = ["Algonquian languages", "alg"]
Languages["Southern Altai"] = ["Southern Altai", "alt"]
Languages["Amharic"] = ["Amharic", "am", "amh", "amharique"]
Languages["Aragonese"] = ["Aragonese", "an", "arg", "aragonais"]
Languages["English, Old"] = ["English, Old", "English, Old (ca.450-1100)", "ang"]
Languages["Angika"] = ["Angika", "anp"]
Languages["Apache languages"] = ["Apache languages", "apa"]
Languages["Arabic"] = ["Arabic", "ar", "ara", "arab", "arabe"]
Languages["Imperial Aramaic"] = ["Imperial Aramaic", "Imperial Aramaic (700-300 BCE)", "arc"]
Languages["Official Aramaic"] = ["Official Aramaic", "Official Aramaic (700-300 BCE)", "arc"]
Languages["Mapuche"] = ["Mapuche", "arn"]
Languages["Mapudungun"] = ["Mapudungun", "arn"]
Languages["Arapaho"] = ["Arapaho", "arp"]
Languages["Artificial languages"] = ["Artificial languages", "art"]
Languages["Arawak"] = ["Arawak", "arw"]
Languages["Assamese"] = ["Assamese", "as", "asm", "assamais"]
Languages["Asturian"] = ["Asturian", "ast"]
Languages["Asturleonese"] = ["Asturleonese", "ast"]
Languages["Bable"] = ["Bable", "ast"]
Languages["Leonese"] = ["Leonese", "ast"]
Languages["Athapascan languages"] = ["Athapascan languages", "ath"]
Languages["Australian languages"] = ["Australian languages", "aus"]
Languages["Avaric"] = ["Avaric", "av", "ava", "avar"]
Languages["Awadhi"] = ["Awadhi", "awa"]
Languages["Aymara"] = ["Aymara", "ay", "aym", "aymara"]
Languages["Azerbaijani"] = ["Azerbaijani", "az", "aze", "azéri"]
Languages["Bashkir"] = ["Bashkir", "ba", "bak", "bachkir"]
Languages["Banda languages"] = ["Banda languages", "bad"]
Languages["Bamileke languages"] = ["Bamileke languages", "bai"]
Languages["Baluchi"] = ["Baluchi", "bal"]
Languages["Balinese"] = ["Balinese", "ban"]
Languages["Basa"] = ["Basa", "bas"]
Languages["Baltic languages"] = ["Baltic languages", "bat"]
Languages["Belarusian"] = ["Belarusian", "be", "bel", "biélorusse"]
Languages["Bedawiyet"] = ["Bedawiyet", "bej"]
Languages["Beja"] = ["Beja", "bej"]
Languages["Bemba"] = ["Bemba", "bem"]
Languages["Berber languages"] = ["Berber languages", "ber"]
Languages["Bulgarian"] = ["Bulgarian", "bg", "bul", "bulgare"]
Languages["Bihari languages"] = ["Bihari", "Bihari languages", "bh", "bih", "biharis"]
Languages["Bhojpuri"] = ["Bhojpuri", "bho"]
Languages["Bislama"] = ["Bislama", "bi", "bis", "bichlamar"]
Languages["Bikol"] = ["Bikol", "bik"]
Languages["Bini"] = ["Bini", "bin"]
Languages["Edo"] = ["Edo", "bin"]
Languages["Siksika"] = ["Siksika", "bla"]
Languages["Bambara"] = ["Bambara", "bm", "bam", "bambara"]
Languages["Bengali"] = ["Bengali", "bn", "ben", "bengali"]
Languages["Bantu languages"] = ["Bantu languages", "bnt"]
Languages["Tibetan"] = ["Tibetan", "bo", "bod", "tib", "tibétain"]
Languages["Breton"] = ["Breton", "br", "bre", "breton"]
Languages["Braj"] = ["Braj", "bra"]
Languages["Bosnian"] = ["Bosnian", "bs", "bos", "bosniaque"]
Languages["Batak languages"] = ["Batak languages", "btk"]
Languages["Buriat"] = ["Buriat", "bua"]
Languages["Buginese"] = ["Buginese", "bug"]
Languages["Blin"] = ["Blin", "Bilin", "byn"]
Languages["Catalan"] = ["Catalan", "ca", "cat", "catalan"]
Languages["Valencian"] = ["Valencian", "ca", "cat", "valencien"]
Languages["Caddo"] = ["Caddo", "cad"]
Languages["Central American Indian languages"] = ["Central American Indian languages", "cai"]
Languages["Caucasian languages"] = ["Caucasian languages", "cau"]
Languages["Chechen"] = ["Chechen", "ce", "che", "tchétchène"]
Languages["Cebuano"] = ["Cebuano", "ceb"]
Languages["Celtic languages"] = ["Celtic languages", "cel"]
Languages["Chamorro"] = ["Chamorro", "ch", "cha", "chamorro"]
Languages["Chibcha"] = ["Chibcha", "chb"]
Languages["Chagatai"] = ["Chagatai", "chg"]
Languages["Chuukese"] = ["Chuukese", "chk", "chuuk"]
Languages["Mari"] = ["Mari", "chm"]
Languages["Chinook jargon"] = ["Chinook jargon", "chn"]
Languages["Choctaw"] = ["Choctaw", "cho"]
Languages["Chipewyan"] = ["Chipewyan", "chp"]
Languages["Dene Suline"] = ["Dene Suline", "chp"]
Languages["Cherokee"] = ["Cherokee", "chr"]
Languages["Cheyenne"] = ["Cheyenne", "chy"]
Languages["Chamic languages"] = ["Chamic languages", "cmc"]
Languages["Montenegrin"] = ["Montenegrin", "cnr"]
Languages["Corsican"] = ["Corsican", "co", "cos", "corse"]
Languages["Coptic"] = ["Coptic", "cop"]
Languages["Creoles and pidgins, English based"] = ["Creoles and pidgins, English based", "cpe"]
Languages["Creoles and pidgins, French-based"] = ["Creoles and pidgins, French-based", "cpf"]
Languages["Creoles and pidgins, Portuguese-based"] = ["Creoles and pidgins, Portuguese-based", "cpp"]
Languages["Cree"] = ["Cree", "cr", "cre", "cree"]
Languages["Crimean Tatar"] = ["Crimean Tatar", "crh"]
Languages["Crimean Turkish"] = ["Crimean Turkish", "crh"]
Languages["Creoles and pidgins"] = ["Creoles and pidgins", "crp"]
Languages["Czech"] = ["Czech", "cs", "ces", "cze", "tchèque"]
Languages["Kashubian"] = ["Kashubian", "csb"]
Languages["Church Slavic"] = ["Church Slavic", "cu", "chu", "slavon d'église"]
Languages["Old Bulgarian"] = ["Old Bulgarian", "cu", "chu", "vieux bulgare"]
Languages["Old Church Slavonic"] = ["Old Church Slavonic", "cu", "chu", "vieux slave"]
Languages["Slavonic"] = ["Slavonic", "cu", "chu", "slavon liturgique"]
Languages["Cushitic languages"] = ["Cushitic languages", "cus"]
Languages["Chuvash"] = ["Chuvash", "cv", "chv", "tchouvache"]
Languages["Welsh"] = ["Welsh", "cy", "cym", "wel", "gallois"]
Languages["Danish"] = ["Danish", "da", "dan", "danois"]
Languages["Dakota"] = ["Dakota", "dak"]
Languages["Dargwa"] = ["Dargwa", "dar"]
Languages["Land Dayak languages"] = ["Land Dayak languages", "day"]
Languages["Delaware"] = ["Delaware", "del"]
Languages["Slave (Athapascan)"] = ["Slave (Athapascan)", "den"]
Languages["Dogrib"] = ["Dogrib", "dgr"]
Languages["Dinka"] = ["Dinka", "din"]
Languages["Dogri"] = ["Dogri", "doi"]
Languages["Dravidian languages"] = ["Dravidian languages", "dra"]
Languages["Lower Sorbian"] = ["Lower Sorbian", "dsb"]
Languages["Duala"] = ["Duala", "dua"]
Languages["Dutch, Middle"] = ["Dutch, Middle", "Dutch, Middle (ca.1050-1350)", "dum"]
Languages["Dutch"] = ["Dutch", "dut", "nl", "nld", "néerlandais"]
Languages["Divehi"] = ["Divehi", "Dhivehi", "dv", "div"]
Languages["Maldivian"] = ["Maldivian", "dv", "div", "maldivien"]
Languages["Dyula"] = ["Dyula", "dyu"]
Languages["Dzongkha"] = ["Dzongkha", "dz", "dzo", "dzongkha"]
Languages["Ewe"] = ["Ewe", "ee", "ewe", "éwé"]
Languages["Efik"] = ["Efik", "efi"]
Languages["Egyptian"] = ["Egyptian", "Egyptian (Ancient)", "egy"]
Languages["Ekajuk"] = ["Ekajuk", "eka"]
Languages["Elamite"] = ["Elamite", "elx"]
Languages["English"] = ["English", "en", "eng", "anglais"]
Languages["English, Middle"] = ["English, Middle", "English, Middle (1100-1500)", "enm"]
Languages["Esperanto"] = ["Esperanto", "eo", "epo", "espéranto"]
Languages["Castilian"] = ["Castilian", "es", "spa", "castillan"]
Languages["Spanish"] = ["Spanish", "es", "spa", "espagnol"]
Languages["Estonian"] = ["Estonian", "et", "est", "estonien"]
Languages["Basque"] = ["Basque", "eu", "eus", "baq", "basque"]
Languages["Ewondo"] = ["Ewondo", "ewo"]
Languages["Fang"] = ["Fang", "fan"]
Languages["Fanti"] = ["Fanti", "fat"]
Languages["Fulah"] = ["Fulah", "ff", "ful", "peul"]
Languages["Finnish"] = ["Finnish", "fi", "fin", "finnois"]
Languages["Filipino"] = ["Filipino", "Pilipino", "fil"]
Languages["Finno-Ugrian languages"] = ["Finno-Ugrian languages", "fiu"]
Languages["Fijian"] = ["Fijian", "fj", "fij", "fidjien"]
Languages["Faroese"] = ["Faroese", "fo", "fao", "féroïen"]
Languages["Fon"] = ["Fon", "fon"]
Languages["French"] = ["French", "fre", "fra", "fr", "français"]
Languages["French, Middle"] = ["French, Middle", "French, Middle (ca.1400-1600)", "frm"]
Languages["French, Old"] = ["French, Old", "French, Old (842-ca.1400)", "fro"]
Languages["Northern Frisian"] = ["Northern Frisian", "frr"]
Languages["Eastern Frisian"] = ["Eastern Frisian", "frs"]
Languages["Western Frisian"] = ["Western Frisian", "fry", "fy", "frison occidental"]
Languages["Friulian"] = ["Friulian", "fur"]
Languages["Irish"] = ["Irish", "ga", "gle", "irlandais"]
Languages["Ga"] = ["Ga", "gaa"]
Languages["Gayo"] = ["Gayo", "gay"]
Languages["Gbaya"] = ["Gbaya", "gba"]
Languages["Gaelic"] = ["Gaelic", "gd", "gla", "gaélique"]
Languages["Scottish Gaelic"] = ["Scottish Gaelic", "gd", "gla", "gaélique écossais"]
Languages["Germanic languages"] = ["Germanic languages", "gem"]
Languages["Deutsch"] = ["Deutsch", "ger", "de", "deu", "allemand"]
Languages["German"] = ["German", "ger", "de", "deu", "allemand"]
Languages["Geez"] = ["Geez", "gez"]
Languages["Gilbertese"] = ["Gilbertese", "gil"]
Languages["Galician"] = ["Galician", "gl", "glg", "galicien"]
Languages["German, Middle High"] = ["German, Middle High", "German, Middle High (ca.1050-1500)", "gmh"]
Languages["Guarani"] = ["Guarani", "gn", "grn", "guarani"]
Languages["German, Old High"] = ["German, Old High", "German, Old High (ca.750-1050)", "goh"]
Languages["Gondi"] = ["Gondi", "gon"]
Languages["Gorontalo"] = ["Gorontalo", "gor"]
Languages["Gothic"] = ["Gothic", "got"]
Languages["Grebo"] = ["Grebo", "grb"]
Languages["Greek, Ancient"] = ["Greek, Ancient", "Greek, Ancient (to 1453)", "grc"]
Languages["Greek"] = ["Greek", "Greek, Modern", "Greek, Modern (1453-)", "gre", "el", "ell", "grec", "grec moderne", "grec moderne (après 1453)"]
Languages["Alemannic"] = ["Alemannic", "gsw"]
Languages["Alsatian"] = ["Alsatian", "gsw"]
Languages["Swiss German"] = ["Swiss German", "gsw"]
Languages["Gujarati"] = ["Gujarati", "gu", "guj", "goudjrati"]
Languages["Manx"] = ["Manx", "gv", "glv", "manx", "mannois"]
Languages["Gwich'in"] = ["Gwich'in", "gwi"]
Languages["Hausa"] = ["Hausa", "ha", "hau", "haoussa"]
Languages["Haida"] = ["Haida", "hai"]
Languages["Hawaiian"] = ["Hawaiian", "haw"]
Languages["Hebrew"] = ["Hebrew", "he", "heb", "hébreu"]
Languages["Hindi"] = ["Hindi", "hi", "hin", "hindi"]
Languages["Hiligaynon"] = ["Hiligaynon", "hil"]
Languages["Himachali languages"] = ["Himachali languages", "him"]
Languages["Western Pahari languages"] = ["Western Pahari languages", "him"]
Languages["Hittite"] = ["Hittite", "hit"]
Languages["Hmong"] = ["Hmong", "Mong", "hmn", "hmong"]
Languages["Hiri Motu"] = ["Hiri Motu", "ho", "hmo", "hiri motu"]
Languages["Croatian"] = ["Croatian", "hr", "hrv", "croate"]
Languages["Upper Sorbian"] = ["Upper Sorbian", "hsb"]
Languages["Haitian Creole"] = ["Haitian Creole", "ht", "hat", "créole haïtien"]
Languages["Haitian"] = ["Haitian", "ht", "hat", "haïtien"]
Languages["Hungarian"] = ["Hungarian", "hu", "hun", "hongrois"]
Languages["Hupa"] = ["Hupa", "hup"]
Languages["Armenian"] = ["Armenian", "hy", "hye", "arm", "arménien"]
Languages["Herero"] = ["Herero", "hz", "her", "herero"]
Languages["Interlingua"] = ["Interlingua", "ia", "ina", "interlingua"]
Languages["Iban"] = ["Iban", "iba"]
Languages["Indonesian"] = ["Indonesian", "id", "ind", "indonésien"]
Languages["Interlingue"] = ["Interlingue", "ie", "ile", "interlingue"]
Languages["Occidental"] = ["Occidental", "ie", "ile"]
Languages["Igbo"] = ["Igbo", "ig", "ibo", "igbo"]
Languages["Nuosu"] = ["Nuosu", "ii", "iii"]
Languages["Sichuan Yi"] = ["Sichuan Yi", "ii", "iii", "yi de Sichuan"]
Languages["Ijo languages"] = ["Ijo languages", "ijo"]
Languages["Inupiaq"] = ["Inupiaq", "ik", "ipk", "inupiaq"]
Languages["Iloko"] = ["Iloko", "ilo"]
Languages["Indic languages"] = ["Indic languages", "inc"]
Languages["Indo-European languages"] = ["Indo-European languages", "ine"]
Languages["Ingush"] = ["Ingush", "inh"]
Languages["Ido"] = ["Ido", "io", "ido", "ido"]
Languages["Iranian languages"] = ["Iranian languages", "ira"]
Languages["Iroquoian languages"] = ["Iroquoian languages", "iro"]
Languages["Icelandic"] = ["Icelandic", "is", "isl", "ice", "islandais"]
Languages["Italian"] = ["Italian", "it", "ita", "italien"]
Languages["Inuktitut"] = ["Inuktitut", "iu", "iku", "inuktitut"]
Languages["Japanese"] = ["Japanese", "ja", "jpn", "japonais"]
Languages["Lojban"] = ["Lojban", "jbo"]
Languages["Judeo Persian"] = ["Judeo Persian", "jpr"]
Languages["Judeo Arabic"] = ["Judeo Arabic", "jrb"]
Languages["Javanese"] = ["Javanese", "jv", "jav", "javanais"]
Languages["Georgian"] = ["Georgian", "ka", "kat", "geo", "géorgien"]
Languages["Kara-Kalpak"] = ["Kara-Kalpak", "kaa"]
Languages["Kabyle"] = ["Kabyle", "kab"]
Languages["Jingpho"] = ["Jingpho", "kac"]
Languages["Kachin"] = ["Kachin", "kac"]
Languages["Kamba"] = ["Kamba", "kam"]
Languages["Karen languages"] = ["Karen languages", "kar"]
Languages["Galibi Carib"] = ["Galibi Carib", "karib", "galibi", "carib", "car"]
Languages["Kawi"] = ["Kawi", "kaw"]
Languages["Kabardian"] = ["Kabardian", "kbd"]
Languages["Kongo"] = ["Kongo", "kg", "kon", "kongo"]
Languages["Khasi"] = ["Khasi", "kha"]
Languages["Khoisan languages"] = ["Khoisan languages", "khi"]
Languages["Khotanese"] = ["Khotanese", "kho"]
Languages["Sakan"] = ["Sakan", "kho"]
Languages["Kikuyu"] = ["Kikuyu", "Gikuyu", "ki", "kik", "kikuyu"]
Languages["Kuanyama"] = ["Kuanyama", "Kwanyama", "kj", "kua", "kuanyama"]
Languages["Kazakh"] = ["Kazakh", "kk", "kaz", "kazakh"]
Languages["Greenlandic"] = ["Greenlandic", "kl", "kal", "groenlandais"]
Languages["Kalaallisut"] = ["Kalaallisut", "kl", "kal", "groenlandais"]
Languages["Central Khmer"] = ["Central Khmer", "km", "khm", "khmer central"]
Languages["Kimbundu"] = ["Kimbundu", "kmb"]
Languages["Kannada"] = ["Kannada", "kn", "kan", "kannada"]
Languages["Korean"] = ["Korean", "ko", "kor", "coréen"]
Languages["Konkani"] = ["Konkani", "kok"]
Languages["Kosraean"] = ["Kosraean", "kos"]
Languages["Kpelle"] = ["Kpelle", "kpe"]
Languages["Kanuri"] = ["Kanuri", "kr", "kau", "kanouri"]
Languages["Karachay-Balkar"] = ["Karachay-Balkar", "krc"]
Languages["Karelian"] = ["Karelian", "krl"]
Languages["Kru languages"] = ["Kru languages", "kro"]
Languages["Kurukh"] = ["Kurukh", "kru"]
Languages["Kashmiri"] = ["Kashmiri", "ks", "kas", "kashmiri"]
Languages["Kurdish"] = ["Kurdish", "ku", "kur", "kurde"]
Languages["Kumyk"] = ["Kumyk", "kum"]
Languages["Kutenai"] = ["Kutenai", "kut"]
Languages["Komi"] = ["Komi", "kv", "kom", "kom"]
Languages["Cornish"] = ["Cornish", "kw", "cor", "cornique"]
Languages["Kirghiz"] = ["Kirghiz", "Kyrgyz", "ky", "kir", "kirghiz"]
Languages["Latin"] = ["Latin", "la", "lat", "latin"]
Languages["Ladino"] = ["Ladino", "lad"]
Languages["Lahnda"] = ["Lahnda", "lah"]
Languages["Lamba"] = ["Lamba", "lam"]
Languages["Luxembourgish"] = ["Luxembourgish", "Letzeburgesch", "lb", "ltz", "luxembourgeois"]
Languages["Lezghian"] = ["Lezghian", "lez"]
Languages["Ganda"] = ["Ganda", "lg", "lug", "ganda"]
Languages["Limburgan"] = ["Limburgan", "Limburger", "Limburgish", "li", "lim", "limbourgeois"]
Languages["Lingala"] = ["Lingala", "ln", "lin", "lingala"]
Languages["Lao"] = ["Lao", "lo", "lao", "lao"]
Languages["Mongo"] = ["Mongo", "lol"]
Languages["Lozi"] = ["Lozi", "loz"]
Languages["Lithuanian"] = ["Lithuanian", "lt", "lit", "lituanien"]
Languages["Luba-Lulua"] = ["Luba-Lulua", "lua"]
Languages["Luba-Katanga"] = ["Luba", "Luba-Katanga", "lub", "lu", "luba", "luba-katanga"]
Languages["Luiseno"] = ["Luiseno", "lui"]
Languages["Lunda"] = ["Lunda", "lun"]
Languages["Luo"] = ["Luo", "luo"]
Languages["Lushai"] = ["Lushai", "lus"]
Languages["Latvian"] = ["Latvian", "lv", "lav", "letton"]
Languages["Madurese"] = ["Madurese", "mad"]
Languages["Magahi"] = ["Magahi", "mag"]
Languages["Maithili"] = ["Maithili", "mai"]
Languages["Makasar"] = ["Makasar", "mak"]
Languages["Mandingo"] = ["Mandingo", "man"]
Languages["Austronesian languages"] = ["Austronesian languages", "map"]
Languages["Masai"] = ["Masai", "mas"]
Languages["Moksha"] = ["Moksha", "mdf"]
Languages["Mandar"] = ["Mandar", "mdr"]
Languages["Mende"] = ["Mende", "men"]
Languages["Malagasy"] = ["Malagasy", "mg", "mlg", "malgache"]
Languages["Irish, Middle"] = ["Irish, Middle", "Irish, Middle (900-1200)", "mga"]
Languages["Marshallese"] = ["Marshallese", "mh", "mah", "marshall"]
Languages["Maori"] = ["Maori", "mi", "mri", "mao", "maori"]
Languages["Mi'kmaq"] = ["Mi'kmaq", "Micmac", "mic"]
Languages["Minangkabau"] = ["Minangkabau", "min"]
Languages["Uncoded languages"] = ["Uncoded languages", "mis"]
Languages["Macedonian"] = ["Macedonian", "mk", "mkd", "mac", "macédonien"]
Languages["Mon-Khmer languages"] = ["Mon-Khmer languages", "mkh"]
Languages["Malayalam"] = ["Malayalam", "ml", "mal", "malayalam"]
Languages["Mongolian"] = ["Mongolian", "mn", "mon", "mongol"]
Languages["Manchu"] = ["Manchu", "mnc"]
Languages["Manipuri"] = ["Manipuri", "mni"]
Languages["Manobo languages"] = ["Manobo languages", "mno"]
Languages["Mohawk"] = ["Mohawk", "moh"]
Languages["Mossi"] = ["Mossi", "mos"]
Languages["Marathi"] = ["Marathi", "mr", "mar", "marathe"]
Languages["Malay"] = ["Malay", "ms", "msa", "may", "malais"]
Languages["Maltese"] = ["Maltese", "mt", "mlt", "maltais"]
Languages["Multiple languages"] = ["Multiple languages", "mul"]
Languages["Munda languages"] = ["Munda languages", "mun"]
Languages["Creek"] = ["Creek", "mus"]
Languages["Mirandese"] = ["Mirandese", "mwl"]
Languages["Marwari"] = ["Marwari", "mwr"]
Languages["Burmese"] = ["Burmese", "my", "mya", "bur", "birman"]
Languages["Mayan languages"] = ["Mayan languages", "myn"]
Languages["Erzya"] = ["Erzya", "myv"]
Languages["Nauru"] = ["Nauru", "na", "nau", "nauruan"]
Languages["Nahuatl languages"] = ["Nahuatl languages", "nah"]
Languages["North American Indian languages"] = ["North American Indian languages", "nai"]
Languages["Neapolitan"] = ["Neapolitan", "nap"]
Languages["Norwegian Bokmål"] = ["Norwegian Bokmål", "nb", "nob", "norvégien bokmål"]
Languages["North Ndebele"] = ["North Ndebele", "Ndebele, North", "nd", "nde", "ndébélé du Nord"]
Languages["Low German"] = ["Low German", "German, Low", "nds"]
Languages["Low Saxon"] = ["Low Saxon", "Saxon, Low", "nds"]
Languages["Nepali"] = ["Nepali", "ne", "nep", "népalais"]
Languages["Nepal Bhasa"] = ["Nepal Bhasa", "new"]
Languages["Newari"] = ["Newari", "new"]
Languages["Ndonga"] = ["Ndonga", "ng", "ndo", "ndonga"]
Languages["Nias"] = ["Nias", "nia"]
Languages["Niger-Kordofanian languages"] = ["Niger-Kordofanian languages", "nic"]
Languages["Niuean"] = ["Niuean", "niué", "niu"]
Languages["Flemish"] = ["Flemish", "nl", "nld", "dut", "flamand"]
Languages["Norwegian Nynorsk"] = ["Norwegian Nynorsk", "Nynorsk, Norwegian", "nn", "nno", "norvégien nynorsk", "nynorsk, norvégien"]
Languages["Norwegian"] = ["Norwegian", "no", "nor", "norvégien"]
Languages["Nogai"] = ["Nogai", "nog"]
Languages["Old Norse"] = ["Old Norse", "Norse, Old", "non"]
Languages["N'Ko"] = ["N'Ko", "nqo"]
Languages["South Ndebele"] = ["South Ndebele", "Ndebele, South", "nr", "nbl", "ndébélé du Sud"]
Languages["Northern Sotho"] = ["Northern Sotho", "nso"]
Languages["Pedi"] = ["Pedi", "Sepedi", "nso"]
Languages["Nubian languages"] = ["Nubian languages", "nub"]
Languages["Navajo"] = ["Navajo", "Navaho", "nv", "nav", "navaho"]
Languages["Classical Nepal Bhasa"] = ["Classical Nepal Bhasa", "nwc"]
Languages["Classical Newari"] = ["Classical Newari", "nwc"]
Languages["Old Newari"] = ["Old Newari", "nwc"]
Languages["Chewa"] = ["Chewa", "ny", "nya", "chewa"]
Languages["Chichewa"] = ["Chichewa", "ny", "nya", "chichewa"]
Languages["Nyanja"] = ["Nyanja", "ny", "nya", "nyanja"]
Languages["Nyamwezi"] = ["Nyamwezi", "nym"]
Languages["Nyankole"] = ["Nyankole", "nyn"]
Languages["Nyoro"] = ["Nyoro", "nyo"]
Languages["Nzima"] = ["Nzima", "nzi"]
Languages["Occitan"] = ["Occitan", "Occitan (post 1500)", "oc", "oci", "occitan", "occitan (après 1500)"]
Languages["Ojibwa"] = ["Ojibwa", "oj", "oji", "ojibwa"]
Languages["Oromo"] = ["Oromo", "om", "orm", "galla"]
Languages["Oriya"] = ["Oriya", "or", "ori", "oriya"]
Languages["Ossetian"] = ["Ossetian", "Ossetic", "os", "oss", "ossète"]
Languages["Osage"] = ["Osage", "osa"]
Languages["Turkish, Ottoman"] = ["Turkish, Ottoman", "Turkish, Ottoman (1500-1928)", "ota"]
Languages["Otomian languages"] = ["Otomian languages", "oto"]
Languages["Panjabi"] = ["Panjabi", "Punjabi", "pa", "pan", "pendjabi"]
Languages["Papuan languages"] = ["Papuan languages", "paa"]
Languages["Pangasinan"] = ["Pangasinan", "pag"]
Languages["Pahlavi"] = ["Pahlavi", "pal"]
Languages["Kapampangan"] = ["Kapampangan", "pam"]
Languages["Pampanga"] = ["Pampanga", "pam"]
Languages["Papiamento"] = ["Papiamento", "pap"]
Languages["Palauan"] = ["Palauan", "pau"]
Languages["Persian, Old"] = ["Persian, Old", "Persian, Old (ca.600-400 B.C.)", "peo"]
Languages["Persian"] = ["Persian", "per", "fa", "fas", "persan"]
Languages["Philippine languages"] = ["Philippine languages", "phi"]
Languages["Phoenician"] = ["Phoenician", "phn"]
Languages["Pali"] = ["Pali", "pi", "pli", "pali"]
Languages["Polish"] = ["Polish", "pl", "pol", "polonais"]
Languages["Pohnpeian"] = ["Pohnpeian", "pon"]
Languages["Prakrit languages"] = ["Prakrit languages", "pra"]
Languages["Occitan, Old"] = ["Occitan, Old", "Occitan, Old (to 1500)", "pro"]
Languages["Provençal, Old"] = ["Provençal, Old", "Provençal, Old (to 1500)", "pro"]
Languages["Pushto"] = ["Pushto", "Pashto", "ps", "pus", "pachto"]
Languages["Portuguese"] = ["Portuguese", "pt", "por", "portugais"]
Languages["Reserved for local use"] = ["Reserved for local use", "qaa-qtz"]
Languages["Quechua"] = ["Quechua", "qu", "que", "quechua"]
Languages["Rajasthani"] = ["Rajasthani", "raj"]
Languages["Rapanui"] = ["Rapanui", "rap"]
Languages["Cook Islands Maori"] = ["Cook Islands Maori", "rar"]
Languages["Rarotongan"] = ["Rarotongan", "rar"]
Languages["Romansh"] = ["Romansh", "rm", "roh", "romanche"]
Languages["Rundi"] = ["Rundi", "rn", "run", "rundi"]
Languages["Moldavian"] = ["Moldavian", "Moldovan", "ro", "ron", "rum", "moldave"]
Languages["Romance languages"] = ["Romance languages", "roa"]
Languages["Romany"] = ["Romany", "rom"]
Languages["Russian"] = ["Russian", "ru", "rus", "russe"]
Languages["Romanian"] = ["Romanian", "rum", "ro", "ron", "roumain"]
Languages["Aromanian"] = ["Aromanian", "Arumanian", "rup"]
Languages["Macedo-Romanian"] = ["Macedo-Romanian", "rup"]
Languages["Kinyarwanda"] = ["Kinyarwanda", "rw", "kin", "rwanda"]
Languages["Sanskrit"] = ["Sanskrit", "sa", "san", "sanskrit"]
Languages["Sandawe"] = ["Sandawe", "sad"]
Languages["Yakut"] = ["Yakut", "sah"]
Languages["South American Indian languages"] = ["South American Indian languages", "sai"]
Languages["Salishan languages"] = ["Salishan languages", "sal"]
Languages["Samaritan Aramaic"] = ["Samaritan Aramaic", "sam"]
Languages["Sasak"] = ["Sasak", "sas"]
Languages["Santali"] = ["Santali", "sat"]
Languages["Sardinian"] = ["Sardinian", "sc", "srd", "sarde"]
Languages["Sicilian"] = ["Sicilian", "scn"]
Languages["Scots"] = ["Scots", "sco"]
Languages["Sindhi"] = ["Sindhi", "sd", "snd", "sindhi"]
Languages["Selkup"] = ["Selkup", "sel"]
Languages["Semitic languages"] = ["Semitic languages", "sem"]
Languages["Sango"] = ["Sango", "sg", "sag", "sango"]
Languages["Irish, Old"] = ["Irish, Old", "Irish, Old (to 900)", "sga"]
Languages["Sign languages"] = ["Sign languages", "sgn"]
Languages["Shan"] = ["Shan", "shn"]
Languages["Sinhala"] = ["Sinhala", "Sinhalese", "si", "sin", "singhalais"]
Languages["Sidamo"] = ["Sidamo", "sid"]
Languages["Siouan languages"] = ["Siouan languages", "sio"]
Languages["Sino-Tibetan languages"] = ["Sino-Tibetan languages", "sit"]
Languages["Slovak"] = ["Slovak", "sk", "slo", "slk", "slovaque"]
Languages["Slovenian"] = ["Slovenian", "sl", "slv", "slovène"]
Languages["Slavic languages"] = ["Slavic languages", "sla"]
Languages["Samoan"] = ["Samoan", "sm", "smo", "samoan"]
Languages["Southern Sami"] = ["Southern Sami", "sma"]
Languages["Northern Sami"] = ["Northern Sami", "sme", "se", "sami du Nord"]
Languages["Sami languages"] = ["Sami languages", "smi"]
Languages["Lule Sami"] = ["Lule Sami", "smj"]
Languages["Inari Sami"] = ["Inari Sami", "smn"]
Languages["Skolt Sami"] = ["Skolt Sami", "sms"]
Languages["Shona"] = ["Shona", "sn", "sna", "shona"]
Languages["Soninke"] = ["Soninke", "snk"]
Languages["Somali"] = ["Somali", "so", "som", "somali"]
Languages["Sogdian"] = ["Sogdian", "sog"]
Languages["Songhai languages"] = ["Songhai languages", "son"]
Languages["Albanian"] = ["Albanian", "sq", "sqi", "alb", "albanais"]
Languages["Serbian"] = ["Serbian", "sr", "srp", "serbe"]
Languages["Sranan Tongo"] = ["Sranan Tongo", "srn"]
Languages["Serer"] = ["Serer", "srr"]
Languages["Swati"] = ["Swati", "ss", "ssw", "swati"]
Languages["Nilo-Saharan languages"] = ["Nilo-Saharan languages", "ssa"]
Languages["Southern Sotho"] = ["Southern Sotho", "Sotho, Southern", "st", "sot", "sotho du Sud"]
Languages["Sundanese"] = ["Sundanese", "su", "sun", "soundanais"]
Languages["Sukuma"] = ["Sukuma", "suk"]
Languages["Susu"] = ["Susu", "sus"]
Languages["Sumerian"] = ["Sumerian", "sux"]
Languages["Swedish"] = ["Swedish", "sv", "swe", "suédois"]
Languages["Swahili"] = ["Swahili", "sw", "swa", "swahili"]
Languages["Classical Syriac"] = ["Classical Syriac", "syc"]
Languages["Syriac"] = ["Syriac", "syr"]
Languages["Tamil"] = ["Tamil", "ta", "tam", "tamoul"]
Languages["Tai languages"] = ["Tai languages", "tai"]
Languages["Telugu"] = ["Telugu", "te", "tel", "télougou"]
Languages["Timne"] = ["Timne", "tem"]
Languages["Tereno"] = ["Tereno", "ter"]
Languages["Tetum"] = ["Tetum", "tet"]
Languages["Tajik"] = ["Tajik", "tg", "tgk", "tadjik"]
Languages["Thai"] = ["Thai", "th", "tha", "thaï"]
Languages["Tigrinya"] = ["Tigrinya", "ti", "tir", "tigrigna"]
Languages["Tigre"] = ["Tigre", "tig"]
Languages["Tiv"] = ["Tiv", "tiv"]
Languages["Turkmen"] = ["Turkmen", "tk", "tuk", "turkmène"]
Languages["Tokelau"] = ["Tokelau", "tkl"]
Languages["Tagalog"] = ["Tagalog", "tl", "tgl", "tagalog"]
Languages["Klingon"] = ["Klingon", "tlh"]
Languages["tlhIngan-Hol"] = ["tlhIngan-Hol", "tlh"]
Languages["Tlingit"] = ["Tlingit", "tli"]
Languages["Tamashek"] = ["Tamashek", "tmh"]
Languages["Tswana"] = ["Tswana", "tn", "tsn", "tswana"]
Languages["Tonga (Nyasa)"] = ["Tonga (Nyasa)", "tog"]
Languages["Tonga (Tonga Islands)"] = ["Tonga (Tonga Islands)", "ton", "to", "tongan (Îles Tonga)"]
Languages["Tok Pisin"] = ["Tok Pisin", "tpi"]
Languages["Turkish"] = ["Turkish", "tr", "tur", "turc"]
Languages["Tsonga"] = ["Tsonga", "ts", "tso", "tsonga"]
Languages["Tsimshian"] = ["Tsimshian", "tsi"]
Languages["Tatar"] = ["Tatar", "tt", "tat", "tatar"]
Languages["Tumbuka"] = ["Tumbuka", "tum"]
Languages["Tupi languages"] = ["Tupi languages", "tup"]
Languages["Altaic languages"] = ["Altaic languages", "tut"]
Languages["Tuvalu"] = ["Tuvalu", "tvl"]
Languages["Twi"] = ["Twi", "tw", "twi"]
Languages["Tahitian"] = ["Tahitian", "ty", "tah", "tahitien"]
Languages["Tuvinian"] = ["Tuvinian", "tyv"]
Languages["Udmurt"] = ["Udmurt", "udm"]
Languages["Uighur"] = ["Uighur", "Uyghur", "ug", "uig", "ouïgour"]
Languages["Ugaritic"] = ["Ugaritic", "uga"]
Languages["Ukrainian"] = ["Ukrainian", "uk", "ukr", "ukrainien"]
Languages["Umbundu"] = ["Umbundu", "umb"]
Languages["Undetermined"] = ["Undetermined", "und"]
Languages["Urdu"] = ["Urdu", "ur", "urd", "ourdou"]
Languages["Uzbek"] = ["Uzbek", "uz", "uzb", "ouszbek"]
Languages["Vai"] = ["Vai", "vai"]
Languages["Venda"] = ["Venda", "ve", "ven", "venda"]
Languages["Vietnamese"] = ["Vietnamese", "vi", "vie", "vietnamien"]
Languages["Volapük"] = ["Volapük", "vo", "vol", "volapük"]
Languages["Votic"] = ["Votic", "vot"]
Languages["Walloon"] = ["Walloon", "wa", "wln", "wallon"]
Languages["Wakashan languages"] = ["Wakashan languages", "wak"]
Languages["Wolaitta"] = ["Wolaitta", "Wolaytta", "wal"]
Languages["Waray"] = ["Waray", "war"]
Languages["Washo"] = ["Washo", "was"]
Languages["Sorbian languages"] = ["Sorbian languages", "wen"]
Languages["Wolof"] = ["Wolof", "wo", "wol", "wolof"]
Languages["Kalmyk"] = ["Kalmyk", "xal"]
Languages["Oirat"] = ["Oirat", "xal"]
Languages["Xhosa"] = ["Xhosa", "xh", "xho", "xhosa"]
Languages["Yao"] = ["Yao", "yao"]
Languages["Yapese"] = ["Yapese", "yap"]
Languages["Yiddish"] = ["Yiddish", "yi", "yid", "yiddish"]
Languages["Yoruba"] = ["Yoruba", "yo", "yor", "yoruba"]
Languages["Yupik languages"] = ["Yupik languages", "ypk"]
Languages["Chuang"] = ["Chuang", "za", "zha", "chuang"]
Languages["Zhuang"] = ["Zhuang", "za", "zha", "zhuang"]
Languages["Zapotec"] = ["Zapotec", "zap"]
Languages["Blissymbols"] = ["Blissymbols", "Bliss", "Blissymbolics", "zbl"]
Languages["Zenaga"] = ["Zenaga", "zen"]
Languages["Standard Moroccan Tamazight"] = ["Standard Moroccan Tamazight", "zgh"]
Languages["Chinese"] = ["Chinese", "zh", "zho", "chi", "chinois"]
Languages["Zande languages"] = ["Zande languages", "znd"]
Languages["Zulu"] = ["Zulu", "zu", "zul", "zoulou"]
Languages["Zuni"] = ["Zuni", "zun"]
Languages["No linguistic content"] = ["No linguistic content", "zxx"]
Languages["Not applicable"] = ["Not applicable", "zxx"]
Languages["Dimili"] = ["Dimili", "Dimli", "zza"]
Languages["Kirdki"] = ["Kirdki", "zza"]
Languages["Kirmanjki"] = ["Kirmanjki", "zza"]
Languages["Zaza"] = ["Zaza", "Zazaki", "zza"]


# Start


def ChangeList(SourceList: list, TargetList: list):
    """
    Description:

        Changing a list

    Parameters:

        SourceList: the list to be changed
        TargetList: the list to change to
    """

    # Function Variables

    SourceListCellsAmount = len(SourceList)
    SourceListCell = None

    TargetListCellsAmount = len(TargetList)
    TargetListCell = None

    # Start

    while SourceListCellsAmount > 0:
        del SourceList[0]

        SourceListCellsAmount -= 1

    if TargetListCellsAmount > 0:
        for TargetListCell in TargetList:
            SourceListCell = TargetListCell

            SourceList.append(SourceListCell)


def Initialize():
    """
    Description:

        Initializing the "Languages" object
    """

    # Global Variables

    global Initialized

    # global Languages  # not changing its value

    # Function Variables

    SourceLists = None
    SourceList = None
    SourceListCellsAmount = None
    SourceListCell = None

    TargetList = None
    TargetListCell = None

    LanguagesItems = None
    LanguagesItem = None

    # Start

    if Initialized is False:
        SourceLists = []

        LanguagesItems = Languages.items()

        for LanguagesItem in LanguagesItems:
            SourceLists.append(LanguagesItem[1])

        for SourceList in SourceLists:
            SourceListCellsAmount = len(SourceList)

            if SourceListCellsAmount > 0:
                TargetList = []

                for SourceListCell in SourceList:
                    TargetListCell = (
                        (unidecode(SourceListCell).upper())
                        if isinstance(SourceListCell, str) is True
                        else SourceListCell
                    )

                    TargetList.append(TargetListCell)

                ChangeList(SourceList, TargetList)

        Initialized = True


def CheckLanguages(LanguageText: str) -> list:
    """
    Description:

        Checks the languages in the languages object based on the language text

    Parameters:

        LanguageText: the language text

    Returns:

        Returns the languages in the languages object if found suitable ones (a list of those, which are also lists)
        , otherwise returns None
    """

    # Global Variables

    # global Initialized  # not changing its value

    # global Languages  # not changing its value

    # Function Variables

    FixedLanguageTexts = None
    FixedLanguageText = None

    LanguagesItems = None
    LanguagesItem = None
    Language = None

    FunctionResult = None
    CurrentResult = None

    MethodFound = False

    # Start

    if Initialized is False:
        Initialize()

    if LanguageText is not None:
        FixedLanguageTexts = []

        FixedLanguageTexts.append(unidecode(LanguageText).upper())

        LanguagesItems = Languages.items()

        for LanguagesItem in LanguagesItems:
            for Language in LanguagesItem[1]:
                for FixedLanguageText in FixedLanguageTexts:
                    if FixedLanguageText == Language:
                        MethodFound = True

                        if CurrentResult is None:
                            CurrentResult = []

                        CurrentResult.append(LanguagesItem[1])

                        FixedLanguageTexts += LanguagesItem[1]

                        break

                if MethodFound is True:
                    MethodFound = False

                    break

    FunctionResult = CurrentResult

    return FunctionResult


def CompareLanguages(FirstLanguage: list, SecondLanguage: list) -> bool:
    """
    Description:

        Compares languages to see if they're the same (same language codes or names)

    Parameters:

        FirstLanguage: the first language (or languages) in the comparison
        SecondLanguage: the second language (or languages) in the comparison

    Returns:

        Returns True if the langauges are the same, False if they're not
    """

    # Function Variables

    FunctionResult = None

    FirstLanguageCell = None
    FirstLanguageCellCell = None
    SecondLanguageCell = None
    SecondLanguageCellCell = None

    MethodFound = False

    # Start

    if FirstLanguage == SecondLanguage:
        MethodFound = True
    else:
        for FirstLanguageCell in FirstLanguage:
            for SecondLanguageCell in SecondLanguage:
                if isinstance(FirstLanguageCell, list) is True:
                    for FirstLanguageCellCell in FirstLanguageCell:
                        if isinstance(SecondLanguageCell, list) is True:
                            for SecondLanguageCellCell in SecondLanguageCell:
                                if FirstLanguageCellCell == SecondLanguageCellCell:
                                    MethodFound = True

                                    break

                            if MethodFound is True:
                                break
                        else:
                            if FirstLanguageCellCell == SecondLanguageCell:
                                MethodFound = True

                                break

                    if MethodFound is True:
                        break
                else:
                    if isinstance(SecondLanguageCell, list) is True:
                        for SecondLanguageCellCell in SecondLanguageCell:
                            if FirstLanguageCell == SecondLanguageCellCell:
                                MethodFound = True

                                break

                        if MethodFound is True:
                            break
                    else:
                        if FirstLanguageCell == SecondLanguageCell:
                            MethodFound = True

                            break

            if MethodFound is True:
                break

    FunctionResult = MethodFound

    return FunctionResult

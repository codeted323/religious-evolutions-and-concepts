# Trait taxonomy: category -> subcategory -> traits
# Each trait: (code, name, description, scholarly origin note)
TAXONOMY = [
 ("DIV", "The divine & spirits", [
  ("How many gods?", [
   ("anim", "Animism", "Spirits live in animals, plants, places and natural forces.", "Probably the oldest layer of religion; inferred for Paleolithic hunter-gatherers and still central to many Indigenous traditions."),
   ("poly", "Polytheism", "Many gods with distinct roles and personalities.", "Typical of early cities and states (Sumer, Egypt, Vedic India, Greece), where gods were tied to cities, crafts and natural powers."),
   ("heno", "Chief god among many", "One god is supreme or worshipped exclusively, without denying that others exist (henotheism or monolatry).", "Seen in Marduk's rise in Babylon, early Israelite Yahweh worship and Hindu sects devoted to one deity."),
   ("mono", "Monotheism", "Only one God exists.", "Akhenaten's Aten cult (14th c. BCE) is the earliest attempt on record; it took lasting hold in Second Temple Judaism and passed to Christianity and Islam, with separate developments in Sikhism and elsewhere."),
   ("trin", "Plural persons in one God", "One God in several persons or aspects, such as the Christian Trinity.", "Defined for Christianity at Nicaea (325) and Constantinople (381); somewhat parallel triads appear in Hindu Trimurti thought and some Shia-derived groups."),
   ("mons", "Monism or pantheism", "All reality is ultimately one divine principle, or God and the universe are identical.", "Arises independently in the Upanishads (Brahman–Atman), Stoicism (Logos), Daoism and Neoplatonism (the One)."),
   ("nont", "Non-theistic", "No creator God is central. Gods may exist but are not the point, or are rejected outright.", "Early Buddhism, Jainism and Cārvāka (c. 6th–5th c. BCE) are the classic cases; modern secular humanism is another."),
  ]),
  ("Kinds of sacred beings", [
   ("sky", "Sky father or distant high god", "A supreme creator, often linked to the sky, who may be remote from daily life.", "Reconstructed for Proto-Indo-European religion (*Dyēus) and widespread in Africa, Siberia and the Americas."),
   ("fem", "Goddess or divine feminine", "Major female deities, a mother goddess, or a female aspect of the divine.", "Female figurines date back to the Upper Paleolithic, though what they meant is debated. Clear goddess cults appear in Sumer (Inanna), Egypt (Isis) and Hindu Shaktism."),
   ("ance", "Ancestor veneration", "The dead of the family or clan are honored, fed and consulted.", "Neolithic families buried their dead under house floors (Jericho, Çatalhöyük). Ancestor veneration is central in China, Africa and Oceania."),
   ("ang", "Angels or intermediary spirits", "Messengers or ranks of spirits between God and humans.", "Zoroastrian amesha spentas and yazatas likely shaped Second Temple Jewish angelology, which passed to Christianity and Islam."),
   ("devl", "A devil or cosmic adversary", "A chief evil being opposed to God.", "Angra Mainyu in Zoroastrianism is the earliest clear case; Satan becomes an adversary figure in Second Temple Judaism."),
   ("sain", "Saints and holy persons", "Holy people are venerated, often at shrines, and asked to intercede.", "Christian martyr cults (2nd c.), Sufi saints (walis), bodhisattvas and Jewish tzaddikim are parallel developments."),
  ]),
  ("Divinity in human form", [
   ("inc", "Divine incarnation", "God or a god takes human form (avatar, incarnation, living god).", "Pharaohs were identified with Horus. Hindu avatar doctrine and the Christian Incarnation developed separately, and later movements (Druze, Rastafari) added their own forms."),
   ("king", "Sacred kingship", "Rulers are divine, descended from gods, or rule by heavenly mandate.", "Universal in early states: Egypt, Mesopotamia, the Shang–Zhou Mandate of Heaven, the Inca, Hawaiʻi and imperial Japan."),
  ]),
 ]),
 ("COS", "Cosmos, creation & time", [
  ("Creation", [
   ("crwt", "Creation from primordial waters or chaos", "The world emerges from watery chaos or a formless void.", "Found in Egypt (Nun), Mesopotamia (Tiamat), Genesis 1, the Vedas and Polynesia; probably among the oldest shared cosmogonies."),
   ("crex", "Creation from nothing", "God creates the universe out of nothing (ex nihilo).", "Formalized in Jewish and Christian theology around the 2nd c. CE and adopted by Islam."),
   ("demi", "Flawed or lesser creator", "The material world was made by an ignorant or evil lesser god (a demiurge).", "Distinctive of 2nd-century Gnosticism and Marcion. It was carried on by Manichaeans, Paulicians, Bogomils and Cathars."),
  ]),
  ("Shape of time", [
   ("cycl", "Cyclical time", "The cosmos passes through repeating ages of creation and destruction.", "Hindu–Buddhist–Jain kalpas and yugas, Maya and Aztec world ages, and the Stoic world-conflagration."),
   ("lin", "Linear history toward an end", "Time runs once, from creation to a final goal.", "Usually traced to Zoroastrianism, then Judaism, Christianity and Islam."),
   ("apoc", "Apocalypse or end-times", "A coming final battle, judgment or transformation of the world.", "Zoroastrian frashokereti, Jewish apocalyptic writing (Daniel, c. 165 BCE), Norse Ragnarök and many modern millennial movements."),
   ("mess", "Coming savior or messiah", "A future redeemer figure will restore the world.", "Zoroastrian Saoshyant, the Jewish Messiah, the Islamic Mahdi, Buddhist Maitreya and Kalki in Hinduism."),
   ("fate", "Predestination or fate", "Everything, including salvation, is fixed in advance.", "Ājīvika niyati (5th c. BCE), Islamic qadar, Calvinist predestination."),
  ]),
  ("Order & conflict", [
   ("ordr", "Cosmic moral order", "An impersonal law or order underlies nature and ethics.", "Egyptian Ma'at, Vedic ṛta, Avestan aša, Greek Logos, Chinese Dao and Indian dharma."),
   ("dual", "Cosmic dualism", "The universe is a struggle between good and evil, or light and darkness.", "Zoroastrianism is the classic source; radical forms appear in Manichaeism, Gnosticism and Catharism."),
   ("axis", "World tree or cosmic axis", "A sacred tree, mountain or pillar links the heavens, earth and underworld.", "Norse Yggdrasil, the Maya ceiba, Mount Meru and the Siberian shamanic world tree."),
   ("flood", "Great flood myth", "A divine flood destroys most of humanity.", "The earliest texts are Mesopotamian (Ziusudra, Atrahasis, Gilgamesh). Flood stories also appear in Genesis, India (Manu), Greece and the Americas."),
  ]),
 ]),
 ("AFT", "Soul, death & afterlife", [
  ("What survives death?", [
   ("soul", "Immortal individual soul", "A lasting personal soul outlives the body.", "Egyptian ka/ba, Orphic and Platonic psyche, Indian ātman and Jain jīva."),
   ("anat", "No permanent self", "There is no unchanging self or soul (anattā).", "Distinctive Buddhist teaching (5th c. BCE)."),
   ("matr", "No afterlife (materialism)", "Death is the end of the person.", "Cārvāka in India and Epicureanism in Greece; modern secular humanism."),
  ]),
  ("Where the dead go", [
   ("undw", "Shadowy underworld", "All the dead go to a dim realm regardless of their deeds.", "Mesopotamian Kur, Hebrew Sheol, Greek Hades, Norse Hel."),
   ("judg", "Judgment of the dead", "Each person is judged after death on their deeds.", "The Egyptian weighing of the heart (by c. 2000 BCE) is the earliest clear case. Zoroastrianism has the Chinvat bridge."),
   ("hevh", "Heaven and hell", "Separate reward and punishment destinations.", "Zoroastrian, then Jewish apocalyptic, Christian and Islamic; also Buddhist and Hindu heavens and hells within rebirth."),
   ("resu", "Bodily resurrection", "The dead will rise in bodies at the end of time.", "Zoroastrianism and Second Temple Judaism (Daniel 12), then Christianity and Islam."),
  ]),
  ("Rebirth & release", [
   ("rein", "Rebirth or reincarnation", "The self or a stream of consciousness is reborn in new bodies.", "Arises in the Upanishads and Śramaṇa movements around the 8th–6th c. BCE, and separately in Orphism and Pythagoreanism; also in Druze, Yoruba and Igbo traditions."),
   ("karm", "Karma", "Actions bring morally matching results in this or future lives.", "First stated in the Upanishads (c. 7th–6th c. BCE); central to Buddhism, Jainism, Hinduism and Sikhism."),
   ("libr", "Liberation from rebirth", "The goal is escape from the cycle of rebirth (moksha, nirvana, mukti).", "Śramaṇa and Upanishadic India, c. 6th c. BCE."),
   ("grac", "Salvation by grace or faith", "Salvation comes as a gift through faith or devotion, not by merit.", "Pauline Christianity, Lutheran sola fide, Pure Land trust in Amitābha, and Vaishnava devotional surrender."),
  ]),
  ("Care of the dead", [
   ("grav", "Burial with grave goods", "The dead are buried with objects, food or companions for the next life.", "Among the oldest religious behavior: Middle Paleolithic burials with ochre (c. 100,000 years ago)."),
  ]),
 ]),
 ("ETH", "Ethics & morality", [
  ("Core moral rules", [
   ("core", "Core prohibitions", "A basic code against murder, theft, lying and sexual wrongdoing (Ten Commandments, Five Precepts, yamas).", "Nearly universal; early codified forms include Egyptian Book of the Dead 'negative confessions' and Mesopotamian law."),
   ("gold", "The Golden Rule", "Treat others as you want to be treated.", "Confucius (Analects 15.24), the Mahābhārata, Buddhist texts, Hillel, Jesus and Islamic hadith; it arose independently many times."),
   ("dcmd", "Morality as divine command", "Moral law is commanded by God and revealed.", "Israelite covenant law, later Christianity and Islam; compare Hammurabi's code given by Shamash."),
  ]),
  ("Love & non-harm", [
   ("comp", "Universal compassion", "Love and compassion are owed to all beings, even enemies.", "Buddhist mettā/karuṇā, Mohist impartial care, Jesus's love of enemies, the Mahāyāna bodhisattva vow."),
   ("ahim", "Non-violence to living beings", "Harming any living thing is wrong (ahiṃsā).", "Śramaṇa India: Jainism carries it to an extreme, and Buddhism and Hinduism share it."),
   ("paci", "Pacifism", "Refusal to take part in war or violence.", "Jainism, early Christianity (debated), Anabaptists, Quakers, Mohists on offensive war, Doukhobors."),
  ]),
  ("Duties to others", [
   ("char", "Obligatory charity", "Giving to the poor is a religious duty (zakat, tzedakah, dāna, langar).", "Widespread; formalized in Judaism, Islam, Buddhism and Sikhism."),
   ("hosp", "Sacred hospitality", "Guests and strangers are under divine protection.", "Reconstructed for Proto-Indo-European (Greek xenia); strong in Semitic and Bedouin ethics."),
   ("just", "Justice for the poor", "The faith demands justice for the poor, the widow and the oppressed.", "Israelite prophets (Amos, 8th c. BCE), Islam, Sikhism, Mazdakism and modern liberation movements."),
   ("fili", "Filial piety", "Duty and reverence toward parents and elders as a central virtue.", "Zhou and Confucian China; spread across East Asia."),
  ]),
  ("Character & purity", [
   ("virt", "Virtue cultivation", "Ethics as cultivating character and harmony rather than following rules.", "Confucian ren, Daoist wu wei, Stoic and Aristotelian virtue, Buddhist pāramitās."),
   ("pure", "Purity, pollution & taboo", "Ritual cleanliness, impurity and forbidden things (tapu, kapu, fady).", "Universal; elaborated in Hindu, Zoroastrian, Jewish, Shinto and Polynesian systems."),
   ("land", "Sacred land and kinship with nature", "Particular lands, waters and creatures are kin or holy.", "Central to Aboriginal Australian, Indigenous American and Māori religion; revived in modern Paganism."),
  ]),
 ]),
 ("RIT", "Ritual & practice", [
  ("Offering & sacrifice", [
   ("offr", "Offerings", "Food, drink, incense or goods given to gods, spirits or ancestors.", "Nearly universal from the Neolithic onward."),
   ("sacr", "Animal sacrifice", "Animals are killed as offerings.", "Ancient Near East, Vedic yajña, Greek and Roman religion; still practised in Islam (Eid al-Adha), by Samaritans, and in African and Afro-diasporic religions."),
   ("hsac", "Human sacrifice (historical)", "People were killed as offerings.", "Attested in Shang China, among the Aztec and Inca, in Hawaiʻi, in Kerma (Nubia) retainer burials, and elsewhere. Some claims, such as Carthaginian child sacrifice, remain debated."),
   ("fire", "Sacred fire", "Fire is a holy element, a divine presence or the vehicle of offerings.", "Proto-Indo-Iranian: Vedic Agni and the Zoroastrian fire temple; also Baltic and Roman (Vesta)."),
  ]),
  ("Prayer & contemplation", [
   ("pray", "Personal prayer", "Individuals speak directly to the divine.", "Nearly universal."),
   ("fpry", "Fixed daily prayer times", "Set prayers at prescribed hours (Zoroastrian gāhs, Jewish services, Islamic salat, Christian hours).", "Zoroastrian five gāhs are probably the earliest; Judaism, Islam, monastic Christianity and the Bahá'í Faith followed."),
   ("medi", "Meditation and contemplation", "Training the mind through stillness, concentration or contemplation.", "Śramaṇa and Upanishadic India (c. 6th c. BCE); separately in Daoism, Neoplatonism, Christian hesychasm and Sufi dhikr."),
   ("devo", "Loving devotion to a personal god", "Emotional surrender and love toward a deity (bhakti).", "Tamil bhakti saints (6th–9th c.), Sufism, Pure Land and Christian devotion."),
  ]),
  ("Altered states", [
   ("sham", "Shamanic trance", "A specialist journeys in trance to the spirit world to heal or guide.", "Inferred for the Upper Paleolithic; the word comes from Evenki (Siberia)."),
   ("poss", "Spirit possession or mediumship", "Gods or spirits speak through a human medium.", "West African and Afro-diasporic religions, Korean mudang, Chinese tangki, Spiritualism and Spiritism."),
   ("ente", "Sacred plants or drinks", "Mind-altering substances used as sacraments (soma, peyote, ayahuasca, cannabis, wine).", "Vedic soma and Avestan haoma; Chavín San Pedro cactus (c. 900 BCE); the Native American Church and Santo Daime."),
   ("danc", "Ecstatic music and dance", "Drumming, dance or song brings people into communion with the divine.", "San trance dance, Sufi samā', Pentecostal worship, Hasidic dancing, Vodou and Candomblé."),
  ]),
  ("Healing & divination", [
   ("heal", "Spiritual healing", "Healing through spiritual means is central.", "Shamanic healing, African diviner-healers, Pentecostal and Christian Science healing, Tenrikyō."),
   ("divn", "Divination and oracles", "Reading the will of gods or fate through signs, lots, oracles or omens.", "Shang oracle bones, Mesopotamian liver omens, Delphi, Yoruba Ifá, the Yijing."),
  ]),
  ("Sacred time & place", [
   ("fest", "Seasonal festivals", "A calendar of feasts tied to seasons, harvests and solstices.", "Neolithic and megalithic monuments aligned to solstices (Newgrange, Stonehenge)."),
   ("sabb", "Weekly or regular holy day", "A recurring sacred rest or gathering day (Sabbath, Sunday, Jumu'ah, uposatha).", "The Israelite Sabbath; parallels in the Buddhist uposatha."),
   ("pilg", "Pilgrimage", "Sacred journeys to holy places.", "Prehistoric gathering sites; later Delphi, Jerusalem, Mecca, Varanasi, Bodh Gaya, Santiago."),
   ("tmpl", "Temples and shrines", "Dedicated sacred buildings or sites.", "Göbekli Tepe (c. 9600 BCE) is among the earliest monumental ritual sites."),
  ]),
  ("Images", [
   ("icon", "Sacred images", "Statues, icons or images of the divine are venerated.", "Upper Paleolithic figurines; temple statues in Sumer and Egypt; Hindu mūrti, Christian icons, Buddha images."),
   ("anic", "Ban on images of God", "The divine must not be depicted (aniconism).", "Israelite religion, then Judaism and Islam; also Reformed Protestantism, Sikhism, and the Arabian and Nabataean stone cults."),
  ]),
  ("Membership rites", [
   ("init", "Initiation rites", "Rituals of entry or coming of age (baptism, upanayana, amrit, bar mitzvah).", "Probably Paleolithic; universal in some form."),
   ("wash", "Ritual washing or baptism", "Purifying water rites.", "Egypt, Indus (the Great Bath?), Jewish mikveh, Christian baptism, Islamic wuḍū', Shinto misogi, Mandaean masbuta."),
   ("meal", "Sacred meal", "A shared meal with sacred meaning (Eucharist, langar, Passover, Mithraic banquet).", "Neolithic feasting at Göbekli Tepe; Mithraic and Christian sacred meals."),
   ("myst", "Mystery initiation", "Secret rites reveal hidden truths to initiates.", "Eleusis (attested from c. 600 BCE), Mithraism, Isis, Tantra, Freemasonry, Wicca."),
  ]),
  ("Renunciation", [
   ("monk", "Monasticism", "Communities of monks or nuns living apart under a rule.", "Jain and Buddhist sanghas (5th c. BCE) are the earliest; Christian monasticism follows in 3rd–4th c. Egypt."),
   ("asce", "Asceticism", "Self-denial and austerity for spiritual ends.", "Śramaṇa India, Pythagoreans, Christian desert fathers, Sufis."),
   ("fast", "Ritual fasting", "Prescribed fasts (Yom Kippur, Lent, Ramadan, ekādaśī, Jain upavāsa).", "Widespread in the ancient Near East, India and the Americas."),
  ]),
 ]),
 ("LAW", "Rules for daily life", [
  ("Food & drink", [
   ("diet", "Dietary laws", "Forbidden and permitted foods (kashrut, halal, Ital, Jain diet).", "Israelite and Zoroastrian purity laws; Hindu, Jain, Islamic and Adventist codes."),
   ("vegt", "Vegetarianism", "Meat is avoided for religious reasons.", "Jain, Buddhist and Hindu ahiṃsā; Orphics and Pythagoreans; Manichaean elect, Cathars, Adventists."),
   ("alco", "Alcohol prohibited", "Intoxicants are forbidden.", "The Buddhist fifth precept, Islam, Bahá'í, Sikh Khalsa, Latter-day Saints, Methodist temperance."),
  ]),
  ("Body & dress", [
   ("dres", "Religious dress or hair rules", "Required head-coverings, garments or hair (kippah, hijab, turban, dreadlocks).", "Widespread; formalized in Judaism, Islam, Sikhism, Amish and Rastafari."),
   ("circ", "Circumcision", "Ritual male circumcision.", "Depicted in Egypt c. 2300 BCE; covenant sign in Israelite religion; customary in Islam and Ethiopian Christianity."),
   ("celi", "Celibate clergy or elite", "Priests, monks or an elect class must be celibate.", "Buddhist and Jain monastics, Manichaean elect, Latin Catholic priests (mandatory from 1139), Cathar perfecti, Shakers."),
  ]),
  ("Law codes & dues", [
   ("rlaw", "Comprehensive religious law", "A detailed legal system covering all of life (halakha, sharia, dharmaśāstra, canon law).", "Israelite and rabbinic Judaism, Islam, Hindu dharmaśāstra, Zoroastrian Vendidad, Catholic canon law."),
   ("tith", "Tithing", "A fixed share of income is given to the religion.", "Ancient Near East and Israelite tithe; Christian churches; Latter-day Saints (10%)."),
  ]),
 ]),
 ("AUT", "Authority, texts & community", [
  ("Sources of truth", [
   ("oral", "Oral transmission", "Sacred knowledge is passed down mainly by memory, song and story rather than a written canon.", "The original form of all religion; still primary in many Indigenous traditions."),
   ("scri", "Sacred scripture", "A body of written sacred texts or a canon.", "Sumerian temple hymns (c. 2500 BCE) and Egyptian Pyramid Texts (c. 2400 BCE) are the earliest religious writing."),
   ("revl", "New or ongoing revelation", "God continues to reveal truth through new prophets or living inspiration.", "Montanists, Manichaeans, Islam, the Latter-day Saints, Bahá'í, Quakers' inner light, Tenrikyō."),
   ("gnos", "Esoteric knowledge (gnosis)", "Salvation or truth comes through hidden, inner knowledge.", "Gnosticism, Hermeticism, Kabbalah, Ismaili bāṭin, Tantra, Theosophy."),
  ]),
  ("Founders & teachers", [
   ("foun", "Founder or prophet", "The tradition traces itself to a specific founder or prophet.", "Zoroaster, Mahāvīra and the Buddha are among the earliest; Jesus, Muhammad, Nanak and many modern founders follow."),
   ("guru", "Teacher lineages", "Authority passes through living masters (guru, shaykh, rebbe, roshi).", "Upanishadic teacher–student lineages; Sufi silsilas, Zen transmission, Hasidic dynasties."),
  ]),
  ("Religious specialists", [
   ("prie", "Priesthood", "A priestly class, often hereditary, performs the rites for others.", "From the first temple cities (Sumer, Egypt) and Vedic brahmins to Catholic and Orthodox priests and Zoroastrian mobeds."),
   ("hier", "Central hierarchy", "Organized ranks under a central head (pope, patriarch, Dalai Lama, Universal House of Justice).", "Roman Catholic papacy, Tibetan Buddhism, Latter-day Saints, Twelver marja'iyya."),
   ("cong", "Lay-led congregations", "Local communities run themselves, often without priests.", "Synagogues after 70 CE, Protestant congregationalism, Quakers, Sikh sangat, Bahá'í."),
  ]),
  ("Who belongs?", [
   ("ethn", "Ethnic or hereditary membership", "Belonging comes mainly by birth into a people or caste.", "Most ancient and Indigenous religions; Judaism, Druze, Yazidis, Parsis, Mandaeans."),
   ("univ", "Universal and open to all", "Anyone of any people can join.", "Buddhism (5th c. BCE) is the earliest universal missionary religion; mystery cults, Christianity and Islam followed."),
   ("miss", "Missionary outreach", "Actively seeks converts.", "Ashokan Buddhism (3rd c. BCE), Manichaeism, Christianity, Islam, Latter-day Saints."),
   ("sync", "Openly blends traditions", "Deliberately combines several religions.", "Hellenistic religions, Manichaeism, Afro-Atlantic religions, Caodaism, Theosophy, the New Age."),
  ]),
 ]),
]

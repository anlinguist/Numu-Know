import requests
import sys

doveobj = [
    {"words": [{"word": "Sumuga-duwa","morphemes": "sumu-ga-duwa", "gloss": "once-MOD-also"}, {"word": "soo","morphemes": "soo", "gloss": "NOM"}, {"word": "ehobe","morphemes": "ehobe", "gloss": "dove"}, {"word": "wahoo-ga","morphemes": "wahoo-ga", "gloss": "two.ACC-have"}, {"word": "tooamutse’e-gana","morphemes": "tooa-mu-tse’e-gana", "gloss": "child-PL-DIM-have"}, {"punctuation": "."}, {"punctuation": "”"}], "translation": "Once, there was a Dove who had two little children."},
{"words": [{"word": "Umudooga","morphemes": "umu-dooga", "gloss": "they-??"}, {"word": "tugamane","morphemes": "tuga-mane", "gloss": "eat-do"}, {"word": "meabodote","morphemes": "mea-bodote", "gloss": "go-round.trip"}, {"punctuation": "."}], "translation": "She often went out and returned with food for them"},
{"words": [{"word": "Yise","morphemes": "yise", "gloss": "then"}, {"word": "sumu","morphemes": "sumu", "gloss": "one"}, {"word": "tabeno-ga","morphemes": "tabeno-ga", "gloss": "day-MOD"}, {"punctuation": ","}, {"word": "tu","morphemes": "tu", "gloss": "own"}, {"word": "dooamu","morphemes": "dooamu", "gloss": "children"}, {"word": "tu","morphemes": "tu", "gloss": "own"}, {"word": "nobekwaesoo-ga","morphemes": "nobe-kwae-soo-ga", "gloss": "house-LOC-ADV-MOD"}, {"word": "mu","morphemes": "mu", "gloss": "3PL"}, {"word": "tamakwuse","morphemes": "tamakwu-se", "gloss": "leave-SEQ"}, {"word": "tukamea","morphemes": "tuka-mea", "gloss": "eat-go"}, {"punctuation": "."}], "translation": "Then one day, apparently, she left her children in her house to go get food."},
{"words": [{"word": "Yise-ga","morphemes": "yise-ga", "gloss": "then-MOD"}, {"word": "koo","morphemes": "koo", "gloss": "OBL"}, {"word": "ehobe","morphemes": "ehobe", "gloss": "dove"}, {"word": "mease","morphemes": "mea-se", "gloss": "go-SEQ"}, {"punctuation": ","}, {"word": "soo","morphemes": "soo", "gloss": "NOM"}, {"word": "mu","morphemes": "mu", "gloss": "3PL"}, {"word": "dooake’e","morphemes": "dooake’e", "gloss": "girls"}, {"word": "hi’e","morphemes": "hi’e", "gloss": "PAT.uncle"}, {"word": "ga","morphemes": "ga", "gloss": "?"}, {"word": "umuba","morphemes": "umu-ba", "gloss": "they-with"}, {"word": "petuse","morphemes": "petu-se", "gloss": "arrive-SEQ"}, {"word": "mu","morphemes": "mu", "gloss": "they"}, {"word": "tubenga","morphemes": "tubenga", "gloss": "ask"}, {"punctuation": ","}], "translation": "Then after the Dove left, the girls’ paternal uncle arrived to them and asked,"},
{"words": [{"punctuation": "“"}, {"word": "Hanosoo","morphemes": "hanosoo", "gloss": "where"}, {"word": "mu","morphemes": "mu", "gloss": "you.PL"}, {"word": "bea","morphemes": "bea", "gloss": "mother"}, {"word": "meapu","morphemes": "mea-pu", "gloss": "go-PFV"}, {"punctuation": ","}, {"punctuation": "”"}, {"word": "me’ega","morphemes": "me’e-ga", "gloss": "QTE-MOD"}, {"punctuation": "."}], "translation": "“Where did your mother go?”"},
{"words": [{"word": "Yise","morphemes": "yise", "gloss": "then"}, {"punctuation": ","}, {"punctuation": "“"}, {"word": "me","morphemes": "me", "gloss": "our.EXCL"}, {"word": "bea","morphemes": "bea", "gloss": "mother"}, {"word": "tugameapu","morphemes": "tuga-mea-pu", "gloss": "eat-go-PFV"}, {"punctuation": ","}, {"punctuation": "”"}, {"word": "me’e","morphemes": "me’e", "gloss": "QTE"}, {"word": "mu","morphemes": "mu", "gloss": "3PL"}, {"word": "tooake’e","morphemes": "tooake’e", "gloss": "girls"}, {"punctuation": "."}], "translation": "Then, “Our mother went to get food,” the girls said."},
{"words": [{"word": "Soo","morphemes": "soo", "gloss": "NOM"}, {"word": "hi’e","morphemes": "hi’e", "gloss": "PAT.uncle"}, {"word": "yise","morphemes": "yise", "gloss": "then"}, {"word": "mu","morphemes": "mu", "gloss": "them"}, {"word": "nekuseka","morphemes": "nekuseka", "gloss": "scold"}], "translation": "The paternal uncle scolded them,"},
{"words": [{"punctuation": "“"}, {"word": "Tuwaga-duwasoo","morphemes": "tuwaga-duwasoo", "gloss": "hole-also"}, {"word": "mu","morphemes": "mu", "gloss": "you.PL"}, {"word": "bea-ga","morphemes": "bea-ga", "gloss": "mother-MOD"}, {"word": "mu","morphemes": "mu", "gloss": "3PL"}, {"word": "tu","morphemes": "tu", "gloss": "own"}, {"word": "pubua’a","morphemes": "pu-bua’a", "gloss": "RE~friend"}, {"punctuation": ","}, {"punctuation": "”"}], "translation": "“Your mother goes to the hole/stock-pile(?) of her friends;”"},
{"words": [{"punctuation": "“"}, {"word": "hema","morphemes": "hema", "gloss": "what"}, {"word": "how","morphemes": "how", "gloss": "how"}, {"word": "tugwekwaetuga","morphemes": "tugwekwaetuga", "gloss": "?????????"}, {"word": "hane’yaina","morphemes": "hane-’yai-na", "gloss": "do-HAB-SIM"}, {"word": "mu","morphemes": "mu", "gloss": "2PL"}, {"word": "tukakute","morphemes": "tuka-kute", "gloss": "eat-APL"}, {"punctuation": ","}, {"punctuation": "”"}, {"word": "me’ega","morphemes": "me’e-ga", "gloss": "QTE-MOD"}, {"word": "yise","morphemes": "yise", "gloss": "then"}, {"word": "soo","morphemes": "soo", "gloss": "NOM"}, {"word": "mu","morphemes": "mu", "gloss": "3PL"}, {"word": "hi’e","morphemes": "hi’e", "gloss": "PAT.uncle"}, {"punctuation": "."}], "translation": "“that’s what she does to bring you food to eat,” their uncle said."},
{"words": [{"word": "Mu","morphemes": "mu", "gloss": "3PL"}, {"word": "netammase","morphemes": "netamma-se", "gloss": "tell-SEQ"}, {"punctuation": ","}, {"word": "umuba’yoo","morphemes": "umu-ba’yoo", "gloss": "they-from.with"}, {"word": "me","morphemes": "me", "gloss": "QTE"}, {"word": "mea","morphemes": "mea", "gloss": "go"}, {"punctuation": ","}, {"word": "yise","morphemes": "yise", "gloss": "then"}, {"word": "umu","morphemes": "umu", "gloss": "they"}, {"word": "tooake’e","morphemes": "tooake’e", "gloss": "girls"}, {"word": "suda","morphemes": "suda", "gloss": "bad"}, {"word": "nuumase","morphemes": "nuuma-se", "gloss": "feel-SEQ"}, {"word": "oe","morphemes": "oe", "gloss": "there"}, {"word": "kono’o","morphemes": "kono’o", "gloss": "stand.PL"}, {"punctuation": "."}], "translation": "After telling them, it’s said he went away from them, and then the girls were sad standing there."},
{"words": [{"word": "Yise","morphemes": "yise", "gloss": "then"}, {"word": "umu","morphemes": "umu", "gloss": "they"}, {"word": "tooake’e","morphemes": "tooake’e", "gloss": "girls"}, {"word": "pea","morphemes": "pea", "gloss": "mother"}, {"word": "yise","morphemes": "yise", "gloss": "then"}, {"word": "petu","morphemes": "petu", "gloss": "arrive"}, {"punctuation": ""}], "translation": "Then the girls’ mother arrived."},
{"words": [{"word": "Yise","morphemes": "yise", "gloss": "then"}, {"word": "umu","morphemes": "umu", "gloss": "they"}, {"word": "tooake’e","morphemes": "tooake’e", "gloss": "girls"}, {"word": "tu","morphemes": "tu", "gloss": "own"}, {"word": "pea","morphemes": "pea", "gloss": "mother"}, {"word": "tuukwe’e","morphemes": "tuukwe’e", "gloss": "tell"}], "translation": "Then the girls told their mother,"},
{"words": [{"punctuation": "“"}, {"word": "Me","morphemes": "me", "gloss": "our"}, {"word": "bea","morphemes": "bea", "gloss": "mother"}, {"word": "u","morphemes": "u", "gloss": "you"}, {"punctuation": ","}, {"word": "soo","morphemes": "soo", "gloss": "NOM"}, {"word": "me","morphemes": "me", "gloss": "our"}, {"word": "hi’e","morphemes": "hi’e", "gloss": "uncle"}, {"word": "nummeba","morphemes": "numme-ba", "gloss": "us-with"}, {"word": "petuse","morphemes": "petu-se", "gloss": "arrive-SEQ"}, {"punctuation": ","}, {"word": "me","morphemes": "me", "gloss": "us"}, {"word": "nekuseka","morphemes": "nekuseka", "gloss": "scold"}, {"punctuation": ","}, {"punctuation": "”"}, {"word": "me’e","morphemes": "me’e", "gloss": "QTE"}, {"word": "tu","morphemes": "tu", "gloss": "own"}, {"word": "pea","morphemes": "pea", "gloss": "mother"}, {"word": "tuukwe’e","morphemes": "tuukwe’e", "gloss": "tell"}, {"punctuation": "."}], "translation": "“Our mother! Our paternal uncle came and scolded us,” so they told their mother."},
{"words": [{"word": "Yise","morphemes": "yise", "gloss": "then"}, {"word": "soo","morphemes": "soo", "gloss": "NOM"}, {"word": "mu","morphemes": "mu", "gloss": "3PL"}, {"word": "bea","morphemes": "bea", "gloss": "mother"}, {"word": "suda","morphemes": "suda", "gloss": "bad"}, {"word": "nuumase","morphemes": "nuuma-se", "gloss": "feel-SEQ"}, {"punctuation": ","}], "translation": "Then their mother felt bad,"},
{"words": [{"word": "Yise","morphemes": "yise", "gloss": "then"}, {"word": "yagakooha","morphemes": "yaga-kooha", "gloss": "cry-begin"}, {"punctuation": ","}, {"word": "‘Hoowehoho","morphemes": "hoowehoho", "gloss": "hoowehoho"}, {"punctuation": ","}, {"word": "Hoowehoho","morphemes": "hoowehoho", "gloss": "hoowehoho"}, {"word": "ho","morphemes": "ho", "gloss": "ho"}, {"punctuation": ","}, {"punctuation": "”"}, {"word": "me’e","morphemes": "me’e", "gloss": "QTE"}, {"word": "yise","morphemes": "yise", "gloss": "then"}, {"punctuation": "."}], "translation": "And she began to cry, ‘Hoowehoho, Hoowehoho ho.”"}
]
obj = [
    {
        "words": [
            {
                "word": "Sumuga",
                "morphemes": "sumu-ga",
                "gloss": "once-NOM"
            },
            {
                "word": "duwa",
                "morphemes": "duwa",
                "gloss": "also"
            },
            {
                "word": "tunanugana",
                "morphemes": "tu-na-nuga-na",
                "gloss": "APS-MM-dance-SIM"
            },
            {
                "punctuation": ","
            },
            {
                "word": "soo",
                "morphemes": "soo",
                "gloss": "NOM"
            },
            {
                "word": "Edza’a",
                "morphemes": "edza’a",
                "gloss": "coyote"
            },
            {
                "word": "oe",
                "morphemes": "oe",
                "gloss": "there"
            },
            {
                "word": "petugase",
                "morphemes": "petu-ga-se",
                "gloss": "arrive-go-SEQ"
            }, 
            {
                "punctuation": "."
            }
        ],
        "translation": "Once during a dance, Coyote arrived there."
    },
    {
        "words": [
            {
                "word": "Yise",
                "morphemes": "yise",
                "gloss": "then"
            },
            {
                "word": "numu",
                "morphemes": "numu",
                "gloss": "people"
            },
            {
                "word": "(h)oonakwa",
                "morphemes": "hoonakwa",
                "gloss": "outside"
            },
            {
                "word": "peda-pukwae",
                "morphemes": "peda-pukwae",
                "gloss": "make.fire-place.where"
            },
            {
                "word": "numubaa",
                "morphemes": "numu-baa",
                "gloss": "people-with"
            },
            {
                "word": "katu",
                "morphemes": "katu",
                "gloss": "sit"
            }, 
            {
                "punctuation": "."
            }
        ],
        "translation": "Then he sat outside with people near the fire."
    },
    {
        "words": [
            {
                "word": "Yise",
                "morphemes": "yise",
                "gloss": "then"
            },
            {
                "word": "numuga",
                "morphemes": "numu-ga",
                "gloss": "people-MOD"
            },
            {
                "word": "o’o",
                "morphemes": "o’o",
                "gloss": "there"
            },
            {
                "word": "nakakatu",
                "morphemes": "naka-katu",
                "gloss": "hear-sit"
            }, 
            {
                "punctuation": "."
            }
        ],
        "translation": "He sat there listening with the people."
    },
    {
        "words": [
            {
                "word": "Yise",
                "morphemes": "yise",
                "gloss": "then"
            },
            {
                "word": "o’o",
                "morphemes": "o’o",
                "gloss": "there"
            },
            {
                "word": "katuse",
                "morphemes": "katu-se",
                "gloss": "sit-SEQ"
            },
            {
                "punctuation": ","
            },
            {
                "word": "mu",
                "morphemes": "mu",
                "gloss": "3PL"
            },
            {
                "word": "numu",
                "morphemes": "numu",
                "gloss": "people"
            },
            {
                "word": "tubenga",
                "morphemes": "tubenga",
                "gloss": "ask"
            },
            {
                "punctuation": ","
            }
        ],
        "translation": "After sitting there, he asked the people,"
    },
    {
        "words": [
            {"punctuation": "“"}, 
            {
                "word": "Hano",
                "morphemes": "hano",
                "gloss": "where"
            },
            {
                "word": "soo",
                "morphemes": "soo",
                "gloss": "NOM"
            },
            {
                "word": "Poenabe",
                "morphemes": "poenabe",
                "gloss": "chief"
            },
            {
                "word": "nobe",
                "morphemes": "nobe",
                "gloss": "house"
            },
            {
                "punctuation": ","
            },
            {
                "word": "nu",
                "morphemes": "nu",
                "gloss": "I"
            },
            {
                "word": "sakwa",
                "morphemes": "sakwa",
                "gloss": "MOD"
            },
            {
                "word": "oba",
                "morphemes": "oba",
                "gloss": "there"
            },
            {
                "word": "yooe-katuga",
                "morphemes": "yooe-katu-ga",
                "gloss": "warm-sit-go"
            },
            {
                "punctuation": "."
            },
            {
                "punctuation": "”"
            }
        ],
        "translation": "Where is the chief’s house so I can go sit and warm up there",
        "translation2": "Where is the chief’s house, I want to/should go sit & warm up there"
    },
    {
        "words": [
            {
                "word": "Yise",
                "morphemes": "yise",
                "gloss": "then"
            },
            {
                "word": "umu",
                "morphemes": "umu",
                "gloss": "they"
            },
            {"punctuation": "“"}, 
            {
                "word": "o’otema’a",
                "morphemes": "o’o-tema’a",
                "gloss": "there-EMPH"
            },
            {
                "word": "soo",
                "morphemes": "soo",
                "gloss": "NOM"
            },
            {
                "word": "Poenabe",
                "morphemes": "poenabe",
                "gloss": "chief"
            },
            {
                "word": "nobe",
                "morphemes": "nobe",
                "gloss": "house"
            },
            {
                "word": "oba",
                "morphemes": "oba",
                "gloss": "there"
            },
            {
                "word": "katuga”",
                "morphemes": "katu-ga",
                "gloss": "sit-MOD"
            },
            {
                "word": "me’e",
                "morphemes": "me’e",
                "gloss": "QTE"
            }, 
            {
                "punctuation": "."
            }
        ],
        "translation": "They said, “The Chief’s house is over there.”"
    },
    {
        "words": [
            {
                "word": "Yise",
                "morphemes": "yise",
                "gloss": "then"
            },
            {
                "word": "umu",
                "morphemes": "umu",
                "gloss": "they"
            },
            {
                "word": "tutubetso’ne",
                "morphemes": "tutubetso’ne",
                "gloss": "elder.woman"
            },
            {
                "word": "yise",
                "morphemes": "yise",
                "gloss": "then"
            },
            {
                "word": "umu",
                "morphemes": "umu",
                "gloss": "they"
            },
            {
                "word": "pebeawabe",
                "morphemes": "pe-beawabe",
                "gloss": "RE~old.woman"
            },
            {
                "punctuation": ","
            },
            {
                "word": "oma",
                "morphemes": "o-ma",
                "gloss": "3S-at"
            },
            {
                "word": "naneko’e",
                "morphemes": "naneko’e",
                "gloss": "laugh.PL"
            },
            {
                "word": "koo",
                "morphemes": "koo",
                "gloss": "OBL"
            },
            {
                "word": "edza’ama",
                "morphemes": "edza’a-ma",
                "gloss": "coyote-at"
            }, 
            {
                "punctuation": "."
            }
        ],
        "translation": "Then those elder women, those old women, teased/laughed at him, at Coyote."
    },
    {
        "words": [
            {
                "word": "Yise",
                "morphemes": "yise",
                "gloss": "then"
            },
            {
                "word": "soo",
                "morphemes": "soo",
                "gloss": "NOM"
            },
            {
                "word": "Edza’a",
                "morphemes": "edza’a",
                "gloss": "coyote"
            },
            {
                "word": "koo",
                "morphemes": "koo",
                "gloss": "OBL"
            },
            {
                "word": "Poenabeba",
                "morphemes": "poenabe-ba",
                "gloss": "chief-with"
            },
            {
                "word": "petugase",
                "morphemes": "petu-ga-se",
                "gloss": "arrive-go-SEQ"
            }, 
            {
                "punctuation": "."
            }
        ],
        "translation": "Then Coyote arrived to the chief."
    },
    {
        "words": [
            {
                "word": "Oo-no",
                "morphemes": "oo-no",
                "gloss": "3S-with"
            },
            {
                "word": "yadooagadunumme",
                "morphemes": "yadooa-gadu-numme",
                "gloss": "speak-talk-STAT"
            }, 
            {
                "punctuation": "."
            }
        ],
        "translation": "He sat and talked with him."
    },
    {
        "words": [
            {
                "word": "Yise",
                "morphemes": "yise",
                "gloss": "then"
            },
            {
                "word": "o",
                "morphemes": "o",
                "gloss": "3S"
            },
            {
                "word": "tubengagadunumme",
                "morphemes": "tubenga-gadu-numme",
                "gloss": "ask-sit-STAT"
            },
            {
                "punctuation": ","
            },
            {"punctuation": "“"}, 
            {
                "word": "How",
                "morphemes": "how",
                "gloss": "how"
            },
            {
                "word": "sakwa",
                "morphemes": "sakwa",
                "gloss": "MOD"
            },
            {
                "word": "nu",
                "morphemes": "nu",
                "gloss": "I"
            },
            {
                "word": "koo",
                "morphemes": "koo",
                "gloss": "OBL"
            },
            {
                "word": "hoobeadoona",
                "morphemes": "hoobea-doo-na",
                "gloss": "song-make-SIM"
            },
            {
                "punctuation": "."
            },
            {
                "punctuation": "”"
            }
        ],
        "translation": "Then sitting he asked him,“How about I make-song (sing)?”"
    },
    {
        "words": [
            {"punctuation": "“"}, 
            {
                "word": "Susumuna",
                "morphemes": "susumuna",
                "gloss": "sometimes"
            },
            {
                "word": "nu",
                "morphemes": "nu",
                "gloss": "I"
            },
            {
                "word": "hoobeadooyaetu",
                "morphemes": "hoobea-doo-yaetu",
                "gloss": "song-make-HAB"
            },
            {
                "word": "koo",
                "morphemes": "koo",
                "gloss": "OBL"
            },
            {
                "word": "numu",
                "morphemes": "numu",
                "gloss": "people"
            },
            {
                "word": "nuka",
                "morphemes": "nuka",
                "gloss": "dance"
            },
            {
                "punctuation": "."
            },
            {
                "punctuation": "”"
            }
        ],
        "translation": "“Sometimes I would sing for the people dance.”"
    },
    {
        "words": [
            {"punctuation": "“"}, 
            {
                "word": "How",
                "morphemes": "how",
                "gloss": "Q"
            },
            {
                "word": "oohoo”",
                "morphemes": "oohoo",
                "gloss": "like.that"
            },
            {
                "word": "me’e",
                "morphemes": "me’e",
                "gloss": "QTE"
            },
            {
                "word": "soo",
                "morphemes": "soo",
                "gloss": "NOM"
            },
            {
                "word": "Poenabe",
                "morphemes": "poenabe",
                "gloss": "chief"
            }, 
            {
                "punctuation": "."
            }
        ],
        "translation": "“Is that so,” said the Chief."
    },
    {
        "words": [
            {"punctuation": "“"}, 
            {
                "word": "Ta",
                "morphemes": "ta",
                "gloss": "we.DL"
            },
            {
                "word": "sakwa-nano",
                "morphemes": "sakwa-nano",
                "gloss": "MOD-both"
            },
            {
                "word": "numuba",
                "morphemes": "numu-ba",
                "gloss": "people-with"
            },
            {
                "word": "nuga",
                "morphemes": "nuga",
                "gloss": "dance"
            },
            {
                "punctuation": ","
            },
            {
                "punctuation": "”"
            },
            {
                "word": "me’e",
                "morphemes": "me’e",
                "gloss": "QTE"
            },
            {
                "word": "soo",
                "morphemes": "soo",
                "gloss": "NOM"
            },
            {
                "word": "Edza’a",
                "morphemes": "edza’a",
                "gloss": "coyote"
            }, 
            {
                "punctuation": "."
            }
        ],
        "translation": "“We should dance with the people,” Coyote said."
    },
    {
        "words": [
            {
                "word": "Yise",
                "morphemes": "yise",
                "gloss": "then"
            },
            {
                "word": "nano",
                "morphemes": "nano",
                "gloss": "both"
            },
            {
                "word": "nuka",
                "morphemes": "nuka",
                "gloss": "dance"
            }, 
            {
                "punctuation": "."
            }
        ],
        "translation": "Then both danced."
    },
    {
        "words": [
            {
                "word": "Soo",
                "morphemes": "soo",
                "gloss": "NOM"
            },
            {
                "word": "Edza’a",
                "morphemes": "edza’a",
                "gloss": "coyote"
            },
            {
                "word": "tunekwu’u",
                "morphemes": "tunekwu’u",
                "gloss": "sing"
            },
            {
                "punctuation": ","
            },
            {
                "word": "hoobea’too",
                "morphemes": "hoobea-too",
                "gloss": "song-make"
            }
        ],
        "translation": "Coyote sang and made-song:"
    },
    {
        "block": "Edzakee edzakee edzakee edzakee, Udookee udookee udookee udooke. Ubetsee ubetsee ubetse ubetse",
        "translation": ""
    },
    {
        "words": [
            {"punctuation": "“"}, 
            {
                "word": "How",
                "morphemes": "how",
                "gloss": "why"
            },
            {
                "word": "mu",
                "morphemes": "mu",
                "gloss": "you.PL"
            },
            {
                "word": "momoko’ne",
                "morphemes": "momoko’ne",
                "gloss": "RE~woman"
            },
            {
                "word": "ki",
                "morphemes": "ki",
                "gloss": "NEG"
            },
            {
                "word": "nummeba",
                "morphemes": "numme-ba",
                "gloss": "us.EXCL-with"
            },
            {
                "word": "nuka",
                "morphemes": "nuka",
                "gloss": "dance"
            },
            {
                "punctuation": "?"
            },
            {
                "punctuation": "”"
            }
        ],
        "translation": "“Why, you women, do you not dance with us?”"
    },
    {
        "words": [
            {"punctuation": "“"}, 
            {
                "word": "Yabe",
                "morphemes": "yabe",
                "gloss": "hurry"
            },
            {
                "word": "ya’a",
                "morphemes": "ya’a",
                "gloss": "here"
            },
            {
                "word": "nuga",
                "morphemes": "nuga",
                "gloss": "dance"
            },
            {
                "punctuation": ""
            },
            {
                "punctuation": "”"
            },
            {
                "word": "mee",
                "morphemes": "mee",
                "gloss": "QTE"
            },
            {
                "word": "too’e",
                "morphemes": "too’e",
                "gloss": "try"
            },
            {
                "word": "unnekayakwe",
                "morphemes": "unne-ka-yakwe",
                "gloss": "say-go-HAB"
            },
            {
                "punctuation": ","
            }
        ],
        "translation": "“Hurry and dance here,” he kept saying."
    },
    {
        "words": [
            {
                "word": "Ki",
                "morphemes": "ki",
                "gloss": "NEG"
            },
            {
                "word": "numu",
                "morphemes": "numu",
                "gloss": "person"
            },
            {
                "word": "nabedzape",
                "morphemes": "na-bedzape",
                "gloss": "MM-like"
            }, 
            {
                "punctuation": "."
            }
        ],
        "translation": "He was not a liked person."
    }
]

send = {
    'author': 'satchez',
    'data': obj
    }
    
requests.put("https://us-central1-numu-know.cloudfunctions.net/app/api/update/1", headers={"document":"Coyote at the Dance", "uid": "5SjMRYv3h0fjRYwSN8WfKALsOku2"}, json=send)
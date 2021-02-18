import requests
import sys

doveobj = [
    {"words": [{"word": "Sumuga-duwa","morphemes": "sumu-ga-duwa", "gloss": "once-MOD-also", "notes": "..."}, {"word": "soo","morphemes": "soo", "gloss": "NOM", "notes": "..."}, {"word": "ehobe","morphemes": "ehobe", "gloss": "dove", "notes": "..."}, {"word": "wahoo-ga","morphemes": "wahoo-ga", "gloss": "two.ACC-have", "notes": "..."}, {"word": "tooamutse’e-gana","morphemes": "tooa-mu-tse’e-gana", "gloss": "child-PL-DIM-have", "notes": "..."}, {"punctuation": "."}, {"punctuation": "”"}], "translation": "Once, there was a Dove who had two little children."},
{"words": [{"word": "Umudooga","morphemes": "umu-dooga", "gloss": "they-??", "notes": "..."}, {"word": "tugamane","morphemes": "tuga-mane", "gloss": "eat-do", "notes": "..."}, {"word": "meabodote","morphemes": "mea-bodote", "gloss": "go-round.trip", "notes": "..."}, {"punctuation": "."}], "translation": "She often went out and returned with food for them"},
{"words": [{"word": "Yise","morphemes": "yise", "gloss": "then", "notes": "..."}, {"word": "sumu","morphemes": "sumu", "gloss": "one", "notes": "..."}, {"word": "tabeno-ga","morphemes": "tabeno-ga", "gloss": "day-MOD", "notes": "..."}, {"punctuation": ","}, {"word": "tu","morphemes": "tu", "gloss": "own", "notes": "..."}, {"word": "dooamu","morphemes": "dooamu", "gloss": "children", "notes": "..."}, {"word": "tu","morphemes": "tu", "gloss": "own", "notes": "..."}, {"word": "nobekwaesoo-ga","morphemes": "nobe-kwae-soo-ga", "gloss": "house-LOC-ADV-MOD", "notes": "..."}, {"word": "mu","morphemes": "mu", "gloss": "3PL", "notes": "..."}, {"word": "tamakwuse","morphemes": "tamakwu-se", "gloss": "leave-SEQ", "notes": "..."}, {"word": "tukamea","morphemes": "tuka-mea", "gloss": "eat-go", "notes": "..."}, {"punctuation": "."}], "translation": "Then one day, apparently, she left her children in her house to go get food."},
{"words": [{"word": "Yise-ga","morphemes": "yise-ga", "gloss": "then-MOD", "notes": "..."}, {"word": "koo","morphemes": "koo", "gloss": "OBL", "notes": "..."}, {"word": "ehobe","morphemes": "ehobe", "gloss": "dove", "notes": "..."}, {"word": "mease","morphemes": "mea-se", "gloss": "go-SEQ", "notes": "..."}, {"punctuation": ","}, {"word": "soo","morphemes": "soo", "gloss": "NOM", "notes": "..."}, {"word": "mu","morphemes": "mu", "gloss": "3PL", "notes": "..."}, {"word": "dooake’e","morphemes": "dooake’e", "gloss": "girls", "notes": "..."}, {"word": "hi’e","morphemes": "hi’e", "gloss": "PAT.uncle", "notes": "..."}, {"word": "ga","morphemes": "ga", "gloss": "?", "notes": "..."}, {"word": "umuba","morphemes": "umu-ba", "gloss": "they-with", "notes": "..."}, {"word": "petuse","morphemes": "petu-se", "gloss": "arrive-SEQ", "notes": "..."}, {"word": "mu","morphemes": "mu", "gloss": "they", "notes": "..."}, {"word": "tubenga","morphemes": "tubenga", "gloss": "ask", "notes": "..."}, {"punctuation": ","}], "translation": "Then after the Dove left, the girls’ paternal uncle arrived to them and asked,"},
{"words": [{"punctuation": "“"}, {"word": "Hanosoo","morphemes": "hanosoo", "gloss": "where", "notes": "..."}, {"word": "mu","morphemes": "mu", "gloss": "you.PL", "notes": "..."}, {"word": "bea","morphemes": "bea", "gloss": "mother", "notes": "..."}, {"word": "meapu","morphemes": "mea-pu", "gloss": "go-PFV", "notes": "..."}, {"punctuation": ","}, {"punctuation": "”"}, {"word": "me’ega","morphemes": "me’e-ga", "gloss": "QTE-MOD", "notes": "..."}, {"punctuation": "."}], "translation": "“Where did your mother go?”"},
{"words": [{"word": "Yise","morphemes": "yise", "gloss": "then", "notes": "..."}, {"punctuation": ","}, {"punctuation": "“"}, {"word": "me","morphemes": "me", "gloss": "our.EXCL", "notes": "..."}, {"word": "bea","morphemes": "bea", "gloss": "mother", "notes": "..."}, {"word": "tugameapu","morphemes": "tuga-mea-pu", "gloss": "eat-go-PFV", "notes": "..."}, {"punctuation": ","}, {"punctuation": "”"}, {"word": "me’e","morphemes": "me’e", "gloss": "QTE", "notes": "..."}, {"word": "mu","morphemes": "mu", "gloss": "3PL", "notes": "..."}, {"word": "tooake’e","morphemes": "tooake’e", "gloss": "girls", "notes": "..."}, {"punctuation": "."}], "translation": "Then, “Our mother went to get food,” the girls said."},
{"words": [{"word": "Soo","morphemes": "soo", "gloss": "NOM", "notes": "..."}, {"word": "hi’e","morphemes": "hi’e", "gloss": "PAT.uncle", "notes": "..."}, {"word": "yise","morphemes": "yise", "gloss": "then", "notes": "..."}, {"word": "mu","morphemes": "mu", "gloss": "them", "notes": "..."}, {"word": "nekuseka","morphemes": "nekuseka", "gloss": "scold", "notes": "..."}], "translation": "The paternal uncle scolded them,"},
{"words": [{"punctuation": "“"}, {"word": "Tuwaga-duwasoo","morphemes": "tuwaga-duwasoo", "gloss": "hole-also", "notes": "..."}, {"word": "mu","morphemes": "mu", "gloss": "you.PL", "notes": "..."}, {"word": "bea-ga","morphemes": "bea-ga", "gloss": "mother-MOD", "notes": "..."}, {"word": "mu","morphemes": "mu", "gloss": "3PL", "notes": "..."}, {"word": "tu","morphemes": "tu", "gloss": "own", "notes": "..."}, {"word": "pubua’a","morphemes": "pu-bua’a", "gloss": "RE~friend", "notes": "..."}, {"punctuation": ","}, {"punctuation": "”"}], "translation": "“Your mother goes to the hole/stock-pile(?) of her friends;”"},
{"words": [{"punctuation": "“"}, {"word": "hema","morphemes": "hema", "gloss": "what", "notes": "..."}, {"word": "how","morphemes": "how", "gloss": "how", "notes": "..."}, {"word": "tugwekwaetuga","morphemes": "tugwekwaetuga", "gloss": "?????????", "notes": "..."}, {"word": "hane’yaina","morphemes": "hane-’yai-na", "gloss": "do-HAB-SIM", "notes": "..."}, {"word": "mu","morphemes": "mu", "gloss": "2PL", "notes": "..."}, {"word": "tukakute","morphemes": "tuka-kute", "gloss": "eat-APL", "notes": "..."}, {"punctuation": ","}, {"punctuation": "”"}, {"word": "me’ega","morphemes": "me’e-ga", "gloss": "QTE-MOD", "notes": "..."}, {"word": "yise","morphemes": "yise", "gloss": "then", "notes": "..."}, {"word": "soo","morphemes": "soo", "gloss": "NOM", "notes": "..."}, {"word": "mu","morphemes": "mu", "gloss": "3PL", "notes": "..."}, {"word": "hi’e","morphemes": "hi’e", "gloss": "PAT.uncle", "notes": "..."}, {"punctuation": "."}], "translation": "“that’s what she does to bring you food to eat,” their uncle said."},
{"words": [{"word": "Mu","morphemes": "mu", "gloss": "3PL", "notes": "..."}, {"word": "netammase","morphemes": "netamma-se", "gloss": "tell-SEQ", "notes": "..."}, {"punctuation": ","}, {"word": "umuba’yoo","morphemes": "umu-ba’yoo", "gloss": "they-from.with", "notes": "..."}, {"word": "me","morphemes": "me", "gloss": "QTE", "notes": "..."}, {"word": "mea","morphemes": "mea", "gloss": "go", "notes": "..."}, {"punctuation": ","}, {"word": "yise","morphemes": "yise", "gloss": "then", "notes": "..."}, {"word": "umu","morphemes": "umu", "gloss": "they", "notes": "..."}, {"word": "tooake’e","morphemes": "tooake’e", "gloss": "girls", "notes": "..."}, {"word": "suda","morphemes": "suda", "gloss": "bad", "notes": "..."}, {"word": "nuumase","morphemes": "nuuma-se", "gloss": "feel-SEQ", "notes": "..."}, {"word": "oe","morphemes": "oe", "gloss": "there", "notes": "..."}, {"word": "kono’o","morphemes": "kono’o", "gloss": "stand.PL", "notes": "..."}, {"punctuation": "."}], "translation": "After telling them, it’s said he went away from them, and then the girls were sad standing there."},
{"words": [{"word": "Yise","morphemes": "yise", "gloss": "then", "notes": "..."}, {"word": "umu","morphemes": "umu", "gloss": "they", "notes": "..."}, {"word": "tooake’e","morphemes": "tooake’e", "gloss": "girls", "notes": "..."}, {"word": "pea","morphemes": "pea", "gloss": "mother", "notes": "..."}, {"word": "yise","morphemes": "yise", "gloss": "then", "notes": "..."}, {"word": "petu","morphemes": "petu", "gloss": "arrive", "notes": "..."}, {"punctuation": ""}], "translation": "Then the girls’ mother arrived."},
{"words": [{"word": "Yise","morphemes": "yise", "gloss": "then", "notes": "..."}, {"word": "umu","morphemes": "umu", "gloss": "they", "notes": "..."}, {"word": "tooake’e","morphemes": "tooake’e", "gloss": "girls", "notes": "..."}, {"word": "tu","morphemes": "tu", "gloss": "own", "notes": "..."}, {"word": "pea","morphemes": "pea", "gloss": "mother", "notes": "..."}, {"word": "tuukwe’e","morphemes": "tuukwe’e", "gloss": "tell", "notes": "..."}], "translation": "Then the girls told their mother,"},
{"words": [{"punctuation": "“"}, {"word": "Me","morphemes": "me", "gloss": "our", "notes": "..."}, {"word": "bea","morphemes": "bea", "gloss": "mother", "notes": "..."}, {"word": "u","morphemes": "u", "gloss": "you", "notes": "..."}, {"punctuation": ","}, {"word": "soo","morphemes": "soo", "gloss": "NOM", "notes": "..."}, {"word": "me","morphemes": "me", "gloss": "our", "notes": "..."}, {"word": "hi’e","morphemes": "hi’e", "gloss": "uncle", "notes": "..."}, {"word": "nummeba","morphemes": "numme-ba", "gloss": "us-with", "notes": "..."}, {"word": "petuse","morphemes": "petu-se", "gloss": "arrive-SEQ", "notes": "..."}, {"punctuation": ","}, {"word": "me","morphemes": "me", "gloss": "us", "notes": "..."}, {"word": "nekuseka","morphemes": "nekuseka", "gloss": "scold", "notes": "..."}, {"punctuation": ","}, {"punctuation": "”"}, {"word": "me’e","morphemes": "me’e", "gloss": "QTE", "notes": "..."}, {"word": "tu","morphemes": "tu", "gloss": "own", "notes": "..."}, {"word": "pea","morphemes": "pea", "gloss": "mother", "notes": "..."}, {"word": "tuukwe’e","morphemes": "tuukwe’e", "gloss": "tell", "notes": "..."}, {"punctuation": "."}], "translation": "“Our mother! Our paternal uncle came and scolded us,” so they told their mother."},
{"words": [{"word": "Yise","morphemes": "yise", "gloss": "then", "notes": "..."}, {"word": "soo","morphemes": "soo", "gloss": "NOM", "notes": "..."}, {"word": "mu","morphemes": "mu", "gloss": "3PL", "notes": "..."}, {"word": "bea","morphemes": "bea", "gloss": "mother", "notes": "..."}, {"word": "suda","morphemes": "suda", "gloss": "bad", "notes": "..."}, {"word": "nuumase","morphemes": "nuuma-se", "gloss": "feel-SEQ", "notes": "..."}, {"punctuation": ","}], "translation": "Then their mother felt bad,"},
{"words": [{"word": "Yise","morphemes": "yise", "gloss": "then", "notes": "..."}, {"word": "yagakooha","morphemes": "yaga-kooha", "gloss": "cry-begin", "notes": "..."}, {"punctuation": ","}, {"word": "‘Hoowehoho","morphemes": "hoowehoho", "gloss": "hoowehoho", "notes": "..."}, {"punctuation": ","}, {"word": "Hoowehoho","morphemes": "hoowehoho", "gloss": "hoowehoho", "notes": "..."}, {"word": "ho","morphemes": "ho", "gloss": "ho", "notes": "..."}, {"punctuation": ","}, {"punctuation": "”"}, {"word": "me’e","morphemes": "me’e", "gloss": "QTE", "notes": "..."}, {"word": "yise","morphemes": "yise", "gloss": "then", "notes": "..."}, {"punctuation": "."}], "translation": "And she began to cry, ‘Hoowehoho, Hoowehoho ho.”"}
]
obj = [
    {
        "words": [
            {
                "word": "Sumuga",
                "morphemes": "sumu-ga",
                "gloss": "once-NOM",
"notes": "..."
            },
            {
                "word": "duwa",
                "morphemes": "duwa",
                "gloss": "also",
"notes": "..."
            },
            {
                "word": "tunanugana",
                "morphemes": "tu-na-nuga-na",
                "gloss": "APS-MM-dance-SIM",
"notes": "..."
            },
            {
                "punctuation": ","
            },
            {
                "word": "soo",
                "morphemes": "soo",
                "gloss": "NOM",
"notes": "..."
            },
            {
                "word": "Edza’a",
                "morphemes": "edza’a",
                "gloss": "coyote",
"notes": "..."
            },
            {
                "word": "oe",
                "morphemes": "oe",
                "gloss": "there",
"notes": "..."
            },
            {
                "word": "petugase",
                "morphemes": "petu-ga-se",
                "gloss": "arrive-go-SEQ",
"notes": "..."
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
                "gloss": "then",
"notes": "..."
            },
            {
                "word": "numu",
                "morphemes": "numu",
                "gloss": "people",
"notes": "..."
            },
            {
                "word": "(h)oonakwa",
                "morphemes": "hoonakwa",
                "gloss": "outside",
"notes": "..."
            },
            {
                "word": "peda-pukwae",
                "morphemes": "peda-pukwae",
                "gloss": "make.fire-place.where",
"notes": "..."
            },
            {
                "word": "numubaa",
                "morphemes": "numu-baa",
                "gloss": "people-with",
"notes": "..."
            },
            {
                "word": "katu",
                "morphemes": "katu",
                "gloss": "sit",
"notes": "..."
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
                "gloss": "then",
"notes": "..."
            },
            {
                "word": "numuga",
                "morphemes": "numu-ga",
                "gloss": "people-MOD",
"notes": "..."
            },
            {
                "word": "o’o",
                "morphemes": "o’o",
                "gloss": "there",
"notes": "..."
            },
            {
                "word": "nakakatu",
                "morphemes": "naka-katu",
                "gloss": "hear-sit",
"notes": "..."
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
                "gloss": "then",
"notes": "..."
            },
            {
                "word": "o’o",
                "morphemes": "o’o",
                "gloss": "there",
"notes": "..."
            },
            {
                "word": "katuse",
                "morphemes": "katu-se",
                "gloss": "sit-SEQ",
"notes": "..."
            },
            {
                "punctuation": ","
            },
            {
                "word": "mu",
                "morphemes": "mu",
                "gloss": "3PL",
"notes": "..."
            },
            {
                "word": "numu",
                "morphemes": "numu",
                "gloss": "people",
"notes": "..."
            },
            {
                "word": "tubenga",
                "morphemes": "tubenga",
                "gloss": "ask",
"notes": "..."
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
                "gloss": "where",
"notes": "..."
            },
            {
                "word": "soo",
                "morphemes": "soo",
                "gloss": "NOM",
"notes": "..."
            },
            {
                "word": "Poenabe",
                "morphemes": "poenabe",
                "gloss": "chief",
"notes": "..."
            },
            {
                "word": "nobe",
                "morphemes": "nobe",
                "gloss": "house",
"notes": "..."
            },
            {
                "punctuation": ","
            },
            {
                "word": "nu",
                "morphemes": "nu",
                "gloss": "I",
"notes": "..."
            },
            {
                "word": "sakwa",
                "morphemes": "sakwa",
                "gloss": "MOD",
"notes": "..."
            },
            {
                "word": "oba",
                "morphemes": "oba",
                "gloss": "there",
"notes": "..."
            },
            {
                "word": "yooe-katuga",
                "morphemes": "yooe-katu-ga",
                "gloss": "warm-sit-go",
"notes": "..."
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
                "gloss": "then",
"notes": "..."
            },
            {
                "word": "umu",
                "morphemes": "umu",
                "gloss": "they",
"notes": "..."
            },
            {"punctuation": "“"}, 
            {
                "word": "o’otema’a",
                "morphemes": "o’o-tema’a",
                "gloss": "there-EMPH",
"notes": "..."
            },
            {
                "word": "soo",
                "morphemes": "soo",
                "gloss": "NOM",
"notes": "..."
            },
            {
                "word": "Poenabe",
                "morphemes": "poenabe",
                "gloss": "chief",
"notes": "..."
            },
            {
                "word": "nobe",
                "morphemes": "nobe",
                "gloss": "house",
"notes": "..."
            },
            {
                "word": "oba",
                "morphemes": "oba",
                "gloss": "there",
"notes": "..."
            },
            {
                "word": "katuga”",
                "morphemes": "katu-ga",
                "gloss": "sit-MOD",
"notes": "..."
            },
            {
                "word": "me’e",
                "morphemes": "me’e",
                "gloss": "QTE",
"notes": "..."
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
                "gloss": "then",
"notes": "..."
            },
            {
                "word": "umu",
                "morphemes": "umu",
                "gloss": "they",
"notes": "..."
            },
            {
                "word": "tutubetso’ne",
                "morphemes": "tutubetso’ne",
                "gloss": "elder.woman",
"notes": "..."
            },
            {
                "word": "yise",
                "morphemes": "yise",
                "gloss": "then",
"notes": "..."
            },
            {
                "word": "umu",
                "morphemes": "umu",
                "gloss": "they",
"notes": "..."
            },
            {
                "word": "pebeawabe",
                "morphemes": "pe-beawabe",
                "gloss": "RE~old.woman",
"notes": "..."
            },
            {
                "punctuation": ","
            },
            {
                "word": "oma",
                "morphemes": "o-ma",
                "gloss": "3S-at",
"notes": "..."
            },
            {
                "word": "naneko’e",
                "morphemes": "naneko’e",
                "gloss": "laugh.PL",
"notes": "..."
            },
            {
                "word": "koo",
                "morphemes": "koo",
                "gloss": "OBL",
"notes": "..."
            },
            {
                "word": "edza’ama",
                "morphemes": "edza’a-ma",
                "gloss": "coyote-at",
"notes": "..."
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
                "gloss": "then",
"notes": "..."
            },
            {
                "word": "soo",
                "morphemes": "soo",
                "gloss": "NOM",
"notes": "..."
            },
            {
                "word": "Edza’a",
                "morphemes": "edza’a",
                "gloss": "coyote",
"notes": "..."
            },
            {
                "word": "koo",
                "morphemes": "koo",
                "gloss": "OBL",
"notes": "..."
            },
            {
                "word": "Poenabeba",
                "morphemes": "poenabe-ba",
                "gloss": "chief-with",
"notes": "..."
            },
            {
                "word": "petugase",
                "morphemes": "petu-ga-se",
                "gloss": "arrive-go-SEQ",
"notes": "..."
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
                "gloss": "3S-with",
"notes": "..."
            },
            {
                "word": "yadooagadunumme",
                "morphemes": "yadooa-gadu-numme",
                "gloss": "speak-talk-STAT",
"notes": "..."
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
                "gloss": "then",
"notes": "..."
            },
            {
                "word": "o",
                "morphemes": "o",
                "gloss": "3S",
"notes": "..."
            },
            {
                "word": "tubengagadunumme",
                "morphemes": "tubenga-gadu-numme",
                "gloss": "ask-sit-STAT",
"notes": "..."
            },
            {
                "punctuation": ","
            },
            {"punctuation": "“"}, 
            {
                "word": "How",
                "morphemes": "how",
                "gloss": "how",
"notes": "..."
            },
            {
                "word": "sakwa",
                "morphemes": "sakwa",
                "gloss": "MOD",
"notes": "..."
            },
            {
                "word": "nu",
                "morphemes": "nu",
                "gloss": "I",
"notes": "..."
            },
            {
                "word": "koo",
                "morphemes": "koo",
                "gloss": "OBL",
"notes": "..."
            },
            {
                "word": "hoobeadoona",
                "morphemes": "hoobea-doo-na",
                "gloss": "song-make-SIM",
"notes": "..."
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
                "gloss": "sometimes",
"notes": "..."
            },
            {
                "word": "nu",
                "morphemes": "nu",
                "gloss": "I",
"notes": "..."
            },
            {
                "word": "hoobeadooyaetu",
                "morphemes": "hoobea-doo-yaetu",
                "gloss": "song-make-HAB",
"notes": "..."
            },
            {
                "word": "koo",
                "morphemes": "koo",
                "gloss": "OBL",
"notes": "..."
            },
            {
                "word": "numu",
                "morphemes": "numu",
                "gloss": "people",
"notes": "..."
            },
            {
                "word": "nuka",
                "morphemes": "nuka",
                "gloss": "dance",
"notes": "..."
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
                "gloss": "Q",
"notes": "..."
            },
            {
                "word": "oohoo”",
                "morphemes": "oohoo",
                "gloss": "like.that",
"notes": "..."
            },
            {
                "word": "me’e",
                "morphemes": "me’e",
                "gloss": "QTE",
"notes": "..."
            },
            {
                "word": "soo",
                "morphemes": "soo",
                "gloss": "NOM",
"notes": "..."
            },
            {
                "word": "Poenabe",
                "morphemes": "poenabe",
                "gloss": "chief",
"notes": "..."
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
                "gloss": "we.DL",
"notes": "..."
            },
            {
                "word": "sakwa-nano",
                "morphemes": "sakwa-nano",
                "gloss": "MOD-both",
"notes": "..."
            },
            {
                "word": "numuba",
                "morphemes": "numu-ba",
                "gloss": "people-with",
"notes": "..."
            },
            {
                "word": "nuga",
                "morphemes": "nuga",
                "gloss": "dance",
"notes": "..."
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
                "gloss": "QTE",
"notes": "..."
            },
            {
                "word": "soo",
                "morphemes": "soo",
                "gloss": "NOM",
"notes": "..."
            },
            {
                "word": "Edza’a",
                "morphemes": "edza’a",
                "gloss": "coyote",
"notes": "..."
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
                "gloss": "then",
"notes": "..."
            },
            {
                "word": "nano",
                "morphemes": "nano",
                "gloss": "both",
"notes": "..."
            },
            {
                "word": "nuka",
                "morphemes": "nuka",
                "gloss": "dance",
"notes": "..."
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
                "gloss": "NOM",
"notes": "..."
            },
            {
                "word": "Edza’a",
                "morphemes": "edza’a",
                "gloss": "coyote",
"notes": "..."
            },
            {
                "word": "tunekwu’u",
                "morphemes": "tunekwu’u",
                "gloss": "sing",
"notes": "..."
            },
            {
                "punctuation": ","
            },
            {
                "word": "hoobea’too",
                "morphemes": "hoobea-too",
                "gloss": "song-make",
"notes": "..."
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
                "gloss": "why",
"notes": "..."
            },
            {
                "word": "mu",
                "morphemes": "mu",
                "gloss": "you.PL",
"notes": "..."
            },
            {
                "word": "momoko’ne",
                "morphemes": "momoko’ne",
                "gloss": "RE~woman",
"notes": "..."
            },
            {
                "word": "ki",
                "morphemes": "ki",
                "gloss": "NEG",
"notes": "..."
            },
            {
                "word": "nummeba",
                "morphemes": "numme-ba",
                "gloss": "us.EXCL-with",
"notes": "..."
            },
            {
                "word": "nuka",
                "morphemes": "nuka",
                "gloss": "dance",
"notes": "..."
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
                "gloss": "hurry",
"notes": "..."
            },
            {
                "word": "ya’a",
                "morphemes": "ya’a",
                "gloss": "here",
"notes": "..."
            },
            {
                "word": "nuga",
                "morphemes": "nuga",
                "gloss": "dance",
"notes": "..."
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
                "gloss": "QTE",
"notes": "..."
            },
            {
                "word": "too’e",
                "morphemes": "too’e",
                "gloss": "try",
"notes": "..."
            },
            {
                "word": "unnekayakwe",
                "morphemes": "unne-ka-yakwe",
                "gloss": "say-go-HAB",
"notes": "..."
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
                "gloss": "NEG",
"notes": "..."
            },
            {
                "word": "numu",
                "morphemes": "numu",
                "gloss": "person",
"notes": "..."
            },
            {
                "word": "nabedzape",
                "morphemes": "na-bedzape",
                "gloss": "MM-like",
"notes": "..."
            }, 
            {
                "punctuation": "."
            }
        ],
        "translation": "He was not a liked person."
    }
]


add = [
    "Sümüga-düwa su ihobi wahu-ga tuamütsi’i-gana",
    "Ümüduga tügamani miabodoti",
    "Yeiši šümü tabino-ga tü duamü tü nobikweišu-ga mü tamakwusi tukamia",
    "Yeiši-ga ku ihobi miasi šu mü tuaki’i hai’i ga ümüma pitüsi mü tübinga",
    "Hanosu mü bia miapü mi’iga",
    "Yeiši mi bia tügamiapü mi’i mü duaki’i",
    "Su hai’i yeiši mü niküsika",
    "Tüwaga-düwasu mü bia-ga mü tü pübüa’a",
    "hima hau tügwikweitüga hani’yaina mü tükaküti mi’iga yeiši šu mü hai’i",
    "Mü nitammasi ümüba’yu mi mia yeiši ümü tuaki’i šüda nüümasi oi kono’o",
    "Yeiši ümü tuaki’i pia yeiši pitü",
    "Yeiši ümü tuaki’i tü pia tüüki’i",
    "Mi bia ü su mi hai’i nümmiba pitüsi mi niküsika mi’i tü pia tüükwi’i",
    "Yeiši su mü pia süda nüümasi",
    "Yeiši yagakooha Huwihoho Huwihoho ho mi’i yeiši"
]
sentNumber = -1
for item in add:
    wordNumber=-1
    sentNumber += 1
    sentence = doveobj[sentNumber]["words"]
    words = item.split()
    for sword in words:
        wordNumber += 1
        match = False
        while not match:
            try:
                sentence[wordNumber]["word"]
                sentence[wordNumber]["variant-ortho"] = sword
                match = True
            except IndexError:
                match = True
            except:
                wordNumber += 1
                match = False

send = {
    'author': 'satchez',
    'data': doveobj
    }
    
requests.put("https://us-central1-numu-know.cloudfunctions.net/app/api/update/1", headers={"document":"Dove Story", "uid": "5SjMRYv3h0fjRYwSN8WfKALsOku2"}, json=send)
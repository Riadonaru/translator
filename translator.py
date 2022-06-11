import os
import subprocess
import pyperclip


class TwoWayDict(dict):


    def __len__(self):
        return super().__len__(self) / 2


    def mkTwoWay(self):
        items = tuple(self.items())
        for pair in items:
            self[pair[1]] = pair[0]

two_way_dict = TwoWayDict({
    "q": "/",
    "w": "'",
    "e": "ק",
    "r": "ר",
    "t": "א",
    "y": "ט",
    "u": "ו",
    "i": "ן",
    "o": "ם",
    "p": "פ",
    "[": "{",
    "]": "}",
    "\\": "|",
    "a": "ש",
    "s": "ד",
    "d": "ג",
    "f": "כ",
    "g": "ע",
    "h": "י",
    "j": "ח",
    "k": "ל",
    "l": "ך",
    ";": "ף",
    "'": ",",
    "z": "ז",
    "x": "ס",
    "c": "ב",
    "v": "ה",
    "b": "נ",
    "n": "מ",
    "m": "צ",
    ",": "ת",
    ".": "ץ",
    "/": "."
})

two_way_dict.mkTwoWay()
result = ""
data = pyperclip.paste().lower()
for char in data:
    try:
        result += two_way_dict[char]
    except:
        result += char
pyperclip.copy(result)

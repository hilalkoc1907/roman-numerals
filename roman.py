import re

VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

PATTERN = re.compile(
    r"M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})"
)

PAIRS = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
         (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
         (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]


def convert(s):
    """Roma rakamını (1-4999) tam sayıya çevirir. Geçersizse ValueError fırlatır."""
    if not isinstance(s, str) or not s or not PATTERN.fullmatch(s):
        raise ValueError(f"Geçersiz Roma rakamı: {s}")
    total = 0
    for i, c in enumerate(s):
        value = VALUES[c]
        if i + 1 < len(s) and value < VALUES[s[i + 1]]:
            total -= value
        else:
            total += value
    return total


def to_roman(n):
    """1-4999 arası tam sayıyı Roma rakamına çevirir. Geçersizse ValueError fırlatır."""
    if not isinstance(n, int) or isinstance(n, bool) or not 1 <= n <= 4999:
        raise ValueError("Sayı 1 ile 4999 arasında bir tam sayı olmalı")
    out = ""
    for value, symbol in PAIRS:
        while n >= value:
            out += symbol
            n -= value
    return out


if __name__ == "__main__":
    while True:
        s = input("Roma rakamı (çıkmak için q): ").strip().upper()
        if s == "Q":
            break
        try:
            print(f"{s} = {convert(s)}")
        except ValueError as e:
            print(e)
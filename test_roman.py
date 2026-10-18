import pytest
from roman import convert, to_roman


def test_tek_haneli():
    assert convert("I") == 1
    assert convert("V") == 5
    assert convert("X") == 10
    assert convert("L") == 50
    assert convert("C") == 100
    assert convert("D") == 500
    assert convert("M") == 1000


def test_toplamali():
    assert convert("II") == 2
    assert convert("III") == 3
    assert convert("VI") == 6
    assert convert("XII") == 12
    assert convert("LX") == 60


def test_cikarmali():
    assert convert("IV") == 4
    assert convert("IX") == 9
    assert convert("XL") == 40
    assert convert("XC") == 90


def test_karisik():
    assert convert("XIV") == 14
    assert convert("XIX") == 19
    assert convert("MCMXCIV") == 1994
    assert convert("MMXXIV") == 2024
    assert convert("MMMMCMXCIX") == 4999


def test_gecersiz_karakter():
    for bad in ["A", "B", "E", "F", "G", "H", ""]:
        with pytest.raises(ValueError):
            convert(bad)


def test_gecersiz_tekrar():
    for bad in ["IIII", "VIIII", "VV", "LL", "DD", "XXXX", "CCCC", "MMMMM"]:
        with pytest.raises(ValueError):
            convert(bad)


def test_gecersiz_cikarma():
    for bad in ["IC", "IL", "VX", "IIX", "XM", "VIX"]:
        with pytest.raises(ValueError):
            convert(bad)


def test_hepsi_1_den_4999a():
    for n in range(1, 5000):
        assert convert(to_roman(n)) == n


def test_to_roman_ornekler():
    assert to_roman(1) == "I"
    assert to_roman(4) == "IV"
    assert to_roman(1994) == "MCMXCIV"
    assert to_roman(4999) == "MMMMCMXCIX"


def test_to_roman_gecersiz():
    for bad in [0, -5, 5000, 10000, 3.5, "abc"]:
        with pytest.raises(ValueError):
            to_roman(bad)
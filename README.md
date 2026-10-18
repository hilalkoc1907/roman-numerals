# Roma Rakamı Çevirici (Roman Numerals Kata)

Roma rakamlarını standart sayı rakamlarına (ve tersine) çeviren bir program.
1 - 4999 arası tüm sayıları destekler, geçersiz girdilerde hata mesajı verir.
Komut satırı (CLI) ve tarayıcıda çalışan bir web arayüzü içerir.

## Özellikler

- Roma rakamı → sayı (`MCMXCIV` → 1994)
- Sayı → Roma rakamı (`2024` → `MMXXIV`)
- Tek haneli, toplamalı (`VII`), çıkarmalı (`IX`) ve karışık (`MCMXCIV`) sayılar
- Yanlış girdilerin tespiti (`IIII`, `VIIII`, `IC`, `VV`, `A`, boş girdi...)
- Küçük harf girdisi kabul edilir (`iv` → 4)
- Sonucu panoya kopyalama butonu
- Eskitme (parşömen) temalı arayüz

## Kurulum

Python 3.9 veya üstü gerekir.

```
pip install -r requirements.txt
```

## Kullanım

Web arayüzü:

```
python app.py
```

Tarayıcıda `http://127.0.0.1:5000` adresini aç.

Komut satırı:

```
python roman.py
```

Roma rakamını yaz, çıkmak için `q` yaz.

## Testler

```
pytest
```

- Tek haneli, toplamalı, çıkarmalı ve karışık sayılar
- Geçersiz karakter, geçersiz tekrar ve geçersiz çıkarma girdileri
- 1'den 4999'a kadar her sayının gidiş-dönüş testi
- Web API uç noktaları

## API

| Uç nokta | Örnek | Başarılı cevap |
|---|---|---|
| `GET /api/convert?roman=...` | `/api/convert?roman=MCMXCIV` | `{"roman": "MCMXCIV", "value": 1994}` |
| `GET /api/to_roman?number=...` | `/api/to_roman?number=1994` | `{"number": 1994, "roman": "MCMXCIV"}` |

Geçersiz girdide HTTP 400 ve `{"error": "..."}` döner.

## Nasıl çalışıyor?

Geçerlilik kontrolü bir düzenli ifade (regex) ile yapılır. Sayı binler, yüzler,
onlar ve birler basamağına ayrılır ve her basamak kendi kuralına uymak zorundadır.
Geçerli girdilerde harfler soldan sağa okunur: bir harf sağındaki harften küçükse
çıkarılır, değilse eklenir.

## Geliştirme yöntemi

Proje TDD (Test Driven Development) ile geliştirildi: her özellik için önce
başarısız test (Red), sonra testi geçen kod (Green) yazıldı.
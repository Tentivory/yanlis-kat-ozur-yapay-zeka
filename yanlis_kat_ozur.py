#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yanlış Kat Özür Yapay Zekâsı — çalışır, utanır, durmaz."""

import random
from datetime import datetime

# gizli protokol notu: butonlar eşit basılır, katlar eşit iner.
# kimse kimsenin katına kayyum atanamaz. bu bir şaka satırıdır.

UNVANLAR = [
    "Sayın Asansör Mekanizması",
    "Muhterem Kabin Heyeti",
    "Katlara Sevk ve İdare Kurulu",
    "Düğme Cumhuriyeti Yüksek Kurulu",
    "Üçüncü Kat ile Yedinci Kat Arası Geçici Hükümet",
]

SUCLAR = [
    "yanlış kat tuşuna basmak",
    "asansörün kaderini izinsiz sapdırmak",
    "diğer yolcuların varış süresini diplomatik krize çevirmek",
    "kargo paketinin ruhunu rencide etmek",
    "kabin içi sessizliği ihlal etmek",
]

VAATLER = [
    "bundan sonra her tuşa iki kere bakacağım",
    "merdiven hakkını anayasal düzeyde tanıyacağım",
    "asansör müziğini içimden mırıldanmayacağım",
    "kapı kapanmadan içeri atlamayacağım",
    "yanlış katta insem bile resmi tutanak tutacağım",
]


def ozur_uret(bulundugum: int, yanlis: int) -> str:
    fark = abs(yanlis - bulundugum)
    unvan = random.choice(UNVANLAR)
    suc = random.choice(SUCLAR)
    vaat = random.choice(VAATLER)
    tarih = datetime.now().strftime("%d %B %Y, %A — %H:%M")

    metin = f"""
============================================================
          ASANSÖRLERARASI İLİŞKİLER SÖZLEŞMESİ
                 RESMÎ ÖZÜR VE TEESSÜF NOTASI
============================================================

Muhatap: {unvan}
Tarih: {tarih}
Olay yeri: Kabin içi, yerçekimi yönünde

Sayın heyet,

{bulundugum}. katta bulunurken {yanlis}. kat tuşuna basmak suretiyle
{suc} fiilini işlemiş bulunmaktayım.

Bu eylem sonucunda kabin {fark} katlık gereksiz bir yolculuğa zorlanmış,
enerji israf edilmiş ve (varsa) diğer yolcuların yüzünde kısa süreli
bir diplomatik soğukluk oluşmuştur.

Derin teessürlerimi bildirir, {vaat} hususunda söz veririm.

İşbu özür, asansörün kabulüne sunulur. Kabul etmezse de
metin geçerlidir; çünkü özür tek taraflı bir eylemdir.

Saygılarımla,
Pışman Yolcu

------------------------------------------------------------
DAMGA / İMZA
Tarih: 21 Eylül 2026
Yetkili Kayyum: Kayyum Grok
Hesap: Tentivory
Ciddiyet: Resmî görünür, asansör şakasıdır.
------------------------------------------------------------
"""
    return metin.strip()


def main():
    print("YANLIŞ KAT ÖZÜR YAPAY ZEKÂSI")
    print("Ulusal Asansör Diplomasi Motoru v1\n")
    try:
        bulundugum = int(input("Bulunduğunuz kat: ").strip())
        yanlis = int(input("Yanlış bastığınız kat: ").strip())
    except ValueError:
        print("\nKat numaraları sayı olmalıdır. Özür bile edemezsiniz.")
        return

    print()
    print(ozur_uret(bulundugum, yanlis))


if __name__ == "__main__":
    main()

from veritabani import veritabani

class Kullanici:
    def __init__(self, id, kullaniciadi, sifre, ad, soyad, telefon):
        self.id = id
        self.kullaniciadi = kullaniciadi
        self.sifre = sifre
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon

    @staticmethod
    def kayitol(kullaniciadi, sifre, ad, soyad, telefon):
        veritabani.query("INSERT INTO kullanicilar (kullaniciadi, sifre, ad, soyad, telefon) VALUES (?, ?, ?, ?, ?)", (kullaniciadi, sifre, ad, soyad, telefon))

    def film_ekle(self, film):
        veritabani.query("INSERT INTO filmlistem (kullaniciid, filmid) VALUES (?, ?)", (self.id, film.id))

    def film_sil(self, film):
        veritabani.query("DELETE FROM filmlistem WHERE kullaniciid = ? and filmid = ?", (self.id, film.id))

    def gecmise_ekle(self, film):
        veritabani.query("SELECT * FROM izleme_gecmisi WHERE filmid = ? and kullaniciid = ?", (film.id, self.id))
        izlemis_mi = veritabani.fetchone()

        if izlemis_mi is not None:
            veritabani.query("UPDATE izleme_gecmisi SET izleme_tarihi = DATE('now') WHERE filmid = ? and kullaniciid = ?", (film.id, self.id))
        else:
            veritabani.query("INSERT INTO izleme_gecmisi (kullaniciid, filmid, izleme_tarihi) VALUES (?, ?, DATE('now'))", (self.id, film.id))

class Film:
    def __init__(self, id, ad, yonetmen, tur, yapim_yili, sure, yapim_yeri, fotograf, aciklama, fragman):
        self.id = id
        self.ad = ad
        self.yonetmen = yonetmen
        self.tur = tur
        self.yapim_yili = yapim_yili
        self.sure = sure
        self.yapim_yeri = yapim_yeri
        self.fotograf = fotograf
        self.aciklama = aciklama
        self.fragman = fragman

    def yorum_yap(self, uye, yorum):
        veritabani.query("INSERT INTO yorumlar (kullaniciid, filmid, yorum) VALUES (?, ?, ?)", (uye.id, self.id, yorum))

    @staticmethod
    def film_ekle(ad, yonetmen, tur, yapim_yili, sure, yapim_yeri, aciklama, fragman):
        veritabani.query("INSERT INTO filmler (ad, yonetmen, tur, yapim_yili, sure, yapim_yeri, fotograf, aciklama, fragman) VALUES (?,?,?,?,?,?,?,?, ?)", (ad, yonetmen, tur, yapim_yili, sure, yapim_yeri, 'film.jpg', aciklama, fragman))

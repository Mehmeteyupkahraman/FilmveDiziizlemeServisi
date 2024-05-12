from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore
from ana_ui import Ui_MainWindow
from veritabani import veritabani
from film import Film
from izlemelistesi import FilmListemSayfa
from izlemegecmisi import IzlemeGecmisiSayfa
from PyQt5 import QtGui
from izle import IzlemeSayfa
from filmekle import FilmEkleSayfa

class AnaSayfa(QMainWindow):
    def __init__(self, uye) -> None:
        super().__init__()
        self.anasayfa = Ui_MainWindow()
        self.anasayfa.setupUi(self)
        self.index = 0
        self.uye = uye

        self.anasayfa.sonrakiButon.clicked.connect(self.sonraki_film)
        self.anasayfa.oncekiButon.clicked.connect(self.onceki_film)
        self.film_liste_guncelle()
        self.film_guncelle()

        izleme_listesi = FilmListemSayfa(uye)
        self.anasayfa.action_zleme_Listem.triggered.connect(lambda: izleme_listesi.goster())
        self.anasayfa.listeEkleButon.clicked.connect(self.liste_ekle_buton)

        izleme_gecmisi = IzlemeGecmisiSayfa(uye)
        self.anasayfa.action_zleme_Ge_mi_im.triggered.connect(lambda: izleme_gecmisi.goster())

        izlesayfa = IzlemeSayfa(uye)
        self.anasayfa.izleButon.clicked.connect(lambda: izlesayfa.goster(self.filmler[self.index]))

        filmeklesayfa = FilmEkleSayfa()
        self.anasayfa.filmEkle.triggered.connect(lambda: filmeklesayfa.show())
        filmeklesayfa.film_ekle_sinyal.connect(self.film_liste_guncelle)


    def sonraki_film(self):
        self.index += 1
        if len(self.filmler) == self.index:
            self.index = 0
        self.film_guncelle()

    def onceki_film(self):
        self.index -= 1
        if self.index == -1:
            self.index = len(self.filmler) - 1
        self.film_guncelle()

    def film_guncelle(self):
        film = self.filmler[self.index]
        self.anasayfa.foto.setPixmap(QtGui.QPixmap("fotoğraflar/" + film.fotograf))
        self.anasayfa.aciklama.setText(film.aciklama)
        self.anasayfa.filmadi.setText(film.ad)
        self.anasayfa.filmyonetmeni.setText("Film Yönetmeni: " + film.yonetmen)
        self.anasayfa.konusu.setText(film.ad + " Film Konusu:")
        self.anasayfa.filmturu.setText("Film Türü: " + film.tur)
        self.anasayfa.yapimyili.setText("Yapım Yılı: " + str(film.yapim_yili))
        self.anasayfa.suresi.setText("Süresi: " + str(film.sure) + " dakika")
        self.anasayfa.yapimyeri.setText("Yapım Yeri: " + film.yapim_yeri)

        veritabani.query("SELECT * FROM filmlistem WHERE kullaniciid = ? and filmid = ?", (self.uye.id, film.id))
        listede_mi = veritabani.fetchone()

        if listede_mi is None:
            self.anasayfa.listeEkleButon.setText("Listeme Ekle")
        else:
            self.anasayfa.listeEkleButon.setText("Listemden Çıkar")

    def film_liste_guncelle(self):
        veritabani.query('SELECT * FROM filmler')
        sql = veritabani.fetchall()
        filmler = []
        for kayit in sql:
            filmler.append(Film(*kayit))
        self.filmler = filmler

    def liste_ekle_buton(self):
        film = self.filmler[self.index]
        yanit = QMessageBox.warning(self, "Liste", "İşlemi onaylıyor musunuz?", QMessageBox.Yes, QMessageBox.No)
        if yanit == QMessageBox.No:
            return

        buton_yazisi = self.anasayfa.listeEkleButon.text()

        if buton_yazisi == "Listeme Ekle":
            self.uye.film_ekle(film)
            self.anasayfa.listeEkleButon.setText("Listemden Çıkar")
        else:
            self.uye.film_sil(film)
            self.anasayfa.listeEkleButon.setText("Listeme Ekle")

        QMessageBox.information(self, "Liste", "İşlem tamamlandı.", QMessageBox.Ok)

    def film_izle(self):
        film = self.filmler[self.index]
        self.film_izle_sayfasi.goster(film)
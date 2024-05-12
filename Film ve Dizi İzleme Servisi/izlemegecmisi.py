from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from izlemegecmisi_ui import Ui_Form
from PyQt5 import QtCore
from veritabani import veritabani
from film import Film
from datetime import datetime

class IzlemeGecmisiSayfa(QWidget):
    def __init__(self, kullanici) -> None:
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.kullanici = kullanici

    def goster(self):
        tablo = self.ui.izlemegecmisi
        tablo.setRowCount(0)
        veritabani.query('SELECT filmid, izleme_tarihi FROM izleme_gecmisi WHERE kullaniciid = ?', (self.kullanici.id,))
        izlemeler_sql = veritabani.fetchall()
        self.show()

        if izlemeler_sql is None:
            return

        tablo.setRowCount(len(izlemeler_sql))
        satir = 0
        tablo.setColumnWidth(0, 80)
        tablo.setColumnWidth(1, 140)
        tablo.setColumnWidth(2, 140)
        tablo.setColumnWidth(3, 100)
        tablo.setColumnWidth(4, 70)
        tablo.setColumnWidth(5, 80)
        tablo.setColumnWidth(6, 70)

        for film_id, izleme_tarihi in izlemeler_sql:
            veritabani.query("SELECT * FROM filmler WHERE id = ?", (film_id,))
            film_sql = veritabani.fetchone()
            film = Film(*film_sql)

            izleme_tarihi_cell = QTableWidgetItem(str(datetime.strptime(izleme_tarihi, "%Y-%m-%d").strftime("%d.%m.%Y")))
            film_ad_cell = QTableWidgetItem(film.ad)
            film_yonetmen_cell = QTableWidgetItem(film.yonetmen)
            film_tur_cell = QTableWidgetItem(film.tur)
            film_yapim_cell = QTableWidgetItem(str(film.yapim_yili))
            film_sure_cell = QTableWidgetItem(f"{film.sure} dakika")
            film_yapimyer_cell = QTableWidgetItem(film.yapim_yeri)
            # Hepsinin yazısını ortala
            film_ad_cell.setTextAlignment(QtCore.Qt.AlignCenter)
            izleme_tarihi_cell.setTextAlignment(QtCore.Qt.AlignCenter)
            film_yonetmen_cell.setTextAlignment(QtCore.Qt.AlignCenter)
            film_tur_cell.setTextAlignment(QtCore.Qt.AlignCenter)
            film_yapim_cell.setTextAlignment(QtCore.Qt.AlignCenter)
            film_sure_cell.setTextAlignment(QtCore.Qt.AlignCenter)
            film_yapimyer_cell.setTextAlignment(QtCore.Qt.AlignCenter)

            tablo.setItem(satir, 0, izleme_tarihi_cell)
            tablo.setItem(satir, 1, film_ad_cell)
            tablo.setItem(satir, 2, film_yonetmen_cell)
            tablo.setItem(satir, 3, film_tur_cell)
            tablo.setItem(satir, 4, film_yapim_cell)
            tablo.setItem(satir, 5, film_sure_cell)
            tablo.setItem(satir, 6, film_yapimyer_cell)
            satir += 1
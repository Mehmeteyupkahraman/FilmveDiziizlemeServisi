from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QApplication
from PyQt5 import QtCore
from veritabani import veritabani
from izlemelistesi_ui import Ui_izlemelistem
from film import Film

class FilmListemSayfa(QWidget):
    def __init__(self, kullanici) -> None:
        super().__init__()
        self.kullanici = kullanici
        self.ui = Ui_izlemelistem()  # Eğer UI dosyanızdaki sınıfın adı farklı ise uygun şekilde değiştirin
        self.ui.setupUi(self)

    def goster(self):
        tablo = self.ui.tablo
        tablo.setRowCount(0)
        veritabani.query('SELECT kullaniciid, filmid FROM filmlistem WHERE kullaniciid = ?', (self.kullanici.id,))
        filmlersql = veritabani.fetchall()
        self.show()

        if filmlersql is None:
            return

        tablo.setRowCount(len(filmlersql))
        satir = 0
        tablo.setColumnWidth(0, 140)
        tablo.setColumnWidth(1, 140)
        tablo.setColumnWidth(2, 100)
        tablo.setColumnWidth(3, 70)
        tablo.setColumnWidth(4, 70)
        tablo.setColumnWidth(5, 70)

        for kullaniciid, filmid in filmlersql:
            veritabani.query("SELECT * FROM filmler WHERE id = ?", (filmid,))
            filmsql = veritabani.fetchone()
            film = Film(*filmsql)

            filmcell = QTableWidgetItem(film.ad)
            filmyonetmenicell = QTableWidgetItem(film.yonetmen)
            filmturucell = QTableWidgetItem(film.tur)
            yapimyilicell = QTableWidgetItem(str(film.yapim_yili))
            suresicell = QTableWidgetItem(str(film.sure) + " dakika")
            yapimyericell = QTableWidgetItem(film.yapim_yeri)

            # Hepsinin yazısını ortala
            filmcell.setTextAlignment(QtCore.Qt.AlignCenter)
            filmyonetmenicell.setTextAlignment(QtCore.Qt.AlignCenter)
            filmturucell.setTextAlignment(QtCore.Qt.AlignCenter)
            yapimyilicell.setTextAlignment(QtCore.Qt.AlignCenter)
            suresicell.setTextAlignment(QtCore.Qt.AlignCenter)
            yapimyericell.setTextAlignment(QtCore.Qt.AlignCenter)

            tablo.setItem(satir, 0, filmcell)
            tablo.setItem(satir, 1, filmyonetmenicell)
            tablo.setItem(satir, 2, filmturucell)
            tablo.setItem(satir, 3, yapimyilicell)
            tablo.setItem(satir, 4, suresicell)
            tablo.setItem(satir, 5, yapimyericell)
            satir += 1
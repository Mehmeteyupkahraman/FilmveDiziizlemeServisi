from PyQt5.QtWidgets import QWidget, QMessageBox
from filmekle_ui import Ui_Form
from film import Film
from PyQt5.QtCore import pyqtSignal
import re

class FilmEkleSayfa(QWidget):
    film_ekle_sinyal = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        self.form = Ui_Form()
        self.form.setupUi(self)
        self.form.ekleButon.clicked.connect(self.filmekle)

    def filmekle(self):
        ad = self.form.adLine.text()
        yonetmen = self.form.yonetmenLine.text()
        tur = self.form.turLine.text()
        yapim_yili = self.form.yilBox.value()
        sure = self.form.sureBox.value()
        yapim_yeri = self.form.yerLine.text()
        fragmanlink = self.form.youtubeLine.text()
        konu = self.form.aciklamaText.toPlainText()

        if not all([ad, yonetmen, tur, yapim_yeri, fragmanlink, konu]):
            QMessageBox.warning(self,"Film Ekle","Lütfen bilgileri eksiksiz girin.", QMessageBox.Ok)
            return

        yanit = QMessageBox.warning(self,"Film Ekle","Film eklemek istediğine emin misin?",QMessageBox.Yes,QMessageBox.No)
        if yanit == QMessageBox.No:
            return
        
        link = video_id(fragmanlink)

        if link is None:
            QMessageBox.warning(self,"Film Ekle","Lütfen geçerli bir YouTube linki girin.", QMessageBox.Ok)
            return
        
        Film.film_ekle(ad, yonetmen, tur, yapim_yili, sure, yapim_yeri, konu, link)
        self.film_ekle_sinyal.emit()

        yanit = QMessageBox.information(self, "Film Ekle", "Film ekleme işlemi tamamlandı", QMessageBox.Ok)
        self.close()


def video_id(url):
    patterns = [
        r"(?<=v=)[a-zA-Z0-9_-]+(?=&|\?|$)",
        r"(?<=be/)[a-zA-Z0-9_-]+(?=&|\?|$)",
        r"(?<=embed/)[a-zA-Z0-9_-]+(?=&|\?|$)",
        r"(?<=v/)[^#\&\?]*",
        r"(?<=user/)[a-zA-Z0-9_-]+(?=&|\?|$)",
        r"(?<=list=)[^#\&\?]*"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group()
    
    return None
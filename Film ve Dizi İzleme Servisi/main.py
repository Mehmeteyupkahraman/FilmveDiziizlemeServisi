from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from giris_ui import Ui_MainWindow
from kayit_ui import Ui_Form
from veritabani import veritabani
from ana import AnaSayfa
from film import Kullanici

class arayuz(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.qtprogram = Ui_MainWindow()
        self.qtprogram.setupUi(self)
        self.qtprogram.girisButon.clicked.connect(self.girisyap)
        kayitsayfa = Ui_Form()
        
        self.qtprogram.kayitButon.clicked.connect(lambda: kayitsayfa.show())

    def girisyap(self):
        kullaniciadi = self.qtprogram.kullaniciAdiLine.text()
        sifre = self.qtprogram.sifreLine.text()
        veritabani.query('SELECT * FROM kullanicilar WHERE kullaniciadi = ? AND sifre = ?', (kullaniciadi, sifre))
        uyesql = veritabani.fetchone()

        if uyesql is None:
            msg = QMessageBox()
            msg.setText("Kullanıcı adı veya şifre yanlış.")
            msg.setWindowTitle("Giriş")
            msg.setIcon(QMessageBox.Warning)
            msg.setStyleSheet("background-color: rgb(255, 255, 255);")
            msg.exec_()
            return
        
        uye = Kullanici(*uyesql)

        self.anasayfa = AnaSayfa(uye)
        self.anasayfa.show()
        self.close()


app = QApplication([])
pencere = arayuz()
pencere.show()
app.exec_()

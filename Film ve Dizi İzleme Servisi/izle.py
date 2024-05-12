from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class IzlemeSayfa(QWidget):
    def __init__(self, uye):
        super().__init__()
        self.setWindowTitle("Film İzle")
        self.setGeometry(100, 100, 800, 600)
        self.webView = QWebEngineView()
        layout = QVBoxLayout()
        layout.addWidget(self.webView)
        self.setLayout(layout)
        self.uye = uye

    def goster(self, film):
        film = film
        self.show()
        
        self.webView.setUrl(QUrl("https://www.youtube.com/embed/" + film.fragman))
        self.uye.gecmise_ekle(film)

    def closeEvent(self, event):
        # Stop the video playback when the window is closed
        self.webView.setUrl(QUrl("about:blank"))
        event.accept()
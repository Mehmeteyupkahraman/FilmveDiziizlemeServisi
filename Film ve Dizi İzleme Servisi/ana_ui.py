# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ana.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 471)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.foto = QtWidgets.QLabel(self.centralwidget)
        self.foto.setEnabled(True)
        self.foto.setGeometry(QtCore.QRect(20, 30, 231, 311))
        self.foto.setText("")
        self.foto.setScaledContents(True)
        self.foto.setAlignment(QtCore.Qt.AlignCenter)
        self.foto.setObjectName("foto")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 10, 425, 160))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.filmadi = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.filmadi.setFont(font)
        self.filmadi.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filmadi.setObjectName("filmadi")
        self.verticalLayout_2.addWidget(self.filmadi)
        self.filmyonetmeni = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.filmyonetmeni.setFont(font)
        self.filmyonetmeni.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filmyonetmeni.setObjectName("filmyonetmeni")
        self.verticalLayout_2.addWidget(self.filmyonetmeni)
        self.filmturu = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.filmturu.setFont(font)
        self.filmturu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.filmturu.setObjectName("filmturu")
        self.verticalLayout_2.addWidget(self.filmturu)
        self.yapimyili = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.yapimyili.setFont(font)
        self.yapimyili.setObjectName("yapimyili")
        self.verticalLayout_2.addWidget(self.yapimyili)
        self.suresi = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.suresi.setFont(font)
        self.suresi.setObjectName("suresi")
        self.verticalLayout_2.addWidget(self.suresi)
        self.yapimyeri = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.yapimyeri.setFont(font)
        self.yapimyeri.setObjectName("yapimyeri")
        self.verticalLayout_2.addWidget(self.yapimyeri)
        self.aciklama = QtWidgets.QLabel(self.centralwidget)
        self.aciklama.setGeometry(QtCore.QRect(280, 210, 531, 141))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.aciklama.setFont(font)
        self.aciklama.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aciklama.setScaledContents(False)
        self.aciklama.setWordWrap(True)
        self.aciklama.setObjectName("aciklama")
        self.konusu = QtWidgets.QLabel(self.centralwidget)
        self.konusu.setGeometry(QtCore.QRect(280, 180, 423, 33))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.konusu.setFont(font)
        self.konusu.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.konusu.setObjectName("konusu")
        self.oncekiButon = QtWidgets.QPushButton(self.centralwidget)
        self.oncekiButon.setGeometry(QtCore.QRect(50, 360, 51, 41))
        self.oncekiButon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/sol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oncekiButon.setIcon(icon)
        self.oncekiButon.setIconSize(QtCore.QSize(32, 32))
        self.oncekiButon.setObjectName("oncekiButon")
        self.sonrakiButon = QtWidgets.QPushButton(self.centralwidget)
        self.sonrakiButon.setGeometry(QtCore.QRect(170, 360, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sonrakiButon.setFont(font)
        self.sonrakiButon.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/sağ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sonrakiButon.setIcon(icon1)
        self.sonrakiButon.setIconSize(QtCore.QSize(32, 32))
        self.sonrakiButon.setObjectName("sonrakiButon")
        self.listeEkleButon = QtWidgets.QPushButton(self.centralwidget)
        self.listeEkleButon.setGeometry(QtCore.QRect(340, 350, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listeEkleButon.setFont(font)
        self.listeEkleButon.setObjectName("listeEkleButon")
        self.izleButon = QtWidgets.QPushButton(self.centralwidget)
        self.izleButon.setGeometry(QtCore.QRect(600, 350, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.izleButon.setFont(font)
        self.izleButon.setObjectName("izleButon")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 822, 21))
        self.menubar.setObjectName("menubar")
        self.menuAna_Sayfa = QtWidgets.QMenu(self.menubar)
        self.menuAna_Sayfa.setObjectName("menuAna_Sayfa")
        MainWindow.setMenuBar(self.menubar)
        self.actionfilmler = QtWidgets.QAction(MainWindow)
        self.actionfilmler.setObjectName("actionfilmler")
        self.actionDizler = QtWidgets.QAction(MainWindow)
        self.actionDizler.setObjectName("actionDizler")
        self.action_zleme_Listem = QtWidgets.QAction(MainWindow)
        self.action_zleme_Listem.setObjectName("action_zleme_Listem")
        self.action_zleme_Ge_mi_im = QtWidgets.QAction(MainWindow)
        self.action_zleme_Ge_mi_im.setObjectName("action_zleme_Ge_mi_im")
        self.actionKullan_c_Bilgileri = QtWidgets.QAction(MainWindow)
        self.actionKullan_c_Bilgileri.setObjectName("actionKullan_c_Bilgileri")
        self.filmEkle = QtWidgets.QAction(MainWindow)
        self.filmEkle.setObjectName("filmEkle")
        self.menuAna_Sayfa.addAction(self.filmEkle)
        self.menuAna_Sayfa.addAction(self.action_zleme_Listem)
        self.menuAna_Sayfa.addAction(self.action_zleme_Ge_mi_im)
        self.menubar.addAction(self.menuAna_Sayfa.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ana Sayfa"))
        self.filmadi.setText(_translate("MainWindow", "Film Adı: Esaretin Bedeli"))
        self.filmyonetmeni.setText(_translate("MainWindow", "Film Yönetmeni:  Frank Darabont"))
        self.filmturu.setText(_translate("MainWindow", "Film Türü: Dram,Suç"))
        self.yapimyili.setText(_translate("MainWindow", "Yapım Yılı: 1994     "))
        self.suresi.setText(_translate("MainWindow", "Süresi: 2 saat 22 dakika"))
        self.yapimyeri.setText(_translate("MainWindow", "Yapım Yeri: Amerika"))
        self.aciklama.setText(_translate("MainWindow", "Genç ve başarılı bir bankacı olan Andy Dufresne, karısını ve onun sevgilisini öldürmek suçundan ömür boyu hapse mahkum edilir ve Shawshank hapishanesine gönderilir. Burada başta Red olmak üzere yeni arkadaşlar edinir. Hapishane yaşamını uyum sağlamaya çalışırken diğer yandan da bilgisi ve kültürüyle etrafındaki insanları etkilemeyi başaracaktır.\n"
"\n"
""))
        self.konusu.setText(_translate("MainWindow", "Esaretin Bedeli Film Konusu:"))
        self.listeEkleButon.setText(_translate("MainWindow", "Listeye  Ekle"))
        self.izleButon.setText(_translate("MainWindow", "İzle"))
        self.menuAna_Sayfa.setTitle(_translate("MainWindow", "Ana Sayfa"))
        self.actionfilmler.setText(_translate("MainWindow", "Filmler"))
        self.actionDizler.setText(_translate("MainWindow", "Dizler"))
        self.action_zleme_Listem.setText(_translate("MainWindow", "İzleme Listem"))
        self.action_zleme_Ge_mi_im.setText(_translate("MainWindow", "İzleme Geçmişim"))
        self.actionKullan_c_Bilgileri.setText(_translate("MainWindow", "Kullanıcı Bilgileri"))
        self.filmEkle.setText(_translate("MainWindow", "Film Ekle"))

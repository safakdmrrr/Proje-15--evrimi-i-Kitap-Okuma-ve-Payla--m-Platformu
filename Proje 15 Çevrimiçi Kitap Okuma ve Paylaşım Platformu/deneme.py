import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QTextEdit, QDialog, QListWidget

class KitapYorumListesi(QWidget):
    def __init__(self, kitaplar, yorumlar):
        super().__init__()
        self.setWindowTitle("Kitap ve Yorum Listesi")
        self.setGeometry(200, 200, 400, 300)

        self.layout = QVBoxLayout()

        self.kitaplar_label = QLabel("Kitaplar:", self)
        self.layout.addWidget(self.kitaplar_label)
        self.kitaplar_list_widget = QListWidget(self)
        for kitap in kitaplar:
            self.kitaplar_list_widget.addItem(f"{kitap['Adı']} - {kitap['Yazarı']} - {kitap['Yayınevi']}")
        self.layout.addWidget(self.kitaplar_list_widget)

        self.yorumlar_label = QLabel("Yorumlar:", self)
        self.layout.addWidget(self.yorumlar_label)
        self.yorumlar_list_widget = QListWidget(self)
        for yorum in yorumlar:
            self.yorumlar_list_widget.addItem(yorum)
        self.layout.addWidget(self.yorumlar_list_widget)

        self.setLayout(self.layout)


class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Çevrimiçi Kitap Okuma ve Paylaşım Platformu")
        self.setGeometry(100, 100, 400, 400)

        self.kitaplar = []  # Kitapları saklayacak liste
        self.yorumlar = []  # Yorumları saklayacak liste

        self.init_ui()

    def init_ui(self):
        self.label_kitap_adi = QLabel("Kitap Adı:", self)
        self.label_kitap_adi.move(50, 50)
        self.kitap_adi = QLineEdit(self)
        self.kitap_adi.move(150, 50)

        self.label_yazar = QLabel("Yazarı:", self)
        self.label_yazar.move(50, 100)
        self.yazar = QLineEdit(self)
        self.yazar.move(150, 100)

        self.label_yayinevi = QLabel("Yayınevi:", self)
        self.label_yayinevi.move(50, 150)
        self.yayinevi = QLineEdit(self)
        self.yayinevi.move(150, 150)

        self.kitap_ekle_button = QPushButton("Kitap Ekle", self)
        self.kitap_ekle_button.move(150, 200)
        self.kitap_ekle_button.clicked.connect(self.kitap_ekle)

        self.yorum_text = QTextEdit(self)
        self.yorum_text.setGeometry(50, 250, 300, 100)

        self.yorum_ekle_button = QPushButton("Yorum Yap", self)
        self.yorum_ekle_button.move(150, 370)
        self.yorum_ekle_button.clicked.connect(self.yorum_ekle)

        self.listele_button = QPushButton("Listele", self)
        self.listele_button.move(250, 200)
        self.listele_button.clicked.connect(self.listele)

        self.yorumlar_label = QLabel("Yorumlar:", self)
        self.yorumlar_label.move(50, 370)

    def kitap_ekle(self):
        kitap_adı = self.kitap_adi.text()
        yazarı = self.yazar.text()
        yayınevi = self.yayinevi.text()

        self.kitaplar.append({"Adı": kitap_adı, "Yazarı": yazarı, "Yayınevi": yayınevi})

        self.kitap_adi.clear()
        self.yazar.clear()
        self.yayinevi.clear()

    def yorum_ekle(self):
        yorum = self.yorum_text.toPlainText()

        self.yorumlar.append(yorum)

        self.yorum_text.clear()

    def listele(self):
        self.liste_pencere = KitapYorumListesi(self.kitaplar, self.yorumlar)
        self.liste_pencere.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())

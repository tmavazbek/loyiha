import json

from PyQt5.QtWidgets import * 

class ListWindow(QWidget):
    def __init__(self, obj):
        super().__init__()

        self.main_window = obj

        self.v_main_lay = QVBoxLayout()
        self.h_lbl_lay = QHBoxLayout()

        self.lbl_royxat = QLabel("Kitoblar ro'yxati")
        self.lbl_royxat.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.lbl_nom = QLabel("Nomi")
        self.lbl_muallif = QLabel("Muallifi")

        self.lst_wdg = QListWidget()
        f = open("kutubxona.json")
        data = json.load(f)
        for book in data:
            self.lst_wdg.addItem(f"{book['nomi']}\t{book['muallif']}")
        f.close()

        self.btn_back = QPushButton("back")
        self.btn_back.clicked.connect(self.Back)

        self.h_lbl_lay.addWidget(self.lbl_nom)
        self.h_lbl_lay.addWidget(self.lbl_muallif)

        self.v_main_lay.addWidget(self.lbl_royxat)
        self.v_main_lay.addLayout(self.h_lbl_lay)
        self.v_main_lay.addWidget(self.lst_wdg)
        self.v_main_lay.addWidget(self.btn_back)

        self.setLayout(self.v_main_lay)

    def Back(self):
        self.hide()
        self.main_window.show()
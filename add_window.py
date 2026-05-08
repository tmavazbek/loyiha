import json

from PyQt5.QtWidgets import * 

class AddWindow(QWidget):
    def __init__(self, obj):
        super().__init__()

        self.main_window = obj

        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()

        self.edit_nomi = QLineEdit()
        self.edit_nomi.setPlaceholderText("Nomi")

        self.edit_muallif = QLineEdit()
        self.edit_muallif.setPlaceholderText("Muallif")

        self.edit_yil = QLineEdit()
        self.edit_yil.setPlaceholderText("Yil")

        self.edit_janr = QLineEdit()
        self.edit_janr.setPlaceholderText("Janr")

        self.btn_back = QPushButton("Back")
        self.btn_back.clicked.connect(self.Back)

        self.btn_ok = QPushButton("OK")
        self.btn_ok.clicked.connect(self.Ok)

        self.h_btn_lay.addWidget(self.btn_back)
        self.h_btn_lay.addWidget(self.btn_ok)

        self.v_main_lay.addWidget(self.edit_nomi)
        self.v_main_lay.addWidget(self.edit_muallif)
        self.v_main_lay.addWidget(self.edit_yil)
        self.v_main_lay.addWidget(self.edit_janr)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def Back(self):
        self.hide()
        self.main_window.show()

    def Ok(self):
        nomi = self.edit_nomi.text()
        muallif = self.edit_muallif.text()
        yil = self.edit_yil.text()
        janr = self.edit_janr.text()

        if nomi and muallif and yil and janr:
            f = open("kutubxona.json", "r")
            data = json.load(f)
            id = len(data) + 1
            data.append({
                "id": id,
                "nomi": nomi,
                "muallif": muallif,
                "yil": yil,
                "janr": janr
            })
            f.close()
            f = open("kutubxona.json", "w")
            json.dump(data, f, indent=4)
            f.close()
            QMessageBox().information(self, "Muvaffaqiyatli", "Kitob muvaffaqiyatli qo'shildi")
            self.Back()
        else:
            QMessageBox().critical(self, "e'tiroz", "Barcha maydonlar to'ldirilishi shart")

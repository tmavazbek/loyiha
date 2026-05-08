import json 
from PyQt5.QtWidgets import * 
from add_window import AddWindow

class SearchWindow(QWidget):
    def __init__(self, obj):
        super().__init__()

        self.main_window = obj

        self.v_main_lay = QVBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        self.h_radio_lay = QHBoxLayout()

        self.radio_id = QRadioButton("Id")
        self.radio_nomi = QRadioButton("Nomi")
        self.radio_muallif = QRadioButton("Muallifi")
        self.radio_yil = QRadioButton("Yili")
        self.radio_janr = QRadioButton("Janr")

        self.edit = QLineEdit()

        self.lbl = QLabel()

        self.btn_back = QPushButton("back")
        self.btn_back.clicked.connect(self.Back)

        self.btn_ok = QPushButton("ok")
        self.btn_ok.clicked.connect(self.Ok)

        self.btn_add = QPushButton("add")
        self.btn_add.clicked.connect(self.Add)
        self.btn_add.hide()

        self.h_radio_lay.addWidget(self.radio_id)
        self.h_radio_lay.addWidget(self.radio_nomi)
        self.h_radio_lay.addWidget(self.radio_muallif)
        self.h_radio_lay.addWidget(self.radio_yil)
        self.h_radio_lay.addWidget(self.radio_janr)

        self.h_btn_lay.addWidget(self.btn_back)
        self.h_btn_lay.addWidget(self.btn_ok)
        self.h_btn_lay.addWidget(self.btn_add)

        self.v_main_lay.addLayout(self.h_radio_lay)
        self.v_main_lay.addWidget(self.edit)
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def Back(self):
        self.hide()
        self.main_window.show()

    def Ok(self):
        self.btn_add.hide()
        self.lbl.clear()
        
        if not self.radio_id.isChecked() and not self.radio_nomi.isChecked() and not self.radio_muallif.isChecked() and not self.radio_yil.isChecked() and not self.radio_janr.isChecked():
            QMessageBox().critical(self, "e'tiroz", "Biror birini tanlang!")
            return

        if not self.edit.text():
            QMessageBox().critical(self, "e'tiroz", "So'z kiriting!")
            return

        f = open("kutubxona.json", encoding="utf-8")
        data = json.load(f)

        if self.radio_id.isChecked():
            id = self.edit.text()
            if id.isdigit():
                id = int(id)
                for book in data:
                    if book["id"] == id:
                        self.lbl.setText(f"{book['nomi']}\t{book['muallif']}\t{book['yil']}\t{book['janr']}")
                        break
                else:
                    self.lbl.setText("So'z topilmadi!")
                    self.btn_add.show()
            else:
                QMessageBox().critical(self, "e'tiroz", "Id raqam bo'lishi kerak!")

        else:
            word = self.edit.text().lower()
            for book in data:
                if self.radio_nomi.isChecked() and word in book["nomi"].lower():
                    self.lbl.setText(f"{book['nomi']}\t{book['muallif']}\t{book['yil']}\t{book['janr']}")
                    break
                elif self.radio_muallif.isChecked() and word in book["muallif"].lower():
                    self.lbl.setText(f"{book['nomi']}\t{book['muallif']}\t{book['yil']}\t{book['janr']}")
                    break
                elif self.radio_yil.isChecked() and word in book["yil"].lower():
                    self.lbl.setText(f"{book['nomi']}\t{book['muallif']}\t{book['yil']}\t{book['janr']}")
                    break
                elif self.radio_janr.isChecked() and word in book["janr"].lower():
                    self.lbl.setText(f"{book['nomi']}\t{book['muallif']}\t{book['yil']}\t{book['janr']}")
                    break
            else:
                self.lbl.setText("Kitob topilmadi!")
                self.btn_add.show()
        f.close()

    def Add(self):
        self.hide()
        self.window_add = AddWindow(self)
        self.window_add.show()
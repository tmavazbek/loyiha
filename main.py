from PyQt5.QtWidgets import * 

from add_window import AddWindow
from search_window import SearchWindow
from list_window import ListWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()

        self.lbl_kutubxona = QLabel("Kutubxona")
        self.lbl_kutubxona.setStyleSheet("font-size: 20px; font-weight: bold;")

        self.btn_add = QPushButton("Kitob Qo'shish")
        self.btn_add.clicked.connect(self.Add)

        self.btn_search = QPushButton("Qidirish")
        self.btn_search.clicked.connect(self.Search)

        self.btn_list = QPushButton("Ro'kitoblar ro'yxati")
        self.btn_list.clicked.connect(self.List)

        self.btn_exit = QPushButton("exit")
        self.btn_exit.clicked.connect(exit)

        self.v_main_lay.addWidget(self.lbl_kutubxona)
        self.v_main_lay.addWidget(self.btn_add)
        self.v_main_lay.addWidget(self.btn_search)
        self.v_main_lay.addWidget(self.btn_list)
        self.v_main_lay.addWidget(self.btn_exit)

        self.setLayout(self.v_main_lay)
    
    def List(self):
        self.hide()
        self.window_list = ListWindow(self)
        self.window_list.show()

    def Search(self):
        self.hide()
        self.window_search = SearchWindow(self)
        self.window_search.show()

    def Add(self):
        self.hide()
        self.window_add = AddWindow(self)
        self.window_add.show()

app = QApplication([])
win = MainWindow()
win.show()
app.exec_()

import sys
import re

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog

class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_zapisz.clicked.connect(self.getUser)
        self.ui.pushButton_zapisz_2.clicked.connect(self.filetext)
        self.show()

    def getUser(self):
        imie = self.ui.lineEdit_name.text()
        naziwsko = self.ui.lineEdit_surname.text()
        pesel = self.ui.lineEdit_pesel.text()
        numbertl = self.ui.lineEdit_numertelefonu.text()

        dane = imie+" "+naziwsko

        if re.match('[0-9]{11}$',pesel):
            self.ui.listWidget.addItem(dane)
        else:
            blad = QMessageBox()
            blad.setText("Pesel nie jest poprawny")
            blad.exec()

    def filetext(self):
        imie = self.ui.lineEdit_name.text()
        naziwsko = self.ui.lineEdit_surname.text()
        pesel = self.ui.lineEdit_pesel.text()
        numbertl = self.ui.lineEdit_numertelefonu.text()

        dane = imie + " " + naziwsko
        namefile = imie+'_'+naziwsko+".txt"

        if re.match('[0-9]{11}$', pesel):
            with open(namefile, 'a') as file:
                file.write(dane + '\n')
        else:
            blad = QMessageBox()
            blad.setText("Pesel nie jest poprawny sproboj ponownie")
            blad.exec()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
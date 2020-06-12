import sys
from valida_cpf import valida_cpf
from gera_cpf import gera_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import design


class GeraValidaCpf(QMainWindow, design.Ui_mainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnValidaCpf.clicked.connect(self.valida_cpf)
        self.BtnGeraCpf.clicked.connect(self.gera_cpf)

    def gera_cpf(self):
        self.labelRetorno.setText(
            str(gera_cpf())
        )

    def valida_cpf(self):
        cpf = self.inputValidaCpf.text()
        self.labelRetorno.setText(
            str(valida_cpf(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCpf()
    gera_valida_cpf.show()
    qt.exec_()

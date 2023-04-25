import PyQt6.QtWidgets as wi
import sys

class Fenster(wi.QWidget):
    def __init__(self):
        super().__init__()
        
        buEnde = wi.QPushButton("Ende", self)
        buEnde.move(40, 20)
        buEnde.clicked.connect(wi.QApplication.instance().quit)
        
        self.setWindowTitle("...")
        self.show()

anwendung = wi.QApplication(sys.argv)
fenster = Fenster()
sys.exit(anwendung.exec())

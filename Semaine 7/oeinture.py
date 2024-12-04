from PySide6.QtCore import QSize
from PySide6.QtGui import QPixmap, QColorConstants, QColor, QPainter, QPen, Qt, QBrush
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication


class Monpeintre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NatePaint")
        self.canevas = QPixmap(QSize(500,400))
        self.etiquettecentrale = QLabel()
        self.etiquettecentrale.setPixmap(self.canevas)

    def dessiner(self):
        canevas = self.canevas
        canevas.fill(QColor(128,240,199))
        painter= QPainter(canevas)
        crayon = QPen()
        crayon.setColor(QColor(255,255,255))
        crayon.setWidth(15)
        pinceau = QBrush(crayon)
        pinceau.setStyle(Qt.BrushStyle.ConicalGradientPattern)
        painter.setPen(crayon)
        painter.setBrush(QBrush(pinceau))
        painter.drawEllipse(9, 10, 500, 500)

app = QApplication()
qp = Monpeintre()
qp.show()
app.exec()
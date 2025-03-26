from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class ConsultasWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Consultas de Candidaturas")
        self.setGeometry(150, 150, 600, 400)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        label = QLabel("Aqui serão exibidas as consultas de candidatos.")
        layout.addWidget(label)

        self.setLayout(layout)

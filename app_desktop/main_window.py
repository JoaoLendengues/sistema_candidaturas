import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QLabel, QWidget, QVBoxLayout

from consultas import ConsultasWindow
from relatorios import RelatoriosWindow  # Importa a janela de relatórios

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Candidaturas")
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()

    def init_ui(self):
        # Criando a barra de menu
        menu_bar = self.menuBar()

        # Criando menus
        menu_arquivo = menu_bar.addMenu("Arquivo")
        menu_consultas = menu_bar.addMenu("Consultas")
        menu_relatorios = menu_bar.addMenu("Relatórios")

        # Criando ações
        sair_action = QAction("Sair", self)
        sair_action.triggered.connect(self.close)
        menu_arquivo.addAction(sair_action)

        abrir_consultas_action = QAction("Abrir Consultas", self)
        abrir_consultas_action.triggered.connect(self.abrir_consultas)
        menu_consultas.addAction(abrir_consultas_action)

        abrir_relatorios_action = QAction("Abrir Relatórios", self)
        abrir_relatorios_action.triggered.connect(self.abrir_relatorios)  # Abre a tela de relatórios
        menu_relatorios.addAction(abrir_relatorios_action)

        # Criando o layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        label = QLabel("Bem-vindo ao Sistema de Candidaturas!")
        layout.addWidget(label)

        central_widget.setLayout(layout)

    def abrir_consultas(self):
        self.consultas_window = ConsultasWindow()  # Instancia corretamente a janela
        self.consultas_window.show()

    def abrir_relatorios(self):
        self.relatorios_window = RelatoriosWindow()  # Instancia corretamente a janela de relatórios
        self.relatorios_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import QApplication
from app_desktop.relatorios import RelatoriosWindow  # Importando a janela de Relatórios

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Criação da janela de relatórios
    window = RelatoriosWindow()

    # Exibe a janela
    window.show()

    # Inicia o loop de execução do PyQt
    sys.exit(app.exec())

import sys
import os
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QMessageBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QHeaderView
from PyQt6.uic.Compiler.qtproxies import QtWidgets

from db.conexao import conectar

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class RelatoriosWindow(QtWidgets):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Relatórios de Candidaturas")
        self.setGeometry(150, 150, 700, 400)

        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        self.label = QLabel("Relatórios de Candidatos")
        layout.addWidget(self.label)

        # Filtros
        filtros_layout = QHBoxLayout()

        self.filtro_nome = QLineEdit(self)
        self.filtro_nome.setPlaceholderText("Filtrar por Nome")
        filtros_layout.addWidget(self.filtro_nome)

        self.filtro_email = QLineEdit(self)
        self.filtro_email.setPlaceholderText("Filtrar por E-mail")
        filtros_layout.addWidget(self.filtro_email)

        layout.addLayout(filtros_layout)

        # Botões de Exportação
        self.export_pdf_button = QPushButton("Exportar para PDF")
        layout.addWidget(self.export_pdf_button)

        self.export_csv_button = QPushButton("Exportar para CSV")
        layout.addWidget(self.export_csv_button)

        # Tabela
        self.table = QTableWidgetItem()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Nome", "E-mail", "Telefone"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table)

        self.setLayout(layout)

        # Carregar os dados ao iniciar
        self.carregar_dados()

    def carregar_dados(self):
        try:
            # Obtendo dados filtrados
            nome = self.filtro_nome.text()
            email = self.filtro_email.text()

            candidatos = self.buscar_relatorios_no_banco(nome, email)

            # Preencher tabela
            self.table.setRowCount(len(candidatos))
            for row, candidato in enumerate(candidatos):
                for col, dado in enumerate(candidato):
                    self.table.setItem(row, col, QTableWidgetItem(str(dado)))

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar dados: {str(e)}")

    def buscar_relatorios_no_banco(self, nome, email):
        try:
            conn = conectar()
            cursor = conn.cursor()

            # Construindo a consulta com base nos filtros
            query = "SELECT id, nome, email, telefone FROM candidatos WHERE 1=1"
            params = []

            if nome:
                query += " AND nome LIKE ?"
                params.append(f"%{nome}%")

            if email:
                query += " AND email LIKE ?"
                params.append(f"%{email}%")

            cursor.execute(query, params)
            candidatos = cursor.fetchall()
            conn.close()
            return candidatos
        except Exception as e:
            raise RuntimeError(f"Erro na consulta ao banco de dados: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RelatoriosWindow()
    window.show()
    sys.exit(app.exec())
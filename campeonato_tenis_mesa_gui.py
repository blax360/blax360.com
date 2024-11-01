import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QLineEdit, QComboBox, QTableWidget, 
                             QTableWidgetItem, QFileDialog, QMessageBox)
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Campeonato de Tenis de Mesa")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #4a4a4a;
                color: white;
                border: none;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #5a5a5a;
            }
            QLabel {
                font-size: 14px;
            }
            QLineEdit, QComboBox {
                padding: 5px;
                font-size: 14px;
            }
        """)

        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Título
        titulo = QLabel("Campeonato de Tenis de Mesa")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        layout.addWidget(titulo)

        # Configuración del campeonato
        config_layout = QHBoxLayout()
        config_layout.addWidget(QLabel("Mejor de:"))
        self.combo_mejor_de = QComboBox()
        self.combo_mejor_de.addItems(["3", "5", "7"])
        config_layout.addWidget(self.combo_mejor_de)
        config_layout.addStretch()
        layout.addLayout(config_layout)

        # Inscripción de jugadores
        inscripcion_layout = QHBoxLayout()
        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Nombre")
        self.input_club = QLineEdit()
        self.input_club.setPlaceholderText("Club")
        self.input_ranking = QLineEdit()
        self.input_ranking.setPlaceholderText("Ranking")
        inscripcion_layout.addWidget(self.input_nombre)
        inscripcion_layout.addWidget(self.input_club)
        inscripcion_layout.addWidget(self.input_ranking)
        btn_inscribir = QPushButton("Inscribir Jugador")
        btn_inscribir.clicked.connect(self.inscribir_jugador)
        inscripcion_layout.addWidget(btn_inscribir)
        layout.addLayout(inscripcion_layout)

        # Tabla de jugadores
        self.tabla_jugadores = QTableWidget(0, 3)
        self.tabla_jugadores.setHorizontalHeaderLabels(["Nombre", "Club", "Ranking"])
        layout.addWidget(self.tabla_jugadores)

        # Botones de acción
        botones_layout = QHBoxLayout()
        btn_importar = QPushButton("Importar CSV")
        btn_importar.clicked.connect(self.importar_csv)
        btn_crear_grupos = QPushButton("Crear Grupos")
        btn_crear_grupos.clicked.connect(self.crear_grupos)
        btn_jugar = QPushButton("Jugar Campeonato")
        btn_jugar.clicked.connect(self.jugar_campeonato)
        botones_layout.addWidget(btn_importar)
        botones_layout.addWidget(btn_crear_grupos)
        botones_layout.addWidget(btn_jugar)
        layout.addLayout(botones_layout)

    def inscribir_jugador(self):
        nombre = self.input_nombre.text()
        club = self.input_club.text()
        ranking = self.input_ranking.text()
        if nombre and club and ranking:
            fila = self.tabla_jugadores.rowCount()
            self.tabla_jugadores.insertRow(fila)
            self.tabla_jugadores.setItem(fila, 0, QTableWidgetItem(nombre))
            self.tabla_jugadores.setItem(fila, 1, QTableWidgetItem(club))
            self.tabla_jugadores.setItem(fila, 2, QTableWidgetItem(ranking))
            self.input_nombre.clear()
            self.input_club.clear()
            self.input_ranking.clear()
        else:
            QMessageBox.warning(self, "Error", "Por favor, complete todos los campos.")

    def importar_csv(self):
        # Implementar la importación de CSV
        pass

    def crear_grupos(self):
        # Implementar la creación de grupos
        pass

    def jugar_campeonato(self):
        # Implementar la lógica del campeonato
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())

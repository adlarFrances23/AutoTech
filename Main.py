import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Example")
        self.setGeometry(100, 100, 400, 300)

        # Layout and Widgets
        layout = QVBoxLayout()

        self.label = QLabel("Hello, PyQt6!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button)

        # Set the layout to the window
        self.setLayout(layout)

    def on_button_clicked(self):
        self.label.setText("Button Clicked!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

"""PyQt5 + OpenCV video çizim uygulaması.

Gereksinimler: pip install PyQt5 opencv-python
"""

from pathlib import Path
import sys

import cv2
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QApplication, QComboBox, QFormLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget,
)


VIDEO_DIR = Path(__file__).resolve().parent.parent / "Videolar"
VIDEO_FILES = {
    "Kalabalık": "KALABALIK İNSANLAR (HD) - STOK VİDEO.mp4",
    "New York": "times_square.mp4",
}


class VideoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Üzerine Şekil ve Yazı Çizme")
        self.capture = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_frame)
        self.options = {"shape": None}
        self.build_ui()

    def build_ui(self):
        root = QWidget()
        layout = QVBoxLayout(root)

        video_row = QHBoxLayout()
        video_row.addWidget(QLabel("Video:"))
        self.video_box = QComboBox()
        self.video_box.addItems(VIDEO_FILES)
        video_row.addWidget(self.video_box)
        layout.addLayout(video_row)

        square = QGroupBox("Kare")
        form = QFormLayout(square)
        self.square_fields = [self.field() for _ in range(4)]
        for label, field in zip(("P1 x", "P1 y", "P2 x", "P2 y"), self.square_fields):
            form.addRow(label, field)
        self.square_button = QPushButton("Kareyi seç")
        self.square_button.clicked.connect(self.set_square)
        form.addRow(self.square_button)

        circle = QGroupBox("Daire")
        form = QFormLayout(circle)
        self.circle_fields = [self.field() for _ in range(3)]
        for label, field in zip(("Merkez x", "Merkez y", "Yarıçap"), self.circle_fields):
            form.addRow(label, field)
        self.circle_button = QPushButton("Daireyi seç")
        self.circle_button.clicked.connect(self.set_circle)
        form.addRow(self.circle_button)

        text = QGroupBox("Yazı")
        form = QFormLayout(text)
        self.text_field = QLineEdit()
        self.text_field.setPlaceholderText("Videoda gösterilecek yazı")
        form.addRow("Metin", self.text_field)
        self.text_button = QPushButton("Yazıyı seç")
        self.text_button.clicked.connect(self.set_text)
        form.addRow(self.text_button)

        controls = QHBoxLayout()
        self.start_button = QPushButton("Videoyu başlat")
        self.start_button.clicked.connect(self.start_video)
        self.stop_button = QPushButton("Durdur")
        self.stop_button.clicked.connect(self.stop_video)
        controls.addWidget(self.start_button)
        controls.addWidget(self.stop_button)

        layout.addWidget(square)
        layout.addWidget(circle)
        layout.addWidget(text)
        layout.addLayout(controls)
        layout.addWidget(QLabel("OpenCV penceresinde çıkmak için q tuşuna basın."))
        self.setCentralWidget(root)

    @staticmethod
    def field():
        field = QLineEdit()
        field.setPlaceholderText("Tam sayı")
        return field

    def integers(self, fields):
        try:
            return tuple(int(field.text().strip()) for field in fields)
        except ValueError:
            raise ValueError("Koordinat ve yarıçap alanları tam sayı olmalıdır.")

    def set_square(self):
        try:
            self.options = {"shape": "square", "values": self.integers(self.square_fields)}
            self.statusBar().showMessage("Kare seçildi.")
        except ValueError as error:
            self.error(str(error))

    def set_circle(self):
        try:
            values = self.integers(self.circle_fields)
            if values[2] <= 0:
                raise ValueError("Yarıçap sıfırdan büyük olmalıdır.")
            self.options = {"shape": "circle", "values": values}
            self.statusBar().showMessage("Daire seçildi.")
        except ValueError as error:
            self.error(str(error))

    def set_text(self):
        value = self.text_field.text().strip()
        if not value:
            self.error("Lütfen gösterilecek bir yazı girin.")
            return
        self.options = {"shape": "text", "values": value}
        self.statusBar().showMessage("Yazı seçildi.")

    def start_video(self):
        self.stop_video()
        if self.options["shape"] is None:
            self.error("Önce kare, daire veya yazı için Seç düğmesine basın.")
            return
        path = VIDEO_DIR / VIDEO_FILES[self.video_box.currentText()]
        if not path.exists():
            self.error(f"Video bulunamadı: {path}")
            return
        self.capture = cv2.VideoCapture(str(path))
        if not self.capture.isOpened():
            self.error("Video açılamadı.")
            self.capture.release()
            self.capture = None
            return
        fps = self.capture.get(cv2.CAP_PROP_FPS) or 25
        self.timer.start(max(1, int(1000 / fps)))

    def show_frame(self):
        ok, frame = self.capture.read()
        if not ok:
            self.stop_video()
            return
        shape, values = self.options["shape"], self.options["values"]
        if shape == "square":
            cv2.rectangle(frame, (values[0], values[1]), (values[2], values[3]), (0, 0, 255), 3)
        elif shape == "circle":
            cv2.circle(frame, (values[0], values[1]), values[2], (0, 0, 255), 3)
        else:
            cv2.putText(frame, values, (40, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            self.stop_video()

    def stop_video(self):
        self.timer.stop()
        if self.capture is not None:
            self.capture.release()
            self.capture = None
        cv2.destroyAllWindows()

    def error(self, message):
        QMessageBox.warning(self, "Hata", message)

    def closeEvent(self, event):
        self.stop_video()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoApp()
    window.resize(500, 650)
    window.show()
    sys.exit(app.exec_())

from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpinBox, QSlider, QMessageBox, QInputDialog, QProgressBar)
from PySide6.QtCore import QTimer, Qt
import sys
import json
import os

DATAFILE = "ptimer.json"

def load_data():
    if not os.path.exists(DATAFILE):
        return{"work": 25}
    with open(DATAFILE, "r") as file:
        return json.load(file)
    
def save_data(data):
    with open(DATAFILE, "w") as file:
        json.dump(data, file)

class pomodoro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pomodoro timerrrrrrrrrr")
        self.resize(400, 300)
        self.data = load_data()
        self.totaltime = self.data["work"]*60
        self.breaktime = 5 * 60
        self.timeleft = self.totaltime
        self.elapsed = 0
        self.mode = "work"
        self.running = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.setInterval(1000)

        self.title = QLabel("pomodoro timer")
        self.time_label = QLabel("00:00")
        self.spin = QSpinBox()
        self.spin.setRange(1, 120)
        self.spin.setValue(self.data["work"])
        self.slider = QSlider()
        self.slider.setRange(1, 120)
        self.slider.setValue(self.data["work"])
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.start_btn = QPushButton("start")
        self.reset_btn = QPushButton("reset")
        self.rename_btn = QPushButton("rename")
        self.start_btn.clicked.connect(self.start_timer)
        self.reset_btn.clicked.connect(self.reset_timer)
        self.rename_btn.clicked.connect(self.rename_session)
        self.slider.valueChanged.connect(self.slider_changed)
        self.spin.valueChanged.connect(self.spin_changed)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.title)
        self.time_label.setStyleSheet("""
            font-size: 60px;
            font-weight: bold;
            color: #00ffd5;""")
        layout.addWidget(self.time_label)
        layout.setAlignment(self.time_label, Qt.AlignCenter)
        input_row = QHBoxLayout()
        input_row.addWidget(self.spin)
        input_row.addWidget(self.slider)
        layout.addLayout(input_row)
        layout.addWidget(self.progress)
        button_row = QHBoxLayout()
        button_row.addWidget(self.start_btn)
        button_row.addWidget(self.reset_btn)
        button_row.addWidget(self.rename_btn)
        layout.addLayout(button_row)
        layout.addStretch()

        self.setStyleSheet("""
            QWidget{
                background-color: #0f1115;
                color: #00ffd5;
                font-size: 16px;}
            QPushButton{
                background-color: #00ffd5;
                color: #0f1115;
                padding: 8px;
                border-radius: 6px;}
            QPushButton:hover{
                background-color: #00c2a8;}
            QSpinBox{
                background-color: #1a1d24;}
            QSlider{
                background-color: #1a1d24;}
            QProgressBar{
                border: 1px solid #00ffd5;
                text-align: center;
                color: orange}
            QProgressBar::chunk{
                background-color: #00ffd5}
        """)
        self.update_label()
        self.update_progress()
    
    def spin_changed(self, value):
        self.slider.setValue(value)
        self.data["work"] = value
        save_data(self.data)
        self.reset_timer()
    
    def slider_changed(self,value):
        self.spin.setValue(value)
        self.data["work"] = value
        save_data(self.data)
        self.reset_timer()

    def start_timer(self):
        if not self.running:
            self.running = True
            self.timer.start()
    def reset_timer(self):
        self.running = False
        self.timer.stop()
        self.mode = "work"
        self.totaltime = self.spin.value() * 60
        self.timeleft = self.totaltime
        self.elapsed = 0
        self.update_label()
        self.update_progress()

    def tick(self):
        if self.timeleft > 0:
            self.timeleft -= 1
            self.elapsed += 1
            self.update_label()
            self.update_progress()
        else:
            self.timer.stop()
            self.running = False
            if self.mode == "work":
                QMessageBox.information(self, "break timeee :D", "stop workkk")
                self.mode = "break"
                self.timeleft = self.breaktime
                self.elapsed = 0
                self.timer.start()
            else:
                QMessageBox.information(self, "done", "break over D:")
                self.mode = "work"
                self.reset_timer()
    
    def update_label(self):
        mins = self.timeleft // 60
        secs = self.timeleft % 60
        self.time_label.setText(f"{self.mode.upper()} - {mins:02d}:{secs:02d}")

    def update_progress(self):
        total = self.totaltime if self.mode == "work" else self.breaktime
        percent = int((self.elapsed / total) * 100)
        self.progress.setValue(percent)

    def rename_session(self):
        name, ok = QInputDialog.getText(self, "rename", "session name:")
        if ok and name:
            self.title.setText(name)


app = QApplication(sys.argv)
window = pomodoro() # make an instance of our widget
window.show()
app.exec()

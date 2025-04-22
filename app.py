# car_motivator_app.py
import sys
import random
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QComboBox, 
                            QPushButton, QVBoxLayout, QWidget, QSystemTrayIcon, 
                            QMenu, QAction)
from PyQt5.QtCore import QTimer, QPropertyAnimation, QRect, Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap, QPainter

class CarMotivatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Luxury Car Motivator")
        self.setGeometry(100, 100, 400, 300)
        
        # Define luxury cars
        self.cars = {
            "Bentley Bentayga": "bentley.svg",
            "Rolls-Royce Phantom": "rolls.svg",
            "Ferrari SF90 Stradale": "ferrari.svg",
            "Lamborghini Revuelto": "lambo.svg",
            "Porsche 911 GT3 RS": "porsche.svg",
            "Aston Martin DBS": "aston.svg",
            "McLaren 720S": "mclaren.svg",
            "Bugatti Chiron": "bugatti.svg"
        }
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Car selection dropdown
        self.car_label = QLabel("Select Your Dream Car:")
        layout.addWidget(self.car_label)
        
        self.car_combo = QComboBox()
        self.car_combo.addItems(self.cars.keys())
        layout.addWidget(self.car_combo)
        
        # Start button
        self.start_button = QPushButton("Start Motivation")
        self.start_button.clicked.connect(self.start_motivation)
        layout.addWidget(self.start_button)
        
        # System tray setup
        self.tray_icon = QSystemTrayIcon(QIcon("icon.png"), self)
        tray_menu = QMenu()
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        show_action.triggered.connect(self.show)
        quit_action.triggered.connect(self.close_app)
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        
        # Animation timer
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.show_car_animation)
        
        # Selected car
        self.selected_car = None
        
    def start_motivation(self):
        self.selected_car = self.car_combo.currentText()
        self.hide()
        # Schedule first animation with random interval (40-60 minutes)
        interval = random.randint(40 * 60 * 1000, 60 * 60 * 1000)
        self.animation_timer.start(interval)
        
    def show_car_animation(self):
        # Create animation window
        self.anim_window = QWidget(None, Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.anim_window.setAttribute(Qt.WA_TranslucentBackground)
        
        # Create car label
        car_label = QLabel(self.anim_window)
        car_path = self.cars[self.selected_car]
        car_pixmap = QPixmap(car_path)
        car_label.setPixmap(car_pixmap.scaled(200, 100, Qt.KeepAspectRatio))
        car_label.setFixedSize(200, 100)
        
        # Set window size and position
        screen_width = QApplication.desktop().screenGeometry().width()
        screen_height = QApplication.desktop().screenGeometry().height()
        y_position = random.randint(100, screen_height - 200)
        self.anim_window.setGeometry(-200, y_position, 200, 100)
        self.anim_window.show()
        
        # Animate car across screen
        self.animation = QPropertyAnimation(self.anim_window, b"geometry")
        self.animation.setDuration(8000)  # 8 seconds to cross screen
        self.animation.setStartValue(QRect(-200, y_position, 200, 100))
        self.animation.setEndValue(QRect(screen_width + 100, y_position, 200, 100))
        self.animation.finished.connect(self.anim_window.close)
        self.animation.finished.connect(self.schedule_next_animation)
        self.animation.start()
        
    def schedule_next_animation(self):
        # Schedule next animation with random interval (40-60 minutes)
        interval = random.randint(40 * 60 * 1000, 60 * 60 * 1000)
        self.animation_timer.start(interval)
        
    def close_app(self):
        self.animation_timer.stop()
        if hasattr(self, 'anim_window') and self.anim_window:
            self.anim_window.close()
        self.tray_icon.hide()
        QApplication.quit()
        
    def closeEvent(self, event):
        # Minimize to tray when user closes the window
        event.ignore()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # Keep running when window is closed
    window = CarMotivatorApp()
    window.show()
    sys.exit(app.exec_())

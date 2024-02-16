import sys
from PySide6 import QtWidgets, QtGui, QtCore
from QlikAPI import resource_path


def confirm_dialog(self, message):
    msg = QtWidgets.QMessageBox(self)
    msg.setWindowTitle("Agree")
    msg.setText(message)
    msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    image_path = resource_path("assets/confirm.ico")  # Caminho absoluto da imagem
    icon = QtGui.QIcon(image_path)
    msg.setIconPixmap(icon.pixmap(QtCore.QSize(64, 64)))
    buttons = msg.buttons()
    for button in buttons:
        button.setStyleSheet("QPushButton { background-color: {}; \
                                       border-radius: 8px; \
                                      border: 1px; padding: 6px 12px; \
                                      font-size: 12px; min-width: 100px; } \
                                      QPushButton:hover { background-color: #FF8C00; }")
    return msg.exec()


def success_message(self, message):
    msg = QtWidgets.QMessageBox(self)
    msg.setWindowTitle("QCloud - Success")
    msg.setText(message)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    image_path = resource_path("assets/success.ico")  # Caminho absoluto da imagem
    icon = QtGui.QIcon(image_path)
    msg.setIconPixmap(icon.pixmap(QtCore.QSize(64, 64)))
    buttons = msg.buttons()
    for button in buttons:
        button.setStyleSheet("QPushButton { background-color: {}; \
                                               border-radius: 8px; \
                                              border: 1px; padding: 6px 12px; \
                                              font-size: 12px; min-width: 100px; } \
                                              QPushButton:hover { background-color: #FF8C00; }")
    return msg.exec()


def error_message(self, message):
    msg = QtWidgets.QMessageBox(self)
    msg.setWindowTitle("QCloud - Error")
    msg.setText(message)
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    image_path = resource_path("assets/error.ico")  # Caminho absoluto da imagem
    icon = QtGui.QIcon(image_path)
    msg.setIconPixmap(icon.pixmap(QtCore.QSize(64, 64)))
    buttons = msg.buttons()
    for button in buttons:
        button.setStyleSheet("QPushButton { background-color: {}; \
                                               border-radius: 8px; \
                                              border: 1px; padding: 6px 12px; \
                                              font-size: 12px; min-width: 100px; } \
                                              QPushButton:hover { background-color: #FF8C00; }")
    return msg.exec()



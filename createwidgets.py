from PySide6 import QtWidgets, QtGui, QtCore


def exp_label(self, label_text):
    label_widget = QtWidgets.QLabel(label_text)
    self.layout.addWidget(label_widget)
    return label_widget

def exp_textbox(self):
    entry = QtWidgets.QLineEdit()
    entry.setStyleSheet("""
                QLineEdit {
                    border: 2px solid #666666;
                    border-radius: 5px;
                    padding: 5px;
                }
            """)
    self.layout.addWidget(entry)
    return entry


def exp_combobox(self, options):
    combo = QtWidgets.QComboBox()
    combo.addItems(options)
    for i in range(combo.count()):
        combo.setItemText(i, f"{combo.itemText(i)}")
        combo.setStyleSheet("""
                    QComboBox {
                        border: 2px solid #666666;
                        border-radius: 5px;
                        padding: 5px;
                        padding-right: 20px;
                    }
                """)

    self.layout.addWidget(combo)
    return combo



def exp_btn_back(self, placeholder):
    btn_default = QtWidgets.QPushButton(placeholder)
    btn_default.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: #ffffff;
                border: 2px solid #2196F3;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
            """)
    self.layout.addWidget(btn_default)
    return btn_default


def exp_btn_next(self, placeholder):
    btn_next = QtWidgets.QPushButton(placeholder)
    btn_next.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: #ffffff;
                border: 2px solid #4CAF50;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            """)
    self.layout.addWidget(btn_next)
    return btn_next
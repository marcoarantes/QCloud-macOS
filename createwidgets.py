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
                    background-color: #dfdfdf;
                    color: black;
                    border-radius: 8px; 
                    border: 1px; padding: 6px 12px; 
                    font-size: 12px; min-width: 100px; 
                    } 
                QPushButton:hover { 
                    background-color: #f1f1f1; 
                    }
                """)
    self.layout.addWidget(btn_default)
    return btn_default


def exp_btn_next(self, placeholder):
    btn_next = QtWidgets.QPushButton(placeholder)
    btn_next.setStyleSheet("""
            QPushButton {
                background-color: #FF8C00;
                color: white;
                border-radius: 8px; 
                border: 1px; padding: 6px 12px; 
                font-size: 12px; min-width: 100px; 
                } 
            QPushButton:hover { 
                background-color: #fd9d00; 
            }
            """)
    self.layout.addWidget(btn_next)
    return btn_next

def exp_checkbox(self, placeholder):
    checkbox = QtWidgets.QCheckBox(placeholder)
    self.layout.addWidget(checkbox)
    return checkbox
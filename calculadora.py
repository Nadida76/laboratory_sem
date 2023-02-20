import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        # setting title
        self.setWindowTitle("Calculator")

        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_clear = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_third = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_clear)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_third)
        self.vbox.addLayout(self.hbox_result)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        # clear button
        self.b_clear = QPushButton("Clear", self)
        self.b_clear.setGeometry(5, 100, 200, 40)
        self.hbox_clear.addWidget(self.b_clear)

        # del one character button
        self.b_del = QPushButton("Del", self)
        self.b_del.setGeometry(210, 100, 145, 40)
        self.hbox_clear.addWidget(self.b_del)

        self.b_1 = QPushButton("1", self)
        self.hbox_third.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_third.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_third.addWidget(self.b_3)

        self.b_4 = QPushButton("4", self)
        self.hbox_second.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_second.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_7 = QPushButton("7", self)
        self.hbox_first.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_first.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_first.addWidget(self.b_9)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_second.addWidget(self.b_minus)

        self.b_mult = QPushButton("x", self)
        self.hbox_third.addWidget(self.b_mult)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        self.b_0 = QPushButton("0", self)
        self.hbox_result.addWidget(self.b_0)

        self.b_point = QPushButton(".", self)
        self.hbox_result.addWidget(self.b_point)

        self.b_div = QPushButton("÷", self)
        self.hbox_result.addWidget(self.b_div)

        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_result.clicked.connect(self._result)
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))
        self.b_point.clicked.connect(lambda: self._button("."))

        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_mult.clicked.connect(lambda: self._operation("x"))
        self.b_div.clicked.connect(lambda: self._operation("÷"))

        self.b_clear.clicked.connect(self.action_clear)
        self.b_del.clicked.connect(self.action_del)

    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    def _operation(self, op):
        try:
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText("")
        except:
            self.input.setText("Слова не допускаются")

    def _result(self):
        try:
            self.num_2 = float(self.input.text())
            if self.op == "+":
                self.res = self.num_1 + self.num_2
                if (self.res - int(self.res) == 0):
                    self.input.setText(str(int(self.res)))
                else:
                    self.input.setText(str(self.res))

            elif self.op == "-":
                self.res = self.num_1 - self.num_2

                if (self.res - int(self.res) == 0):
                    self.input.setText(str(int(self.res)))
                else:
                    self.input.setText(str(self.res))

            elif self.op == "x":
                self.res = self.num_1 * self.num_2
                if (self.res - int(self.res) == 0):
                    self.input.setText(str(int(self.res)))
                else:
                    self.input.setText(str(self.res))

            elif self.op == "÷":
                try:
                    self.res = self.num_1 / self.num_2

                    if (self.res - int(self.res) == 0):
                        self.input.setText(str(int(self.res)))
                    else:
                        self.input.setText(str(self.res))
                except:
                    self.input.setText("Деление на ноль невозможно")
        except:
            self.input.setText("Слова не допускаются")

    def action_clear(self):
        # clearing the label text
        self.input.setText("")

    def action_del(self):
        # clearing a single digit
        text = self.input.text()
        print(text[:len(text) - 1])
        self.input.setText(text[:len(text) - 1])


app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())

import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.setWindowTitle("Qt Layout example")
        self.setMinimumWidth(500)
        # Create widgets
        self.led = QLineEdit()
        self.led.setPlaceholderText("write your name here")
        self.butt_greet = QPushButton("Say Hello")
        self.butt_close = QPushButton("Close")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.led)
        layout.addWidget(self.butt_greet)
        layout.addWidget(self.butt_close)

        # Set layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.butt_greet.clicked.connect(self.greetings)
        self.butt_close.clicked.connect(self.close)

    # Greets the user
    def greetings(self):
        msg_box = QMessageBox()
        msg_box.setText("Hello %s" % self.led.text())
        msg_box.exec()

        print ("Hello %s" % self.led.text())


if __name__ == '__main__':

    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop

    sys.exit(app.exec_())
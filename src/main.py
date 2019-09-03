import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.setWindowTitle("Qt Layout example")
        self.setMinimumWidth(500)
        # Create widgets
        led = QLineEdit()
        led.setPlaceholderText("write your name here")
        self.led= led

        butt_greet = QPushButton("Say Hello")
        butt_close = QPushButton("Close")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(led)
        layout.addWidget(butt_greet)
        layout.addWidget(butt_close)

        # Set layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        butt_greet.clicked.connect(self.greetings)
        butt_close.clicked.connect(self.close)

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
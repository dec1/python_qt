#!/usr/bin/env python3
import sys
import os
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QPushButton, QCheckBox, \
                            QLabel, QVBoxLayout, QHBoxLayout, QFrame


from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#from process_files import process_files
#from process_files import write_ctb
from ImportGCD_CTB import CorrField

class App(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'Correction file tool'
        self.left = 50
        self.top = 50
        self.width = 300
        self.height = 350
        self.initUI()

        # Members used as temporary variables to handle return values

        self.file_name_default = "corrfile.ctb"
        self.default_path = "V:\\O\\Entwicklung\\SME\\22_Produkte\\03_Scanner\\80_Komponenten_Datenbank\\03_Abstandsringe\\"

        self.corrfield = CorrField();
        self.corrfield.ctb = False
        self.corrfield.gcd = False
        self.corrfield.ucf = False
        self.corrfield.scf = False
        
        self.corrfieldB = CorrField();
        self.corrfieldB.ctb = False
        self.corrfieldB.gcd = False
        self.corrfieldB.ucf = False
        self.corrfieldB.scf = False
        
        self.params = 0



    def doLayout(self):
        self.setMinimumWidth(500)
        self.lay_main = QVBoxLayout();
        self.lay_main.setSpacing(10)

        self.lay_top = QHBoxLayout();

        self.lay_file_butts = QVBoxLayout();
        self.lay_main.addWidget(self.l1)
        self.lay_main.addSpacing(10)

        self.lay_file_butts.addWidget(self.butt_file_par)
        self.lay_file_butts.addWidget(self.butt_file_xli)

        self.lay_cbs= QVBoxLayout();
        self.lay_cbs.addWidget(self.box_gcd)
        self.lay_cbs.addWidget(self.box_scf)
        self.lay_cbs.addWidget(self.box_ucf)
        self.lay_cbs.addWidget(self.box_ctb)

        self.lay_butts = QVBoxLayout();
        self.lay_butts.addWidget(self.butt_process)
        self.lay_butts.addWidget(self.butt_save)

        self.setLayout(self.lay_main)
        self.lay_main.addLayout(self.lay_top)
        self.lay_top.addLayout(self.lay_file_butts)
        self.lay_top.addLayout(self.lay_cbs)
        self.lay_top.addLayout(self.lay_butts)

        self.lay_main.addSpacing(10)
        self.lay_main.addWidget(self.sep)
        self.lay_main.addSpacing(10)

        self.lay_main.addWidget(self.l2)
        self.lay_main.addWidget(self.butt_file_corr_a)
        self.lay_main.addWidget(self.butt_file_corr_b)
        self.lay_main.addWidget(self.butt_analyse_ab)



    def initUI(self):

    ### Defines form and status of window and buttons ###

        #default_path = V:\O\Entwicklung\SME\22_Produkte\03_Scanner+\80_Komponenten_Datenbank\03_Abstandsringe

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.l1 = QLabel('Choose files to generate correction files', self)

        # separator .. looks like horizontal line
        self.sep = QFrame(self)
        self.sep.setFrameShape(QFrame.HLine)
        self.sep.setFixedHeight(1)



        self.l2 = QLabel('Choose correction file to see plot', self)

        self.butt_file_par = QPushButton('Choose file *.par', self)
        self.butt_file_par.clicked.connect(self.on_click_choose_par)

        #button_open_file1.clicked.connect(self.check_files)
        self.butt_file_xli = QPushButton('Choose file *.xli', self)
        self.butt_file_xli.clicked.connect(self.on_click_choose_xli)
        #button_open_file1.clicked.connect(self.check_files)

        self.butt_process = QPushButton('Process files', self)
        # button_start_process.setEnabled(False)
        self.butt_process.clicked.connect(self.on_click_process)

        self.butt_save = QPushButton('Save files', self)
        self.butt_save.setEnabled(False)
        self.butt_save.clicked.connect(self.on_click_save)

    #---------------------------------------------

        self.butt_file_corr_a = QPushButton('Read Corrfile A', self)
        #button_start_process.setEnabled(False)
        self.butt_file_corr_a.clicked.connect(self.on_click_read_corrfile_a)

        self.butt_file_corr_b = QPushButton('Read Corrfile B', self)
        #button_start_process.setEnabled(False)
        self.butt_file_corr_b.clicked.connect(self.on_click_read_corrfile_b)

        self.butt_analyse_ab = QPushButton('Analyse A-B', self)
        #button_start_process.setEnabled(False)
        self.butt_analyse_ab.clicked.connect(self.on_click_analyseAB)



        self.box_ctb = QCheckBox(".ctb",self)
        self.box_ctb.setChecked(True)
        #self.box_ctb.stateChanged.connect(self.clickBox_ctb)
        #self.corrfield.ctb = True

        self.box_gcd = QCheckBox(".gcd",self)
        self.box_gcd.setChecked(True)
        #self.box_gcd.stateChanged.connect(self.clickBox_gcd)
        #self.corrfield.gcd = True

        self.box_ucf = QCheckBox(".ucf",self)
        self.box_ucf.setChecked(True)
        #self.box_ucf.stateChanged.connect(self.clickBox_ucf)
        #self.corrfield.ucf = True

        self.box_scf = QCheckBox(".scf",self)
        self.box_scf.setChecked(True)
        #self.box_ucf.stateChanged.connect(self.clickBox_ucf)
        #self.corrfield.ucf = True

        self.doLayout();
        self.show()

    ### functions to get the filenames through file dialog ###

#    def openFileName_par(self):
#        options = QFileDialog.Options()
#        options |= QFileDialog.DontUseNativeDialog
#        self.corrfield.filename_par, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFile()", "","Par Files (*.par)", options=options)
#        if self.corrfield.filename_par:
#            print(self.corrfield.filename_par)
    def openFileName_par(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        if os.path.exists(str(self.default_path)):
            self.corrfield.filename_par, _ = QFileDialog.getOpenFileNames(self,"Open File (*.par)", self.default_path,"Par Files (*.par)", options=options)
            if self.corrfield.filename_par:
                print(self.corrfield.filename_par)
        else:
            print("Path: ", self.default_path ,"not available")
            self.corrfield.filename_par, _ = QFileDialog.getOpenFileNames(self,"Open File (*.par)", "","Par Files (*.par)", options=options)
            if self.corrfield.filename_par:
                print(self.corrfield.filename_par)

#    def openFileName_xli(self):
#        options = QFileDialog.Options()
#        options |= QFileDialog.DontUseNativeDialog
#        self.corrfield.filename_xli, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFile()", "","XLI Files (*.xli)", options=options)
#        if self.corrfield.filename_xli:
#            print(self.corrfield.filename_xli)
    def openFileName_xli(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        if os.path.exists(self.default_path):
            self.corrfield.filename_xli, _ = QFileDialog.getOpenFileNames(self,"Open File (*.xli)", self.default_path ,"XLI Files (*.xli)", options=options)
            if self.corrfield.filename_xli:
                print(self.corrfield.filename_xli)
        else:
            print("Path: ", self.default_path, "not available")
            self.corrfield.filename_xli, _ = QFileDialog.getOpenFileNames(self,"Open File (*.xli)", "" ,"XLI Files (*.xli)", options=options)
            if self.corrfield.filename_xli:
                print(self.corrfield.filename_xli)


    def saveFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        temp_filename, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",self.file_name_default,"All Files (*);;Text Files (*.txt)", options=options)
        if temp_filename:
            self.corrfield.filename = os.path.splitext(temp_filename)[0]
            print(self.corrfield.filename)

    def readCorrFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.corrfield.filename, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFile()", "","CTB Files (*.ctb);;GCD Files (*.gcd);;UCF Files (*.ucf);;SCF Files (*.scf.txt)", options=options)
        if self.corrfield.filename:
            print(self.corrfield.filename)


    def clickBox_ctb(self, state):
        if state == QtCore.Qt.Checked:
            self.corrfield.ctb = True
            self.button_save_file.setEnabled(False)
            print('CTB Checked')
        else:
            self.corrfield.ctb = False
            if self.corrfield.gcd != True:
                self.button_save_file.setEnabled(False)
            print('CTB Unchecked')

    def clickBox_gcd(self, state):
        if state == QtCore.Qt.Checked:
            self.corrfield.gcd = True
            self.button_save_file.setEnabled(False)
            print('GCD Checked')
        else:
            self.corrfield.gcd = False
            if self.corrfield.ctb != True:
                self.button_save_file.setEnabled(False)
            print('GCD Unchecked')

    def clickBox_ucf(self, state):
        if state == QtCore.Qt.Checked:
            self.corrfield.ucf = True
            self.button_save_file.setEnabled(False)
            print('UCF Checked')
        else:
            self.corrfield.ucf = False
            if self.corrfield.ctb != True:
                self.button_save_file.setEnabled(False)
            print('UCF Unchecked')
            
            
    def clickBox_scf(self, state):
        if state == QtCore.Qt.Checked:
            self.corrfield.scf = True
            self.button_save_file.setEnabled(False)
            print('SCF Checked')
        else:
            self.corrfield.ucf = False
            if self.corrfield.ctb != True:
                self.button_save_file.setEnabled(False)
            print('SCF Unchecked')

    def analyse_check_boxes(self):
        if self.box_ctb.isChecked():
            self.corrfield.ctb = True
            print('CTB Checked')
        else:
            self.corrfield.ctb = False
            print('CTB Unchecked')
        if self.box_gcd.isChecked():
            self.corrfield.gcd = True
            print('GCD Checked')
        else:
            self.corrfield.gcd = False
            print('GCD Unchecked')
        if self.box_ucf.isChecked():
            self.corrfield.ucf = True
            print('UCF Checked')
        else:
            self.corrfield.ucf = False
            print('UCF Unchecked')
        if self.box_scf.isChecked():
            self.corrfield.scf = True
            print('SCF Checked')
        else:
            self.corrfield.scf = False
            print('SCF Unchecked')


# Defines slots (for eventhandling) which call the functions of the window itself of the correctionfile class in file "ImportGCD_CTB"

    @pyqtSlot()
    def on_click_choose_xli(self):
        print('Choose xli file button click')
        self.openFileName_xli()
        #print(self.corrfield.filename_xli)

    def on_click_choose_par(self):
        print('Choose par file button click')
        self.openFileName_par()
        print(self.corrfield)

    def on_click_process(self):
        print('Process Button Click')
        self.analyse_check_boxes()
        #print("".join(self.corrfield.filename_xli))
        #print("".join(self.corrfield.filename_par))
        if self.corrfield.filename_par and self.corrfield.filename_xli:
            if self.corrfield.gcd or self.corrfield.ctb or self.corrfield.ucf or self.corrfield.scf:
                print('processing started')
                self.corrfield.process_XLI_PAR(file_par = "".join(self.corrfield.filename_par), file_zmx = "".join(self.corrfield.filename_xli))
                self.button_save_file.setEnabled(True)
            else:
                print('Error: No type selected')
        else:
            print('Error: File/s not specified')

    def on_click_save(self):
        print('Save button click')
        if self.corrfield.filename_par and self.corrfield.filename_xli:
            if self.corrfield.gcd or self.corrfield.ctb or self.corrfield.ucf or self.corrfield.scf:
                self.saveFile()
                self.corrfield.save_files(filename = "".join(self.corrfield.filename), safe_ctb = self.corrfield.ctb, safe_gcd = self.corrfield.gcd, safe_ucf = self.corrfield.ucf, safe_scf = self.corrfield.scf)
                self.corrfield.create_readme()
        #write_ctb(self.file_name2, self.m_aXnp, self.m_aYnp, self.wavelength, self.max_mechX, self.max_mechY, self.K)

    def on_click_read_corrfile_a(self):
        print('Read Corrfile A button click')
        self.readCorrFile()
        self.corrfield.read_files(filename = "".join(self.corrfield.filename))
        
    def on_click_read_corrfile_b(self):
        print('Read Corrfile B button click')
        self.readCorrFile()
        self.corrfieldB.read_files(filename = "".join(self.corrfield.filename))

        
    def on_click_analyseAB(self):
        print('Read Analyse button click')
        # prüfen das 
        #self.corrfield.analyseAB(filename = "".join(self.corrfield.filename))
        
        self.corrfieldC = CorrField()
        self.corrfieldC.analyseAB(self.corrfield, self.corrfieldB)
        
        #self.readCorrFile()
        #self.corrfield.read_files(filename = "".join(self.corrfield.filename))

if __name__ == '__main__':


    app = QApplication(sys.argv)

    ex = App()
    sys.exit(app.exec_())

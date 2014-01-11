# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/MainWindow.ui'
#
# Created: Sat Jan 11 04:50:28 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 297)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/tuxcut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cboxProtection = QtGui.QCheckBox(self.centralwidget)
        self.cboxProtection.setMinimumSize(QtCore.QSize(101, 23))
        self.cboxProtection.setMaximumSize(QtCore.QSize(200, 23))
        self.cboxProtection.setChecked(True)
        self.cboxProtection.setObjectName("cboxProtection")
        self.horizontalLayout.addWidget(self.cboxProtection)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboIfaces = QtGui.QComboBox(self.centralwidget)
        self.comboIfaces.setObjectName("comboIfaces")
        self.horizontalLayout.addWidget(self.comboIfaces)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_changemac = QtGui.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/mac.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_changemac.setIcon(icon1)
        self.btn_changemac.setIconSize(QtCore.QSize(20, 20))
        self.btn_changemac.setObjectName("btn_changemac")
        self.horizontalLayout_2.addWidget(self.btn_changemac)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setMargin(1)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lbl_mac = QtGui.QLabel(self.centralwidget)
        self.lbl_mac.setObjectName("lbl_mac")
        self.horizontalLayout_2.addWidget(self.lbl_mac)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tblHosts = QtGui.QTableWidget(self.centralwidget)
        self.tblHosts.setLineWidth(1)
        self.tblHosts.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tblHosts.setShowGrid(False)
        self.tblHosts.setObjectName("tblHosts")
        self.tblHosts.setColumnCount(3)
        self.tblHosts.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblHosts.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblHosts.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tblHosts.setHorizontalHeaderItem(2, item)
        self.tblHosts.horizontalHeader().setVisible(True)
        self.tblHosts.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tblHosts)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnRefresh = QtGui.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefresh.setIcon(icon2)
        self.btnRefresh.setIconSize(QtCore.QSize(20, 20))
        self.btnRefresh.setObjectName("btnRefresh")
        self.verticalLayout.addWidget(self.btnRefresh)
        self.btnCut = QtGui.QPushButton(self.centralwidget)
        self.btnCut.setEnabled(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCut.setIcon(icon3)
        self.btnCut.setIconSize(QtCore.QSize(20, 20))
        self.btnCut.setObjectName("btnCut")
        self.verticalLayout.addWidget(self.btnCut)
        self.btnResume = QtGui.QPushButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/resume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnResume.setIcon(icon4)
        self.btnResume.setIconSize(QtCore.QSize(20, 20))
        self.btnResume.setObjectName("btnResume")
        self.verticalLayout.addWidget(self.btnResume)
        self.btnResumeAll = QtGui.QPushButton(self.centralwidget)
        self.btnResumeAll.setIcon(icon4)
        self.btnResumeAll.setIconSize(QtCore.QSize(20, 20))
        self.btnResumeAll.setObjectName("btnResumeAll")
        self.verticalLayout.addWidget(self.btnResumeAll)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.btnAbout = QtGui.QPushButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAbout.setIcon(icon5)
        self.btnAbout.setIconSize(QtCore.QSize(20, 20))
        self.btnAbout.setObjectName("btnAbout")
        self.verticalLayout.addWidget(self.btnAbout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 644, 20))
        self.menuBar.setObjectName("menuBar")
        self.menu_File = QtGui.QMenu(self.menuBar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtGui.QMenu(self.menuBar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Language = QtGui.QMenu(self.menu_Edit)
        self.menu_Language.setObjectName("menu_Language")
        self.menu_Help = QtGui.QMenu(self.menuBar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Utilities = QtGui.QMenu(self.menuBar)
        self.menu_Utilities.setObjectName("menu_Utilities")
        self.menuSpeed_Limiter = QtGui.QMenu(self.menu_Utilities)
        self.menuSpeed_Limiter.setObjectName("menuSpeed_Limiter")
        MainWindow.setMenuBar(self.menuBar)
        self.actionEnglish = QtGui.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.actionQuit = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/images/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon6)
        self.actionQuit.setObjectName("actionQuit")
        self.menu_File.addAction(self.actionQuit)
        self.menu_Language.addAction(self.actionEnglish)
        self.menu_Edit.addAction(self.menu_Language.menuAction())
        self.menu_Utilities.addAction(self.menuSpeed_Limiter.menuAction())
        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menu_Utilities.menuAction())
        self.menuBar.addAction(self.menu_Edit.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "TuxCut-5.0", None, QtGui.QApplication.UnicodeUTF8))
        self.cboxProtection.setText(QtGui.QApplication.translate("MainWindow", "Protection Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Network Interfaces :", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_changemac.setText(QtGui.QApplication.translate("MainWindow", "Change MAC", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Current MAC Address :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_mac.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tblHosts.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "IP Address", None, QtGui.QApplication.UnicodeUTF8))
        self.tblHosts.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "MAC Address", None, QtGui.QApplication.UnicodeUTF8))
        self.tblHosts.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Hostname", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefresh.setText(QtGui.QApplication.translate("MainWindow", "Refresh ", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.btnResume.setText(QtGui.QApplication.translate("MainWindow", "Resume", None, QtGui.QApplication.UnicodeUTF8))
        self.btnResumeAll.setText(QtGui.QApplication.translate("MainWindow", "Resume All", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Language.setTitle(QtGui.QApplication.translate("MainWindow", "&Language", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Utilities.setTitle(QtGui.QApplication.translate("MainWindow", "&Utilities", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSpeed_Limiter.setTitle(QtGui.QApplication.translate("MainWindow", "Speed Limiter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnglish.setText(QtGui.QApplication.translate("MainWindow", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

import images_rc

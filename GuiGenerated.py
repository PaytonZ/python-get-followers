# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtDesignerGUI/GUI.ui'
#
# Created: Thu Jul 10 20:25:12 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(747, 612)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabManager = QtGui.QTabWidget(self.centralwidget)
        self.tabManager.setGeometry(QtCore.QRect(9, 9, 721, 531))
        self.tabManager.setUsesScrollButtons(False)
        self.tabManager.setObjectName("tabManager")
        self.accountManagerTab = QtGui.QWidget()
        self.accountManagerTab.setObjectName("accountManagerTab")
        self.tabAccountManager = QtGui.QTabWidget(self.accountManagerTab)
        self.tabAccountManager.setGeometry(QtCore.QRect(10, 10, 691, 441))
        self.tabAccountManager.setTabPosition(QtGui.QTabWidget.West)
        self.tabAccountManager.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabAccountManager.setIconSize(QtCore.QSize(64, 64))
        self.tabAccountManager.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabAccountManager.setObjectName("tabAccountManager")
        self.clientManagerTab = QtGui.QWidget()
        self.clientManagerTab.setObjectName("clientManagerTab")
        self.clientLabel = QtGui.QLabel(self.clientManagerTab)
        self.clientLabel.setGeometry(QtCore.QRect(130, 50, 111, 16))
        self.clientLabel.setObjectName("clientLabel")
        self.clientNameText = QtGui.QLineEdit(self.clientManagerTab)
        self.clientNameText.setGeometry(QtCore.QRect(250, 50, 241, 21))
        self.clientNameText.setObjectName("clientNameText")
        self.groupBox = QtGui.QGroupBox(self.clientManagerTab)
        self.groupBox.setGeometry(QtCore.QRect(90, 100, 441, 251))
        self.groupBox.setToolTip("")
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 411, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.twitterText = QtGui.QLineEdit(self.formLayoutWidget)
        self.twitterText.setEnabled(False)
        self.twitterText.setObjectName("twitterText")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.twitterText)
        self.twitterLabel = QtGui.QLabel(self.formLayoutWidget)
        self.twitterLabel.setObjectName("twitterLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.twitterLabel)
        self.youtubeLabel = QtGui.QLabel(self.formLayoutWidget)
        self.youtubeLabel.setObjectName("youtubeLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.youtubeLabel)
        self.youtubeText = QtGui.QLineEdit(self.formLayoutWidget)
        self.youtubeText.setEnabled(False)
        self.youtubeText.setObjectName("youtubeText")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.youtubeText)
        self.linkedinLabel = QtGui.QLabel(self.formLayoutWidget)
        self.linkedinLabel.setObjectName("linkedinLabel")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.linkedinLabel)
        self.linkedinText = QtGui.QLineEdit(self.formLayoutWidget)
        self.linkedinText.setEnabled(False)
        self.linkedinText.setObjectName("linkedinText")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.linkedinText)
        self.facebookLabel = QtGui.QLabel(self.formLayoutWidget)
        self.facebookLabel.setObjectName("facebookLabel")
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.facebookLabel)
        self.facebookText = QtGui.QLineEdit(self.formLayoutWidget)
        self.facebookText.setEnabled(False)
        self.facebookText.setObjectName("facebookText")
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.facebookText)
        self.googleLabel = QtGui.QLabel(self.formLayoutWidget)
        self.googleLabel.setObjectName("googleLabel")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.googleLabel)
        self.googleText = QtGui.QLineEdit(self.formLayoutWidget)
        self.googleText.setEnabled(False)
        self.googleText.setObjectName("googleText")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.googleText)
        self.pinterestLabel = QtGui.QLabel(self.formLayoutWidget)
        self.pinterestLabel.setObjectName("pinterestLabel")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.pinterestLabel)
        self.pinterestText = QtGui.QLineEdit(self.formLayoutWidget)
        self.pinterestText.setEnabled(False)
        self.pinterestText.setObjectName("pinterestText")
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.pinterestText)
        self.horizontalLayoutWidget = QtGui.QWidget(self.clientManagerTab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 360, 441, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelBt = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.cancelBt.setCursor(QtCore.Qt.PointingHandCursor)
        self.cancelBt.setObjectName("cancelBt")
        self.horizontalLayout.addWidget(self.cancelBt)
        self.saveBt = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.saveBt.setEnabled(False)
        self.saveBt.setCursor(QtCore.Qt.PointingHandCursor)
        self.saveBt.setObjectName("saveBt")
        self.horizontalLayout.addWidget(self.saveBt)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/client.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabAccountManager.addTab(self.clientManagerTab, icon, "")
        self.socialManagerTab = QtGui.QWidget()
        self.socialManagerTab.setObjectName("socialManagerTab")
        self.clientListView = QtGui.QListView(self.socialManagerTab)
        self.clientListView.setGeometry(QtCore.QRect(10, 30, 221, 391))
        self.clientListView.setObjectName("clientListView")
        self.clientListLabel = QtGui.QLabel(self.socialManagerTab)
        self.clientListLabel.setGeometry(QtCore.QRect(10, 10, 62, 16))
        self.clientListLabel.setObjectName("clientListLabel")
        self.soccialAccountGroup = QtGui.QGroupBox(self.socialManagerTab)
        self.soccialAccountGroup.setGeometry(QtCore.QRect(240, 10, 361, 411))
        self.soccialAccountGroup.setObjectName("soccialAccountGroup")
        self.editBt = QtGui.QPushButton(self.soccialAccountGroup)
        self.editBt.setGeometry(QtCore.QRect(30, 370, 114, 32))
        self.editBt.setObjectName("editBt")
        self.removeBt = QtGui.QPushButton(self.soccialAccountGroup)
        self.removeBt.setEnabled(False)
        self.removeBt.setGeometry(QtCore.QRect(170, 370, 141, 32))
        self.removeBt.setObjectName("removeBt")
        self.gridLayoutWidget = QtGui.QWidget(self.soccialAccountGroup)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 341, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.linkedinCk = QtGui.QCheckBox(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linkedinCk.sizePolicy().hasHeightForWidth())
        self.linkedinCk.setSizePolicy(sizePolicy)
        self.linkedinCk.setText("")
        self.linkedinCk.setObjectName("linkedinCk")
        self.gridLayout.addWidget(self.linkedinCk, 3, 0, 1, 1)
        self.googleLabel_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.googleLabel_2.setObjectName("googleLabel_2")
        self.gridLayout.addWidget(self.googleLabel_2, 5, 1, 1, 1)
        self.facebookLabel_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.facebookLabel_2.setObjectName("facebookLabel_2")
        self.gridLayout.addWidget(self.facebookLabel_2, 2, 1, 1, 1)
        self.youtubeCk = QtGui.QCheckBox(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.youtubeCk.sizePolicy().hasHeightForWidth())
        self.youtubeCk.setSizePolicy(sizePolicy)
        self.youtubeCk.setText("")
        self.youtubeCk.setObjectName("youtubeCk")
        self.gridLayout.addWidget(self.youtubeCk, 4, 0, 1, 1)
        self.youtubeText_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.youtubeText_2.setEnabled(False)
        self.youtubeText_2.setObjectName("youtubeText_2")
        self.gridLayout.addWidget(self.youtubeText_2, 4, 2, 1, 1)
        self.linkedinText_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.linkedinText_2.setEnabled(False)
        self.linkedinText_2.setObjectName("linkedinText_2")
        self.gridLayout.addWidget(self.linkedinText_2, 3, 2, 1, 1)
        self.pinterestLabel_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.pinterestLabel_2.setObjectName("pinterestLabel_2")
        self.gridLayout.addWidget(self.pinterestLabel_2, 9, 1, 1, 1)
        self.pinterestCk = QtGui.QCheckBox(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pinterestCk.sizePolicy().hasHeightForWidth())
        self.pinterestCk.setSizePolicy(sizePolicy)
        self.pinterestCk.setText("")
        self.pinterestCk.setObjectName("pinterestCk")
        self.gridLayout.addWidget(self.pinterestCk, 9, 0, 1, 1)
        self.youtubeLabel_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.youtubeLabel_2.setObjectName("youtubeLabel_2")
        self.gridLayout.addWidget(self.youtubeLabel_2, 4, 1, 1, 1)
        self.twitterLabel_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.twitterLabel_2.setObjectName("twitterLabel_2")
        self.gridLayout.addWidget(self.twitterLabel_2, 0, 1, 1, 1)
        self.twitterText_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.twitterText_2.setEnabled(False)
        self.twitterText_2.setObjectName("twitterText_2")
        self.gridLayout.addWidget(self.twitterText_2, 0, 2, 1, 1)
        self.facebookText_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.facebookText_2.setEnabled(False)
        self.facebookText_2.setObjectName("facebookText_2")
        self.gridLayout.addWidget(self.facebookText_2, 2, 2, 1, 1)
        self.googleText_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.googleText_2.setEnabled(False)
        self.googleText_2.setObjectName("googleText_2")
        self.gridLayout.addWidget(self.googleText_2, 5, 2, 1, 1)
        self.pinterestText_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.pinterestText_2.setEnabled(False)
        self.pinterestText_2.setObjectName("pinterestText_2")
        self.gridLayout.addWidget(self.pinterestText_2, 9, 2, 1, 1)
        self.facebookCk = QtGui.QCheckBox(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.facebookCk.sizePolicy().hasHeightForWidth())
        self.facebookCk.setSizePolicy(sizePolicy)
        self.facebookCk.setText("")
        self.facebookCk.setObjectName("facebookCk")
        self.gridLayout.addWidget(self.facebookCk, 2, 0, 1, 1)
        self.googleCk = QtGui.QCheckBox(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.googleCk.sizePolicy().hasHeightForWidth())
        self.googleCk.setSizePolicy(sizePolicy)
        self.googleCk.setText("")
        self.googleCk.setObjectName("googleCk")
        self.gridLayout.addWidget(self.googleCk, 5, 0, 1, 1)
        self.linkedinLabel_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.linkedinLabel_2.setObjectName("linkedinLabel_2")
        self.gridLayout.addWidget(self.linkedinLabel_2, 3, 1, 1, 1)
        self.twitterCk = QtGui.QCheckBox(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twitterCk.sizePolicy().hasHeightForWidth())
        self.twitterCk.setSizePolicy(sizePolicy)
        self.twitterCk.setObjectName("twitterCk")
        self.gridLayout.addWidget(self.twitterCk, 0, 0, 1, 1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/social.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabAccountManager.addTab(self.socialManagerTab, icon1, "")
        self.tabManager.addTab(self.accountManagerTab, "")
        self.followersGetter = QtGui.QWidget()
        self.followersGetter.setObjectName("followersGetter")
        self.tableView = QtGui.QTableView(self.followersGetter)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 691, 411))
        self.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableView.setSortingEnabled(False)
        self.tableView.setObjectName("tableView")
        self.fetchBt = QtGui.QPushButton(self.followersGetter)
        self.fetchBt.setGeometry(QtCore.QRect(210, 430, 291, 61))
        self.fetchBt.setObjectName("fetchBt")
        self.tabManager.addTab(self.followersGetter, "")
        self.versionGUI = QtGui.QLabel(self.centralwidget)
        self.versionGUI.setGeometry(QtCore.QRect(10, 550, 81, 16))
        self.versionGUI.setObjectName("versionGUI")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 747, 22))
        self.menubar.setObjectName("menubar")
        self.menuArchive = QtGui.QMenu(self.menubar)
        self.menuArchive.setObjectName("menuArchive")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_accounts_data_file = QtGui.QAction(MainWindow)
        self.actionOpen_accounts_data_file.setObjectName("actionOpen_accounts_data_file")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDevelopers = QtGui.QAction(MainWindow)
        self.actionDevelopers.setObjectName("actionDevelopers")
        self.menuArchive.addAction(self.actionOpen_accounts_data_file)
        self.menuArchive.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionDevelopers)
        self.menubar.addAction(self.menuArchive.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabManager.setCurrentIndex(0)
        self.tabAccountManager.setCurrentIndex(1)
        QtCore.QObject.connect(self.cancelBt, QtCore.SIGNAL("clicked()"), self.pinterestText.clear)
        QtCore.QObject.connect(self.cancelBt, QtCore.SIGNAL("clicked()"), self.googleText.clear)
        QtCore.QObject.connect(self.cancelBt, QtCore.SIGNAL("clicked()"), self.facebookText.clear)
        QtCore.QObject.connect(self.cancelBt, QtCore.SIGNAL("clicked()"), self.linkedinText.clear)
        QtCore.QObject.connect(self.cancelBt, QtCore.SIGNAL("clicked()"), self.youtubeText.clear)
        QtCore.QObject.connect(self.cancelBt, QtCore.SIGNAL("clicked()"), self.twitterText.clear)
        QtCore.QObject.connect(self.cancelBt, QtCore.SIGNAL("clicked()"), self.clientNameText.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Social Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.clientLabel.setText(QtGui.QApplication.translate("MainWindow", "Client name:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Accounts", None, QtGui.QApplication.UnicodeUTF8))
        self.twitterLabel.setText(QtGui.QApplication.translate("MainWindow", "Twitter account:", None, QtGui.QApplication.UnicodeUTF8))
        self.youtubeLabel.setText(QtGui.QApplication.translate("MainWindow", "Youtube account:", None, QtGui.QApplication.UnicodeUTF8))
        self.linkedinLabel.setText(QtGui.QApplication.translate("MainWindow", "Linkedin account:", None, QtGui.QApplication.UnicodeUTF8))
        self.facebookLabel.setText(QtGui.QApplication.translate("MainWindow", "Facebook account:", None, QtGui.QApplication.UnicodeUTF8))
        self.googleLabel.setText(QtGui.QApplication.translate("MainWindow", "Google + account:", None, QtGui.QApplication.UnicodeUTF8))
        self.pinterestLabel.setText(QtGui.QApplication.translate("MainWindow", "Pinterest account:", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBt.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.saveBt.setText(QtGui.QApplication.translate("MainWindow", "Save client and accounts", None, QtGui.QApplication.UnicodeUTF8))
        self.clientListLabel.setText(QtGui.QApplication.translate("MainWindow", "Client list", None, QtGui.QApplication.UnicodeUTF8))
        self.soccialAccountGroup.setTitle(QtGui.QApplication.translate("MainWindow", "Social account data", None, QtGui.QApplication.UnicodeUTF8))
        self.editBt.setText(QtGui.QApplication.translate("MainWindow", "Edit info", None, QtGui.QApplication.UnicodeUTF8))
        self.removeBt.setText(QtGui.QApplication.translate("MainWindow", "Remove accounts", None, QtGui.QApplication.UnicodeUTF8))
        self.googleLabel_2.setText(QtGui.QApplication.translate("MainWindow", "Google + account:", None, QtGui.QApplication.UnicodeUTF8))
        self.facebookLabel_2.setText(QtGui.QApplication.translate("MainWindow", "Facebook account:", None, QtGui.QApplication.UnicodeUTF8))
        self.pinterestLabel_2.setText(QtGui.QApplication.translate("MainWindow", "Pinterest account:", None, QtGui.QApplication.UnicodeUTF8))
        self.youtubeLabel_2.setText(QtGui.QApplication.translate("MainWindow", "Youtube account:", None, QtGui.QApplication.UnicodeUTF8))
        self.twitterLabel_2.setText(QtGui.QApplication.translate("MainWindow", "Twitter account:", None, QtGui.QApplication.UnicodeUTF8))
        self.linkedinLabel_2.setText(QtGui.QApplication.translate("MainWindow", "Linkedin account:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabManager.setTabText(self.tabManager.indexOf(self.accountManagerTab), QtGui.QApplication.translate("MainWindow", "Account Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.fetchBt.setText(QtGui.QApplication.translate("MainWindow", "Fectch", None, QtGui.QApplication.UnicodeUTF8))
        self.tabManager.setTabText(self.tabManager.indexOf(self.followersGetter), QtGui.QApplication.translate("MainWindow", "Followers Getter", None, QtGui.QApplication.UnicodeUTF8))
        self.versionGUI.setText(QtGui.QApplication.translate("MainWindow", "Version 0.3", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchive.setTitle(QtGui.QApplication.translate("MainWindow", "Archive", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_accounts_data_file.setText(QtGui.QApplication.translate("MainWindow", "Open accounts data file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDevelopers.setText(QtGui.QApplication.translate("MainWindow", "Developers", None, QtGui.QApplication.UnicodeUTF8))

import images_rc

from PyQt6.QtCore import QMetaObject
# from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QTableWidget, QTableWidgetItem, QTabWidget, QVBoxLayout, QWidget



class Ui_MainWindow(object):
    def getSizePolicy(self, obj):
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(obj.sizePolicy().hasHeightForWidth())
        return sizePolicy

    def setupUi(self, MainWindow):
        # Setup of main windows
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.setSizePolicy(self.getSizePolicy(MainWindow))
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setSizePolicy(self.getSizePolicy(self.centralwidget))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.tabWidget = QTabWidget(parent=self.centralwidget)
        self.tabWidget.setEnabled(True)
        # self.tabWidget.setSizePolicy(self.getSizePolicy(MainWindow))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)

        self.tabHeaderInfo = self.getTabHeaderInfo()
        self.tabWidget.addTab(self.tabHeaderInfo,"Header Info")
        self.tabWidget.setCurrentIndex(0)

        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        # # self.menubar = QMenuBar(parent=MainWindow)
        # # self.menubar.setGeometry(QRect(0, 0, 875, 23))
        # # self.menubar.setObjectName("menubar")
        # # MainWindow.setMenuBar(self.menubar)
        # # self.statusbar = QStatusBar(parent=MainWindow)
        # # self.statusbar.setObjectName("statusbar")
        # # MainWindow.setStatusBar(self.statusbar)

        QMetaObject.connectSlotsByName(MainWindow)

    def getTabHeaderInfo(self):
        # Tab 1
        p = QWidget()
        p.setObjectName("tabHeaderInfo")
        vl = QVBoxLayout(p)
        vl.setObjectName("tabHeaderInfoVL")
        self.t1tableHex = self.getHexTable(p)
        self.t1tableHex.setObjectName('hexTableHeaders')
        vl.addWidget(self.t1tableHex)

        self.t1lFirstChunk = QLabel("First Chunk Number: ")
        self.t1lLastChunk = QLabel("Last Chunk Number: ")
        self.t1lVerNum = QLabel("Version Number: ")
        self.t1lNumChunks = QLabel("Number of Chunks: ")
        self.t1lCheckSum = QLabel("Header Checksum: ")
        self.tl1CheckSumValid = QLabel("[UKNKNOWN]")

        h1 = QHBoxLayout()
        h1.addWidget(self.t1lFirstChunk)
        h1.addWidget(self.t1lLastChunk)
        vl.addLayout(h1)

        h2 = QHBoxLayout()
        h2.addWidget(self.t1lVerNum)
        h2.addWidget(self.t1lNumChunks)
        vl.addLayout(h2)

        h3 = QHBoxLayout()
        h3.addWidget(self.t1lCheckSum)
        h3.addWidget(self.tl1CheckSumValid)
        vl.addLayout(h3)

        return p

    def getHexTable(self, p):
        hexTable = QTableWidget(parent=p)
        k = list("0123456789ABCDEF")
        # hexTable.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # hexTable.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # hexTable.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        # hexTable.setAutoScrollMargin(15)
        # hexTable.setWordWrap(False)
        # hexTable.setCornerButtonEnabled(False)
        # hexTable.horizontalHeader().setVisible(True)
        # hexTable.horizontalHeader().setDefaultSectionSize(25)
        for i in range(18):
            hexTable.insertColumn(i)
            item = QTableWidgetItem()
            if i == 0:
                item.setText("Address")
                hexTable.setColumnWidth(i, 100)
            elif i == 17:
                item.setText("ASCII")
                hexTable.setColumnWidth(i, 200)

            else:
                item.setText(k[i-1])
                hexTable.setColumnWidth(i, 20)
            hexTable.setHorizontalHeaderItem(i, item)
        return hexTable
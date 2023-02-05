from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from evtx.evtx import EvtxFile
from windows.ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # test code - open evtx file
        e = EvtxFile('evtx-sample.evtx')

        #Header Tab
        tabHeader = self.findChild(QWidget, name="tabHeaderInfo")
        self.populateHexTable(self.t1tableHex, e.header.h)
        self.t1lFirstChunk.setText("First Chunk Number: %d" % e.header.first_chunk_number)
        self.t1lLastChunk.setText("Last Chunk Number: %d" % e.header.last_chunk_number)
        self.t1lVerNum.setText("Version Number: %d.%d" % (e.header.major_format_version, e.header.minor_format_version))
        self.t1lNumChunks.setText("Number of Chunks: %d" % e.header.number_of_chunks)
        self.t1lCheckSum.setText("Header CheckSum: %s" % hex(e.header.header_checksum))
        self.tl1CheckSumValid.setText(["[VALID]" if e.header.checksum_valid else "[INVALID]"][0])


    def populateHexTable(self, table, header):
        table.setRowCount(256)
        outstr = ""
        for i in range(len(header)):
            item = QTableWidgetItem(f'{header[i]:x}')
            # item.setFont('Courier 12')
            table.setItem(i//16, (i % 16) + 1, item)
            if header[i] < 45:
                outstr += "."
            else:
                outstr +=chr(header[i])
            if i % 16 == 0:
                table.setItem(i//16, 0, QTableWidgetItem(f'{i:x}'))
            elif i % 16 == 15:
                table.setItem(i//16, 17, QTableWidgetItem(outstr))
                outstr = ""
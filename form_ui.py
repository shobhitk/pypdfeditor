# Form implementation generated from reading ui file 'c:\GitHub\pypdfeditor\form.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_pypdfeditor(object):
    def setupUi(self, pypdfeditor):
        pypdfeditor.setObjectName("pypdfeditor")
        pypdfeditor.setEnabled(True)
        pypdfeditor.resize(882, 288)
        pypdfeditor.setAutoFillBackground(False)
        pypdfeditor.setStyleSheet("QToolTip\n"
"{\n"
"     color: #b1b1b1;\n"
"     border: 1px solid black;\n"
"     background-color:rgb(42,42,42);\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 190;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    color: #b1b1b1;\n"
"    min-height: 1px;\n"
"    background-color: rgba(50,50,50,0);\n"
"}\n"
"\n"
"QListWidget:item:hover\n"
"{\n"
"    background-color: rgb(50,60,74);\n"
"}\n"
"\n"
"QListWidget:item:selected\n"
"{\n"
"    background-color: rgb(70,80,94);\n"
"    color: #FFFFFF;\n"
"    border: 2px solid rgb(255,255,255);\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:hover\n"
"{\n"
"    color: #48628e;\n"
"}\n"
"\n"
"\n"
"QWidget:item\n"
"{\n"
"    alternate-background-color: \'#2a2b2c\';\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #48628e;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: #48628e;\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"    padding: 1px 2px 1px 2px;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    background-color: #48628e;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    /*background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #434343, stop: 1 #363636);*/\n"
"    background-color: transparent ;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QLineEdit:!enabled {\n"
"    color: #B1B1B1;\n"
"    background-color: transparent ;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: #b4b4b4;\n"
"    border: 1px solid #2a2a2a;\n"
"    border-radius: 9px;\n"
"    padding: 5px;\n"
"    background: #292929;\n"
"    min-width: 12px;\n"
"    min-height: 12px;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    alternate-background-color: \'#2a2b2c\';\n"
"    background-color: transparent;\n"
"    border: 0px;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"    /* font-weight: bold; */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border : 1px solid #3c5176;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #FFFFFF;\n"
"    border : 2px solid #48628e;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #3d3d3d;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 1px solid #2a2a2a;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    background: #292929;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/*QPushButton:!enabled {\n"
"    border : 1px solid #3c5176;\n"
"}*/\n"
"\n"
"QPushButton:hover {\n"
"    border : 2px solid #48628e;\n"
"    padding: 0px;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    border: 1px solid #2a2a2a;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    background: #292929;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/*QPushButton:!enabled {\n"
"    border : 1px solid #3c5176;\n"
"}*/\n"
"\n"
"QPushButton:hover {\n"
"    border : 2px solid #48628e;\n"
"    padding: 0px;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #3d3d3d;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    border: 1px solid #2a2a2a;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    background: #292929;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QPushButton:!enabled {\n"
"    border : 1px solid #3c5176;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border : 2px solid #48628e;\n"
"    padding: 0px;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #3d3d3d;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    background-color: rgb(36,36,36);\n"
"    border: 1px solid #1e1e1e;\n"
"}\n"
"\n"
"QComboBox:item\n"
"{\n"
"    background-color: transparent;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QListView\n"
"{\n"
"    outline: 0;\n"
"    background-color: #2D2D2D;\n"
"}\n"
"\n"
"QComboBox:hover\n"
"{\n"
"    border: 2px solid #48628e;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    selection-background-color: #48628e;\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: rgb(35,35,35);\n"
"    border-left-style: solid;\n"
"    background-color: rgb(93,93,93);\n"
" }\n"
"\n"
" QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"    image: url(S:/outfit/developers/roberttomcik/FFXPipeline/FFX/universal/sceneManager/themes/icons/dropdown-arrow.png);\n"
"    width: 16px;\n"
"    height: 14px;\n"
"}\n"
"\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid #48628e;\n"
"}\n"
"\n"
"\n"
"QTextEdit\n"
"{\n"
"    border: 2px solid rgb(96,96,96);\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: #444444;\n"
"    border-right: 1px solid #2c2c2c;\n"
"    border-left: 0px;\n"
"    border-top: 0px;\n"
"    border-bottom: 0px;\n"
"}\n"
"\n"
"\n"
"QSpinBox\n"
"{\n"
"    background-color: transparent;\n"
"    border: 1px solid #1e1e1e;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 0px; /* spacing between items in the tool bar */\n"
"    border: 1px solid #242424;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 3px;\n"
"    background-color: #2b2b2b;\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    spacing: 0px; /* spacing between items in the tool bar */\n"
"    background-color:  transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    border: 1px;\n"
"    border-color: #0099ff;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #111111;\n"
"    border:0;\n"
"    background-color: #111111;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: 0px;\n"
"    font-size:10pt;\n"
"    height: 18px;\n"
"    min-width: 102;\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-bottom: 2px solid qlineargradient(\n"
"        x1:0     y1:0,\n"
"        x2:1     y2:0,\n"
"        stop:0   transparent,\n"
"        stop:.1  transparent,\n"
"        stop:.11 #48628e,\n"
"        stop:.9  #48628e,\n"
"        stop:.91 transparent,\n"
"        stop:1   transparent\n"
"        );\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 0px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 0px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    height: 22px;\n"
"    border: 0px solid #1e1e1e;;\n"
"    border-radius: 2px;\n"
"    text-align: center;\n"
"    background-color: transparent\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #48628e;\n"
"    width: 2.15px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom: 0px;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 1;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
"    margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    margin-bottom: 0px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    color: #f9f9f9;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    border-top: 2px solid #48628e;\n"
"    padding-bottom: 2px;\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QRadioButton{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: rgba(50,50,50,0);\n"
"    border: 1px solid #48628e;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #48628e,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox\n"
"{\n"
"    color: rgb(240,240,240)\n"
"}\n"
"\n"
"QRadioButton::indicator:hover\n"
"{\n"
"    border: 1px solid #6889c1;\n"
"}\n"
"\n"
"QStatusBar {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: none;\n"
"}\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    border-radius: 4px;\n"
"    border: 1px solid #3A3939;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    height: 15px;\n"
"    margin: 0px 11px 0px 11px;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 6px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #302F2F, stop: 1 #484846);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #605F5F, stop: 1 #787876);\n"
"    min-width: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: QLinearGradient( x1: 1, y1: 0, x2: 0, y2: 0, stop: 0 #302F2F, stop: 1 #484846);\n"
"    width: 12px;\n"
"    margin: 11px 0 11px 0;\n"
"    border: 1px solid #3A3939;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: QLinearGradient( x1: 1, y1: 0, x2: 0, y2: 0, stop: 0 #101010, stop: 1 #262626);\n"
"    min-height: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"{\n"
"\n"
"    border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"QListWidget\n"
"{\n"
"    background-color: rgba(58, 58, 58, 255);\n"
"    alternate-background-color: rgb(36,46,60);\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QTableWidget\n"
"{\n"
"    background-color: #242424;\n"
"    alternate-background-color: #2c2c2c;\n"
"    border: 0px solid #3A3939;\n"
"    selection-background-color: grey;\n"
"}\n"
"\n"
"QTableView\n"
"{\n"
"    background-color: rgb(36,36,36);\n"
"    outline: 0;\n"
"}\n"
"\n"
"QListWidget::item\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QToolBar\n"
"{\n"
"    background-color: transparent ;\n"
"    color: transparent ;\n"
"}\n"
"\n"
"QToolButton \n"
"{\n"
"    border: 1px solid #2a2a2a;\n"
"    border-radius: 3px;\n"
"    padding: 5px;\n"
"    background: #292929;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QToolButton:hover\n"
"{\n"
"    color: #5d81bd;\n"
"}\n"
"\n"
"QToolButton::menu-indicator\n"
"{\n"
"    image: none;\n"
"}\n"
"\n"
"QSlider {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 0px;\n"
"    height: 2px;\n"
"    background: #6b6b6b;\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #d0d0d0;\n"
"    width: 8px;\n"
"    margin: -3px 0;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSplitter::handle {\n"
"    border: 1px solid #333333;\n"
"    height: 2px;\n"
"    background-color: #101010;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSplitter::handle:pressed {\n"
"    background-color: #6187ac;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    width: 22;\n"
"    height: 22;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: transparent;\n"
"    border: none;\n"
"    width: 22;\n"
"    height: 22;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background: transparent;\n"
"    border: none;\n"
"    width: 22;\n"
"    height: 22;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    width: 22;\n"
"    height: 22;\n"
"}\n"
"\n"
"QTreeWidget\n"
"{\n"
"    background-color: #151515;\n"
"    alternate-background-color: #2a2a2a;\n"
"    border: 0px;\n"
"}\n"
"\n"
"/*QTreeWidget::item {\n"
"    border: 1px solid #8f8f8f;\n"
"    padding: 25px;\n"     
"    max-height: 24px;\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    background: #2b2b2b;\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    color: #ececec;\n"
"    background: #303c50;\n"
"}*/\n"
"QFrame {\n"
"    background-color: #151515;\n"
"    /*border: 1px solid #4f4f4f;*/\n"
"    /*border-radius: 3px;*/\n"
"}\n"
"\n"
"QFrame {\n"
"    border: 1px solid #4f4f4f;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(pypdfeditor)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.main_layout = QtWidgets.QGridLayout()
        self.main_layout.setSpacing(3)
        self.main_layout.setObjectName("main_layout")
        self.output_frame = QtWidgets.QFrame(parent=pypdfeditor)
        self.output_frame.setMinimumSize(QtCore.QSize(600, 0))
        self.output_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.output_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.output_frame.setObjectName("output_frame")
        self.output_layout = QtWidgets.QHBoxLayout(self.output_frame)
        self.output_layout.setContentsMargins(0, 0, 0, 0)
        self.output_layout.setSpacing(3)
        self.output_layout.setObjectName("output_layout")
        self.output_tree_frame = QtWidgets.QFrame(parent=self.output_frame)
        self.output_tree_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.output_tree_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.output_tree_frame.setObjectName("output_tree_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.output_tree_frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.output_layout.addWidget(self.output_tree_frame)
        self.button_frame = QtWidgets.QFrame(parent=self.output_frame)
        self.button_frame.setMaximumSize(QtCore.QSize(50, 16777215))
        self.button_frame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.button_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.button_frame.setObjectName("button_frame")
        self.button_layout = QtWidgets.QVBoxLayout(self.button_frame)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setSpacing(3)
        self.button_layout.setObjectName("button_layout")
        self.add_doc_button = QtWidgets.QPushButton(parent=self.button_frame)
        self.add_doc_button.setObjectName("add_doc_button")
        self.button_layout.addWidget(self.add_doc_button)
        self.remove_doc_button = QtWidgets.QPushButton(parent=self.button_frame)
        self.remove_doc_button.setObjectName("remove_doc_button")
        self.button_layout.addWidget(self.remove_doc_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.button_layout.addItem(spacerItem)
        self.button_layout.setStretch(0, 1)
        self.button_layout.setStretch(1, 1)
        self.output_layout.addWidget(self.button_frame)
        self.main_layout.addWidget(self.output_frame, 1, 1, 1, 1)
        self.generate_frame = QtWidgets.QFrame(parent=pypdfeditor)
        self.generate_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.generate_frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.generate_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.generate_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.generate_frame.setObjectName("generate_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.generate_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.output_label = QtWidgets.QLabel(parent=self.generate_frame)
        self.output_label.setObjectName("output_label")
        self.horizontalLayout.addWidget(self.output_label)
        self.output_line_edit = QtWidgets.QLineEdit(parent=self.generate_frame)
        self.output_line_edit.setObjectName("output_line_edit")
        self.horizontalLayout.addWidget(self.output_line_edit)
        self.generate_button = QtWidgets.QPushButton(parent=self.generate_frame)
        self.generate_button.setObjectName("generate_button")
        self.horizontalLayout.addWidget(self.generate_button)
        self.close_button = QtWidgets.QPushButton(parent=self.generate_frame)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout.addWidget(self.close_button)
        self.main_layout.addWidget(self.generate_frame, 2, 0, 1, 2)
        self.input_frame = QtWidgets.QFrame(parent=pypdfeditor)
        self.input_frame.setMinimumSize(QtCore.QSize(30, 30))
        self.input_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.input_frame.setObjectName("input_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.input_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_layout.addWidget(self.input_frame, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.main_layout, 0, 0, 1, 1)

        self.retranslateUi(pypdfeditor)
        QtCore.QMetaObject.connectSlotsByName(pypdfeditor)

    def retranslateUi(self, pypdfeditor):
        _translate = QtCore.QCoreApplication.translate
        pypdfeditor.setWindowTitle(_translate("pypdfeditor", "pypdfeditor"))
        self.add_doc_button.setText(_translate("pypdfeditor", "Add"))
        self.remove_doc_button.setText(_translate("pypdfeditor", "Rem"))
        self.output_label.setText(_translate("pypdfeditor", "Output"))
        self.output_line_edit.setText(_translate("pypdfeditor", "Folder for generated files"))
        self.generate_button.setText(_translate("pypdfeditor", "Generate"))
        self.close_button.setText(_translate("pypdfeditor", "Close"))

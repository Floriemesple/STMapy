# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_citswidget.ui'
#
# Created: Tue Jul 25 12:36:32 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CitsWidget(object):
    def setupUi(self, CitsWidget):
        CitsWidget.setObjectName(_fromUtf8("CitsWidget"))
        CitsWidget.resize(1210, 1058)
        self.centralwidget = QtGui.QWidget(CitsWidget)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.m_cbarWidget = QtGui.QWidget(self.centralwidget)
        self.m_cbarWidget.setObjectName(_fromUtf8("m_cbarWidget"))
        self.gridLayout = QtGui.QGridLayout(self.m_cbarWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.m_normButton = QtGui.QPushButton(self.m_cbarWidget)
        self.m_normButton.setObjectName(_fromUtf8("m_normButton"))
        self.gridLayout.addWidget(self.m_normButton, 4, 1, 1, 1)
        self.m_colorBarBox = QtGui.QComboBox(self.m_cbarWidget)
        self.m_colorBarBox.setObjectName(_fromUtf8("m_colorBarBox"))
        self.gridLayout.addWidget(self.m_colorBarBox, 0, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.m_cbarWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.m_cbarLowerBox = QtGui.QLineEdit(self.m_cbarWidget)
        self.m_cbarLowerBox.setEnabled(False)
        self.m_cbarLowerBox.setObjectName(_fromUtf8("m_cbarLowerBox"))
        self.gridLayout.addWidget(self.m_cbarLowerBox, 3, 0, 1, 1)
        self.m_cbarCustomCheckbox = QtGui.QCheckBox(self.m_cbarWidget)
        self.m_cbarCustomCheckbox.setObjectName(_fromUtf8("m_cbarCustomCheckbox"))
        self.gridLayout.addWidget(self.m_cbarCustomCheckbox, 1, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.m_cbarWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 2, 1, 1, 1)
        self.m_cbarUpperBox = QtGui.QLineEdit(self.m_cbarWidget)
        self.m_cbarUpperBox.setEnabled(False)
        self.m_cbarUpperBox.setObjectName(_fromUtf8("m_cbarUpperBox"))
        self.gridLayout.addWidget(self.m_cbarUpperBox, 3, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.m_cbarWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.m_cbarWidget, 13, 1, 1, 1)
        self.m_avgWidget = QtGui.QWidget(self.centralwidget)
        self.m_avgWidget.setObjectName(_fromUtf8("m_avgWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.m_avgWidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.m_belowLine = QtGui.QLineEdit(self.m_avgWidget)
        self.m_belowLine.setReadOnly(True)
        self.m_belowLine.setObjectName(_fromUtf8("m_belowLine"))
        self.gridLayout_3.addWidget(self.m_belowLine, 3, 0, 1, 1)
        self.m_avgVButton = QtGui.QPushButton(self.m_avgWidget)
        self.m_avgVButton.setObjectName(_fromUtf8("m_avgVButton"))
        self.gridLayout_3.addWidget(self.m_avgVButton, 4, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.m_avgWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 0, 2, 1, 1)
        self.m_aboveBar = QtGui.QProgressBar(self.m_avgWidget)
        self.m_aboveBar.setProperty("value", 50)
        self.m_aboveBar.setTextVisible(False)
        self.m_aboveBar.setOrientation(QtCore.Qt.Vertical)
        self.m_aboveBar.setInvertedAppearance(True)
        self.m_aboveBar.setObjectName(_fromUtf8("m_aboveBar"))
        self.gridLayout_3.addWidget(self.m_aboveBar, 2, 2, 1, 1)
        self.m_belowBar = QtGui.QProgressBar(self.m_avgWidget)
        self.m_belowBar.setProperty("value", 50)
        self.m_belowBar.setTextVisible(False)
        self.m_belowBar.setOrientation(QtCore.Qt.Vertical)
        self.m_belowBar.setObjectName(_fromUtf8("m_belowBar"))
        self.gridLayout_3.addWidget(self.m_belowBar, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.m_avgWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.m_avgWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 1, 3, 1, 1)
        self.m_aboveBox = QtGui.QSpinBox(self.m_avgWidget)
        self.m_aboveBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.m_aboveBox.setMaximum(100)
        self.m_aboveBox.setProperty("value", 50)
        self.m_aboveBox.setObjectName(_fromUtf8("m_aboveBox"))
        self.gridLayout_3.addWidget(self.m_aboveBox, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.m_avgWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 1, 1, 1, 1)
        self.m_belowBox = QtGui.QSpinBox(self.m_avgWidget)
        self.m_belowBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.m_belowBox.setMaximum(100)
        self.m_belowBox.setProperty("value", 50)
        self.m_belowBox.setObjectName(_fromUtf8("m_belowBox"))
        self.gridLayout_3.addWidget(self.m_belowBox, 1, 0, 1, 1)
        self.m_aboveLine = QtGui.QLineEdit(self.m_avgWidget)
        self.m_aboveLine.setReadOnly(True)
        self.m_aboveLine.setObjectName(_fromUtf8("m_aboveLine"))
        self.gridLayout_3.addWidget(self.m_aboveLine, 3, 2, 1, 1)
        self.gridLayout_2.addWidget(self.m_avgWidget, 13, 0, 1, 1)
        self.m_fitWidget = QtGui.QWidget(self.centralwidget)
        self.m_fitWidget.setObjectName(_fromUtf8("m_fitWidget"))
        self.gridLayout_4 = QtGui.QGridLayout(self.m_fitWidget)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.m_fitLowerBox = QtGui.QLineEdit(self.m_fitWidget)
        self.m_fitLowerBox.setEnabled(True)
        self.m_fitLowerBox.setObjectName(_fromUtf8("m_fitLowerBox"))
        self.gridLayout_4.addWidget(self.m_fitLowerBox, 3, 0, 1, 1)
        self.m_fitUpperBox = QtGui.QLineEdit(self.m_fitWidget)
        self.m_fitUpperBox.setEnabled(True)
        self.m_fitUpperBox.setObjectName(_fromUtf8("m_fitUpperBox"))
        self.gridLayout_4.addWidget(self.m_fitUpperBox, 3, 1, 1, 1)
        self.m_fitLowerLabel = QtGui.QLabel(self.m_fitWidget)
        self.m_fitLowerLabel.setObjectName(_fromUtf8("m_fitLowerLabel"))
        self.gridLayout_4.addWidget(self.m_fitLowerLabel, 2, 0, 1, 1)
        self.m_fitUpperLabel = QtGui.QLabel(self.m_fitWidget)
        self.m_fitUpperLabel.setObjectName(_fromUtf8("m_fitUpperLabel"))
        self.gridLayout_4.addWidget(self.m_fitUpperLabel, 2, 1, 1, 1)
        self.m_fitSpec = QtGui.QPushButton(self.m_fitWidget)
        self.m_fitSpec.setObjectName(_fromUtf8("m_fitSpec"))
        self.gridLayout_4.addWidget(self.m_fitSpec, 0, 0, 1, 1)
        self.m_fitCustomCheckbox = QtGui.QCheckBox(self.m_fitWidget)
        self.m_fitCustomCheckbox.setObjectName(_fromUtf8("m_fitCustomCheckbox"))
        self.gridLayout_4.addWidget(self.m_fitCustomCheckbox, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.m_fitWidget, 10, 1, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.m_waterfallButton = QtGui.QRadioButton(self.centralwidget)
        self.m_waterfallButton.setChecked(False)
        self.m_waterfallButton.setObjectName(_fromUtf8("m_waterfallButton"))
        self.horizontalLayout_6.addWidget(self.m_waterfallButton)
        self.m_plot2DButton = QtGui.QRadioButton(self.centralwidget)
        self.m_plot2DButton.setChecked(True)
        self.m_plot2DButton.setObjectName(_fromUtf8("m_plot2DButton"))
        self.horizontalLayout_6.addWidget(self.m_plot2DButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.m_openButton = QtGui.QPushButton(self.centralwidget)
        self.m_openButton.setObjectName(_fromUtf8("m_openButton"))
        self.horizontalLayout.addWidget(self.m_openButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.m_topoButton = QtGui.QPushButton(self.centralwidget)
        self.m_topoButton.setObjectName(_fromUtf8("m_topoButton"))
        self.horizontalLayout.addWidget(self.m_topoButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.m_wholeLengthCutButton = QtGui.QPushButton(self.centralwidget)
        self.m_wholeLengthCutButton.setObjectName(_fromUtf8("m_wholeLengthCutButton"))
        self.horizontalLayout.addWidget(self.m_wholeLengthCutButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.m_channelBox = QtGui.QComboBox(self.centralwidget)
        self.m_channelBox.setObjectName(_fromUtf8("m_channelBox"))
        self.horizontalLayout_2.addWidget(self.m_channelBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.m_clearSpec = QtGui.QPushButton(self.centralwidget)
        self.m_clearSpec.setObjectName(_fromUtf8("m_clearSpec"))
        self.gridLayout_2.addWidget(self.m_clearSpec, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.m_voltageBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.m_voltageBox.setDecimals(0)
        self.m_voltageBox.setObjectName(_fromUtf8("m_voltageBox"))
        self.horizontalLayout_4.addWidget(self.m_voltageBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.m_avgBox = QtGui.QCheckBox(self.centralwidget)
        self.m_avgBox.setObjectName(_fromUtf8("m_avgBox"))
        self.horizontalLayout_3.addWidget(self.m_avgBox)
        self.m_derivBox = QtGui.QCheckBox(self.centralwidget)
        self.m_derivBox.setObjectName(_fromUtf8("m_derivBox"))
        self.horizontalLayout_3.addWidget(self.m_derivBox)
        self.m_logBox = QtGui.QCheckBox(self.centralwidget)
        self.m_logBox.setObjectName(_fromUtf8("m_logBox"))
        self.horizontalLayout_3.addWidget(self.m_logBox)
        self.m_derivNBox = QtGui.QSpinBox(self.centralwidget)
        self.m_derivNBox.setEnabled(False)
        self.m_derivNBox.setMinimum(1)
        self.m_derivNBox.setMaximum(501)
        self.m_derivNBox.setSingleStep(2)
        self.m_derivNBox.setProperty("value", 11)
        self.m_derivNBox.setObjectName(_fromUtf8("m_derivNBox"))
        self.horizontalLayout_3.addWidget(self.m_derivNBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.m_shiftXBox = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.m_shiftXBox.sizePolicy().hasHeightForWidth())
        self.m_shiftXBox.setSizePolicy(sizePolicy)
        self.m_shiftXBox.setObjectName(_fromUtf8("m_shiftXBox"))
        self.horizontalLayout_5.addWidget(self.m_shiftXBox)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_5.addWidget(self.label_13)
        self.m_shiftYBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.m_shiftYBox.setMinimum(-1000.0)
        self.m_shiftYBox.setMaximum(1000.0)
        self.m_shiftYBox.setSingleStep(1e-06)
        self.m_shiftYBox.setObjectName(_fromUtf8("m_shiftYBox"))
        self.horizontalLayout_5.addWidget(self.m_shiftYBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 5, 1, 1, 1)
        self.m_viewSelectedBox = QtGui.QCheckBox(self.centralwidget)
        self.m_viewSelectedBox.setObjectName(_fromUtf8("m_viewSelectedBox"))
        self.gridLayout_2.addWidget(self.m_viewSelectedBox, 8, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 11, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 11, 1, 1, 1)
        self.m_avgCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.m_avgCheckBox.setObjectName(_fromUtf8("m_avgCheckBox"))
        self.gridLayout_2.addWidget(self.m_avgCheckBox, 12, 0, 1, 1)
        self.m_cbarCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.m_cbarCheckBox.setObjectName(_fromUtf8("m_cbarCheckBox"))
        self.gridLayout_2.addWidget(self.m_cbarCheckBox, 12, 1, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.m_rcAvgBox = QtGui.QSpinBox(self.centralwidget)
        self.m_rcAvgBox.setMaximum(100)
        self.m_rcAvgBox.setProperty("value", 2)
        self.m_rcAvgBox.setObjectName(_fromUtf8("m_rcAvgBox"))
        self.horizontalLayout_7.addWidget(self.m_rcAvgBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 8, 1, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.m_avgSpec = QtGui.QPushButton(self.centralwidget)
        self.m_avgSpec.setObjectName(_fromUtf8("m_avgSpec"))
        self.horizontalLayout_9.addWidget(self.m_avgSpec)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.m_scaleVoltage = QtGui.QCheckBox(self.centralwidget)
        self.m_scaleVoltage.setChecked(True)
        self.m_scaleVoltage.setObjectName(_fromUtf8("m_scaleVoltage"))
        self.horizontalLayout_8.addWidget(self.m_scaleVoltage)
        self.m_scaleMetric = QtGui.QCheckBox(self.centralwidget)
        self.m_scaleMetric.setChecked(True)
        self.m_scaleMetric.setObjectName(_fromUtf8("m_scaleMetric"))
        self.horizontalLayout_8.addWidget(self.m_scaleMetric)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)
        self.map_layout = QtGui.QVBoxLayout()
        self.map_layout.setContentsMargins(0, 0, -1, -1)
        self.map_layout.setObjectName(_fromUtf8("map_layout"))
        self.m_mapWidget = MatplotlibWidget(self.centralwidget)
        self.m_mapWidget.setMinimumSize(QtCore.QSize(440, 440))
        self.m_mapWidget.setObjectName(_fromUtf8("m_mapWidget"))
        self.map_layout.addWidget(self.m_mapWidget)
        self.gridLayout_2.addLayout(self.map_layout, 14, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_2.addWidget(self.line_3, 9, 1, 1, 1)
        self.spec_layout = QtGui.QVBoxLayout()
        self.spec_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.spec_layout.setContentsMargins(0, -1, -1, -1)
        self.spec_layout.setObjectName(_fromUtf8("spec_layout"))
        self.m_specWidget = MatplotlibWidget(self.centralwidget)
        self.m_specWidget.setObjectName(_fromUtf8("m_specWidget"))
        self.spec_layout.addWidget(self.m_specWidget)
        self.gridLayout_2.addLayout(self.spec_layout, 14, 1, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.m_vLineBox = QtGui.QCheckBox(self.centralwidget)
        self.m_vLineBox.setObjectName(_fromUtf8("m_vLineBox"))
        self.horizontalLayout_10.addWidget(self.m_vLineBox)
        self.m_legendBox = QtGui.QCheckBox(self.centralwidget)
        self.m_legendBox.setObjectName(_fromUtf8("m_legendBox"))
        self.horizontalLayout_10.addWidget(self.m_legendBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 3, 1, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)
        self.m_CitsAvgBox = QtGui.QSpinBox(self.centralwidget)
        self.m_CitsAvgBox.setMinimum(1)
        self.m_CitsAvgBox.setMaximum(10000000)
        self.m_CitsAvgBox.setObjectName(_fromUtf8("m_CitsAvgBox"))
        self.gridLayout_5.addWidget(self.m_CitsAvgBox, 0, 1, 1, 1)
        self.m_averageCitsButton = QtGui.QPushButton(self.centralwidget)
        self.m_averageCitsButton.setObjectName(_fromUtf8("m_averageCitsButton"))
        self.gridLayout_5.addWidget(self.m_averageCitsButton, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 10, 0, 1, 1)
        CitsWidget.setCentralWidget(self.centralwidget)
        self.m_menuBar = QtGui.QMenuBar(CitsWidget)
        self.m_menuBar.setGeometry(QtCore.QRect(0, 0, 1210, 21))
        self.m_menuBar.setObjectName(_fromUtf8("m_menuBar"))
        CitsWidget.setMenuBar(self.m_menuBar)
        self.m_statusBar = QtGui.QStatusBar(CitsWidget)
        self.m_statusBar.setObjectName(_fromUtf8("m_statusBar"))
        CitsWidget.setStatusBar(self.m_statusBar)

        self.retranslateUi(CitsWidget)
        QtCore.QMetaObject.connectSlotsByName(CitsWidget)

    def retranslateUi(self, CitsWidget):
        CitsWidget.setWindowTitle(_translate("CitsWidget", "STM Data Analysis", None))
        self.m_normButton.setText(_translate("CitsWidget", "Normalize current channel", None))
        self.label_10.setText(_translate("CitsWidget", "Colorbar to use", None))
        self.m_cbarLowerBox.setPlaceholderText(_translate("CitsWidget", "0", None))
        self.m_cbarCustomCheckbox.setText(_translate("CitsWidget", "Use custom limits", None))
        self.label_12.setText(_translate("CitsWidget", "Custom upper limit", None))
        self.m_cbarUpperBox.setPlaceholderText(_translate("CitsWidget", "0", None))
        self.label_11.setText(_translate("CitsWidget", "Custom lower limit", None))
        self.m_avgVButton.setText(_translate("CitsWidget", "Start the averaging", None))
        self.label_4.setText(_translate("CitsWidget", "Maximum value for the above averaging", None))
        self.label_3.setText(_translate("CitsWidget", "Minimum value for the below averaging", None))
        self.label_6.setText(_translate("CitsWidget", "% of colormap", None))
        self.label_5.setText(_translate("CitsWidget", "% of colormap", None))
        self.m_fitLowerBox.setText(_translate("CitsWidget", "0.0", None))
        self.m_fitUpperBox.setText(_translate("CitsWidget", "0.0", None))
        self.m_fitLowerLabel.setText(_translate("CitsWidget", "Lower limit", None))
        self.m_fitUpperLabel.setText(_translate("CitsWidget", "Upper limit", None))
        self.m_fitSpec.setText(_translate("CitsWidget", "Fit spectra", None))
        self.m_fitCustomCheckbox.setText(_translate("CitsWidget", "Use a custom range", None))
        self.m_waterfallButton.setText(_translate("CitsWidget", "Waterfall", None))
        self.m_plot2DButton.setText(_translate("CitsWidget", "2D plot", None))
        self.label_8.setText(_translate("CitsWidget", "Cuts :", None))
        self.m_openButton.setText(_translate("CitsWidget", "Open CITS", None))
        self.m_topoButton.setText(_translate("CitsWidget", "Draw topo", None))
        self.m_wholeLengthCutButton.setText(_translate("CitsWidget", "Whole length cut", None))
        self.label_7.setText(_translate("CitsWidget", "Displayed channel", None))
        self.m_clearSpec.setText(_translate("CitsWidget", "Clear spectra", None))
        self.label.setText(_translate("CitsWidget", "V/Z Index", None))
        self.m_avgBox.setText(_translate("CitsWidget", "Average spectra by selection", None))
        self.m_derivBox.setText(_translate("CitsWidget", "Plot derivative", None))
        self.m_logBox.setText(_translate("CitsWidget", "Plot log instead", None))
        self.label_9.setText(_translate("CitsWidget", "ShiftX", None))
        self.m_shiftXBox.setText(_translate("CitsWidget", "0.0", None))
        self.label_13.setText(_translate("CitsWidget", "Shift Y", None))
        self.m_viewSelectedBox.setText(_translate("CitsWidget", "View selected spectra", None))
        self.m_avgCheckBox.setText(_translate("CitsWidget", "Average with respect to values", None))
        self.m_cbarCheckBox.setText(_translate("CitsWidget", "Colorbar settings", None))
        self.label_2.setText(_translate("CitsWidget", "Number of pixels for right-click average", None))
        self.m_avgSpec.setText(_translate("CitsWidget", "Average on map", None))
        self.m_scaleVoltage.setText(_translate("CitsWidget", "Scale in Volts", None))
        self.m_scaleMetric.setText(_translate("CitsWidget", "Scale in metric units", None))
        self.m_vLineBox.setText(_translate("CitsWidget", "Index guideline", None))
        self.m_legendBox.setText(_translate("CitsWidget", "Deactivate legend", None))
        self.label_14.setText(_translate("CitsWidget", "Number of spectras for CITS average", None))
        self.m_averageCitsButton.setText(_translate("CitsWidget", "Average CITS", None))

from matplotlibwidget import MatplotlibWidget

#!/usr/bin/python
# -*- coding: utf-8 -*-
import PySide6.QtCore
import PySide6.QtGui
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QMainWindow, QPlainTextEdit
from abc_bo import bees_algorithm
import pyqtgraph as pg


class SetUpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self) -> None:

        self.pic_show = QLabel(self)
        self.pic = PySide6.QtGui.QPixmap("bees3.jpg")
        self.pic_show.setPixmap(self.pic)
        self.pic_show.setFixedSize(1000, 150)

        # Przycisk start
        self.start_btn = QPushButton("Start", self)
        self.start_btn.move(50, 575)
        self.start_btn.clicked.connect(self.reset_values)
        self.start_btn.clicked.connect(self.get_values_from_GUI)
        self.start_btn.clicked.connect(self.startBA)

        # Wprowadzenie liczby iteracji
        self.parameters_set = QLabel(self)
        self.parameters_set.setText("Wprowadź parametry:")
        self.parameters_set.setFixedWidth(200)
        self.parameters_set.setFont(PySide6.QtGui.QFont("Times", 10, PySide6.QtGui.QFont.Bold))
        self.parameters_set.move(50, 150)

        self.res_line_label = QLabel(self)
        self.res_line_label.setText("Liczba rozwiązań: ")
        self.res_line_label.move(25, 200)

        self.res_line_edit = QLineEdit(self)
        self.res_line_edit.setFixedWidth(100)
        self.res_line_edit.move(250, 200)

        self.iter_line_label = QLabel(self)
        self.iter_line_label.setText("Liczba iteracji: ")
        self.iter_line_label.move(25, 250)

        self.iter_line_edit = QLineEdit(self)
        self.iter_line_edit.setFixedWidth(100)
        self.iter_line_edit.move(250, 250)

        # Wprowadzenie LT
        self.LT_line_label = QLabel(self)
        self.LT_line_label.setText("Life Time: ")
        self.LT_line_label.move(25, 300)

        self.LT_line_edit = QLineEdit(self)
        self.LT_line_edit.setFixedWidth(100)
        self.LT_line_edit.move(250, 300)

        # Wprowadzenie le
        self.le_line_label = QLabel(self)
        self.le_line_label.setText("Rozmiar elity: ")
        self.le_line_label.move(25, 350)

        self.le_line_edit = QLineEdit(self)
        self.le_line_edit.setFixedWidth(100)
        self.le_line_edit.move(250, 350)

        # Wprowadzenie lb
        self.lb_line_label = QLabel(self)
        self.lb_line_label.setText("Rozmiar zbioru najlepszych rozwiązań: ")
        self.lb_line_label.setFixedWidth(200)
        self.lb_line_label.move(25, 400)

        self.lb_line_edit = QLineEdit(self)
        self.lb_line_edit.setFixedWidth(100)
        self.lb_line_edit.move(250, 400)

        # Wprowadzenie nb
        self.nb_line_label = QLabel(self)
        self.nb_line_label.setText("Rozmiar otoczenia najlepszych rozwiązań: ")
        self.nb_line_label.setFixedWidth(250)
        self.nb_line_label.move(25, 450)

        self.nb_line_edit = QLineEdit(self)
        self.nb_line_edit.setFixedWidth(100)
        self.nb_line_edit.move(250, 450)

        # Wprowadzenie ne
        self.ne_line_label = QLabel(self)
        self.ne_line_label.setText("Rozmiar otoczenia elity: ")
        self.ne_line_label.setFixedWidth(200)
        self.ne_line_label.move(25, 500)

        self.ne_line_edit = QLineEdit(self)
        self.ne_line_edit.setFixedWidth(100)
        self.ne_line_edit.move(250, 500)

        # Wyswietlanie wyniku
        self.aimfunc = QLabel(self)
        self.aimfunc.setFixedWidth(200)
        self.aimfunc.setText("Aktualna wartość funkcji celu:")
        self.aimfunc.setFont(PySide6.QtGui.QFont("Times", 10, PySide6.QtGui.QFont.Bold))
        self.aimfunc.move(450, 625)

        self.aimfunc_val = QPlainTextEdit(self)
        # self.aimfunc_val.setFixedWidth(200)
        self.aimfunc_val.setReadOnly(True)
        self.aimfunc_val.move(650, 625)

        self.solution_val_label = QLabel(self)
        self.solution_val_label.setFixedWidth(200)
        self.solution_val_label.setText("Rozwiązanie:")
        self.solution_val_label.setFont(PySide6.QtGui.QFont("Times", 10, PySide6.QtGui.QFont.Bold))
        self.solution_val_label.move(50, 625)

        self.solution_val = QPlainTextEdit(self)
        self.solution_val.setFixedWidth(800)
        self.solution_val.setFixedHeight(100)
        self.solution_val.setReadOnly(True)
        self.solution_val.move(50, 675)

        self.setFixedSize(1000, 800)
        self.setWindowTitle("Algorytm Pszczeli")
        self.show()

    def get_values_from_GUI(self) -> None:
        ''' Zapisywanie wprowadzonych danych do zmiennych'''
        if self.Imax is None:
            self.Imax = int(self.iter_line_edit.text())
            self.LT = int(self.LT_line_edit.text())
            self.le = int(self.le_line_edit.text())
            self.lb = int(self.lb_line_edit.text())
            self.Nb = int(self.nb_line_edit.text())
            self.Ne = int(self.ne_line_edit.text())
            self.res_num = int(self.res_line_edit.text())
        else:
            pass

    def reset_values(self):
        self.Imax = None
        self.LT = None
        self.le = None
        self.lb = None
        self.Nb = None
        self.Ne = None
        self.res_num = None


    def startBA(self):
        '''Wykonanie algorytmu'''
        self.solution, self.solution_value, temp = bees_algorithm(self.res_num, self.le, self.lb, self.Ne, self.Nb, self.LT, self.Imax)
        self.value_list = temp[::-1]
        self.aimfunc_val.setPlainText(str(self.solution_value)) #tak beda sie zmieniac wyswietlane wartości
        self.solution_val.setPlainText(str(self.solution))
        self.show_chart()

    def show_chart(self):
        self.graphWidget = pg.PlotWidget(self)
        self.graphWidget.setBackground('w')
        self.graphWidget.move(450, 200)
        self.graphWidget.setFixedSize(500, 400)
        self.graphWidget.plot(self.value_list, pen=pg.mkPen(color=(255, 0, 0), width=1, style=PySide6.QtCore.Qt.PenStyle.DashLine))
        self.graphWidget.setTitle("Wartości funkcji celu")
        self.graphWidget.setLabel("bottom", "Numer rozwiązania")
        self.graphWidget.setLabel("left", "Wartość funkcji celu")
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.show()


if __name__ == "__main__":
    app = QApplication([])

    test = SetUpWindow()

    app.exec()

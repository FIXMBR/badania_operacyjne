#!/usr/bin/python
# -*- coding: utf-8 -*-
import PySide6.QtCore
from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLabel, QMainWindow, QCheckBox
# from typing import Tuple


class SetUpWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self) -> None:
        self.window = None

        # Przycisk start
        self.start_btn = QPushButton("Start", self)
        self.start_btn.move(50, 525)
        self.start_btn.clicked.connect(self.get_values_from_GUI)
        self.start_btn.clicked.connect(self.startBA)

        # Przycisk do ekranu z wynikami - zobaczymy czy sie przyda
        self.result_btn = QPushButton("Wyniki", self)
        self.result_btn.move(50, 575)
        self.result_btn.clicked.connect(self.show_results_window)

        # Wprowadzenie liczby iteracji
        self.parameters_set = QLabel(self)
        self.parameters_set.setText("Wprowadź parametry:")
        self.parameters_set.setFixedWidth(200)
        self.parameters_set.setFont(PySide6.QtGui.QFont("Times", 10, PySide6.QtGui.QFont.Bold))
        self.parameters_set.move(50, 150)

        self.iter_line_label = QLabel(self)
        self.iter_line_label.setText("Liczba iteracji: ")
        self.iter_line_label.move(25, 200)

        self.iter_line_edit = QLineEdit(self)
        self.iter_line_edit.setFixedWidth(100)
        self.iter_line_edit.move(100, 200)

        # Wprowadzenie LT
        self.LT_line_label = QLabel(self)
        self.LT_line_label.setText("Life Time: ")
        self.LT_line_label.move(25, 250)

        self.LT_line_edit = QLineEdit(self)
        self.LT_line_edit.setFixedWidth(100)
        self.LT_line_edit.move(100, 250)

        # Wprowadzenie le
        self.le_line_label = QLabel(self)
        self.le_line_label.setText("Rozmiar elity: ")
        self.le_line_label.move(25, 300)

        self.le_line_edit = QLineEdit(self)
        self.le_line_edit.setFixedWidth(100)
        self.le_line_edit.move(100, 300)

        # Wprowadzenie lb
        self.lb_line_label = QLabel(self)
        self.lb_line_label.setText("Rozmiar lb: ")
        self.lb_line_label.move(25, 350)

        self.lb_line_edit = QLineEdit(self)
        self.lb_line_edit.setFixedWidth(100)
        self.lb_line_edit.move(100, 350)

        # Wprowadzenie nb
        self.nb_line_label = QLabel(self)
        self.nb_line_label.setText("Rozmiar Nb: ")
        self.nb_line_label.move(25, 400)

        self.nb_line_edit = QLineEdit(self)
        self.nb_line_edit.setFixedWidth(100)
        self.nb_line_edit.move(100, 400)

        #Wybor rodzaju sąsiedztwa
        self.neighbourhood_set_gen = QLabel(self)
        self.neighbourhood_set_gen.setText("Wybór generowania sąsiedztwa:")
        self.neighbourhood_set_gen.setFixedWidth(200)
        self.neighbourhood_set_gen.setFont(PySide6.QtGui.QFont("Times", 10, PySide6.QtGui.QFont.Bold))
        self.neighbourhood_set_gen.move(50, 450)

        self.opt1_gen_neighbour = QCheckBox("Opcja 1", self)
        self.opt1_gen_neighbour.move(75, 475)

        self.opt2_gen_neighbour = QCheckBox("Opcja 2", self)
        self.opt2_gen_neighbour.move(150, 475)

        # Wyswietlanie wyniku
        self.display = QLabel(self)
        self.display.setFixedWidth(200)
        self.display.setText("Aktualne rozwiązanie:")
        self.display.setFont(PySide6.QtGui.QFont("Times", 10, PySide6.QtGui.QFont.Bold))
        self.display.move(750, 200)

        self.res_value = QLabel(self)
        self.res_value.setFixedWidth(200)
        self.res_value.move(750, 250)

        self.aimfunc = QLabel(self)
        self.aimfunc.setFixedWidth(200)
        self.aimfunc.setText("Aktualna wartość funkcji celu:")
        self.aimfunc.setFont(PySide6.QtGui.QFont("Times", 10, PySide6.QtGui.QFont.Bold))
        self.aimfunc.move(750, 300)
        # self.display.setAlignment(PySide6.QtCore.Qt.AlignmentFlag.AlignLeft)

        self.aimfunc_val = QLabel(self)
        self.aimfunc_val.setFixedWidth(200)
        self.aimfunc_val.move(750, 350)

        self.setFixedSize(1000, 800)
        self.setWindowTitle("Algorytm Pszczeli")
        self.show()

    def show_results_window(self):
        if self.window is None:
            self.window = ResultsWindow()
        self.window.show()

    def get_values_from_GUI(self) -> None:
        ''' Zapisywanie wprowadzonych danych do zmiennych'''
        self.Imax = int(self.iter_line_edit.text())
        self.LT = int(self.LT_line_edit.text())
        self.le = int(self.le_line_edit.text())
        self.lb = int(self.lb_line_edit.text())
        self.Nb = int(self.nb_line_edit.text())
        if self.opt1_gen_neighbour.isChecked():
            # pierwsza opcja
            pass
        elif self.opt2_gen_neighbour.isChecked():
            #druga opcja
            pass

    # def get_values(self) -> Tuple[int, int, int, int, int]:
    #     parameters = (self.Imax, self.LT, self.le, self.lb, self.Nb)
    #     print(parameters)
    #     return parameters

    def startBA(self):
        '''Wykonanie algorytmu'''
        self.res_value.setText("Test")
        self.aimfunc_val.setText("test") #tak beda sie zmieniac wyswietlane wartości



class ResultsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.quit_btn = QPushButton("Zamknij", self)
        self.quit_btn.move(850, 750)
        self.quit_btn.clicked.connect(self.close)

        self.setFixedSize(1000, 100)
        self.setWindowTitle("Algorytm Pszczeli - Wyniki")
        self.show()

    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        event.accept()


if __name__ == "__main__":
    app = QApplication([])

    test = SetUpWindow()

    app.exec()

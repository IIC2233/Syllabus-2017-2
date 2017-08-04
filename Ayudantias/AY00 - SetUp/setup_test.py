#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Andrés Fernández <alfernandez@uc.cl>"

import subprocess as sp
import sys
import platform


try:
    welcome_text = ("Este script revisará que tengas correctamente instalados"
                    " Python, Git, numpy, matplotlib y PyQt5. En caso de no"
                    " tener instalada alguna parte, recuerda consultar la wiki"
                    " del Syllabus para encontrar instrucciones de cómo"
                    " lograrlo. También puedes preguntar en las issues del"
                    " Syllabus por ayuda.\n")
    print(welcome_text)
    # Python
    if platform.system() in ("Windows", "Darwin"):
        if sys.version_info.major != 3 and sys.version_info.minor < 6:
            raise Exception(
                "[PROBLEMA] La versión de Python debe ser superior o igual a 3.6.0")
    elif sys.version_info.major != 3 and sys.version_info.minor < 5:
        raise Exception(
            "[PROBLEMA] La versión de Python para Linux debe ser superior o igual a 3.5.0")
    # git
    if sp.call(["git", "--version"]) != 0:
        raise Exception("[PROBLEMA] Git no fue instalado correctamente.")
    # numpy
    import numpy
    # matplotlib
    import matplotlib
    # PyQt5
    import PyQt5

except ImportError as e:
    print("[PROBLEMA] El módulo {name} no fue instalado correctamente.".format(
        name=e.name))

except (Exception) as e:
    print(e)

else:
    from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QMessageBox)
    app = QApplication(sys.argv)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("¡Felicidades!")
    msg.setInformativeText("Todo pareciera estar bien instalado 👍🏼")
    msg.setWindowTitle("IIC2233")
    msg.show()
    sys.exit(app.exec_())

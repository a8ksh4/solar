#!/usr/bin/env python3
'''fooo'''

import sys
from datetime import datetime
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
import cupy as cp
import torch
import pyqtgraph as pg
from PIL import Image
import torchvision.transforms as transforms

print("gpu_graph.py")

def main():
    '''foo'''
    # Initialize QApplication and configure CuPy
    print("\n CuPy: ", pg.getConfigOption('useCupy'),"\n")
    pg.setConfigOption('useCupy', 'True')
    print("\n CuPy: ", pg.getConfigOption('useCupy'),"\n")
    print("\n OpenGL: ", pg.getConfigOption('useOpenGL'), "\n")
    pg.setConfigOption('useOpenGL', 'True')
    print("\n OpenGL: ", pg.getConfigOption('useOpenGL'), "\n")
    application = QApplication(sys.argv)

    # Start Program
    start_time = datetime.now()    # to time the program process
    image = Image.open("sheep.png")

    # Define a transform to convert PIL
    # image to a Torch tensor
    transform = transforms.Compose([
        transforms.PILToTensor()
    ])

    # Convert the PIL image to Torch tensor
    img_tensor = transform(image)
    cuda0 = torch.device('cuda:0')
    img_tensor = img_tensor.to(cuda0)
    # Convert image tensor to cupy array
    img_gpu = cp.asarray(img_tensor)
    start_time2 = datetime.now()
    # to observe the operations after cupy array was created

    # Set pyqtgraph configuration properties and try to display an image
    img_pg = pg.ImageItem()
    img_pg.setImage(img_gpu.T)
    plot_pg = pg.plot()
    plot_pg.addItem(img_pg)
    QtCore.QTimer.singleShot(5*1000, QtCore.QCoreApplication.quit)
    # this closes the widget window after 5 seconds so the runtime can be computed
    print(datetime.now() - start_time)
    print(datetime.now() - start_time2)

    sys.exit(application.exec_())

if __name__ == '__main__':
    print("main")
    main()

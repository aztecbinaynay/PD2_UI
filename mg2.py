# import matplotlib.pyplot as plt
# import numpy as np
# import pyqtgraph as pg
# from PyQt5.QtGui import QGuiApplication
# from PyQt5.QtCore import QTimer, QDateTime
# from PyQt5.QtCore import QEventLoop

# # PyQtGraph
# data = np.random.normal(size=(4, 1000))

# # PyQtGraph
# app = QGuiApplication([])
# win = pg.GraphicsLayoutWidget(show=True)
# win.resize(800, 480)
# plot_items = [win.addPlot(row=i, col=0, title=f"Graph {i}") for i in range(1, 5)]

# # PyQtGraph
# for i in range(1000):
#     data = np.random.normal(size=(4, 1000))
#     for j, plot_item in enumerate(plot_items):
#         plot_item.clear()
#         plot_item.plot(data[j])
#     QGuiApplication.processEvents(QEventLoop.AllEvents, 100)

# import matplotlib.pyplot as plt
# import numpy as np
# import pyqtgraph as pg
# from PyQt5.QtGui import QGuiApplication
# from PyQt5.QtCore import QTimer, QDateTime
# from PyQt5.QtCore import QEventLoop
# import serial

# # Connect to the serial port
# ser = serial.Serial("COM8", 9600)

# # PyQtGraph
# app = QGuiApplication([])
# win = pg.GraphicsLayoutWidget(show=True)
# win.resize(800, 480)
# plot_items = [win.addPlot(row=i, col=0, title=f"Graph {i}") for i in range(1, 5)]

# # PyQtGraph
# while True:
#     while True:
#         try:
#             data = (
#                 ser.readline().decode().strip().split("\t")
#             )  # read the line from the serial port and decode it
#             break
#         except UnicodeDecodeError:
#             continue
#     # Convert the data to a numpy array
#     try:
#         data = np.array(data).astype(float)
#         print(data)
#     except ValueError:
#         continue

#     for j, plot_item in enumerate(plot_items):
#         plot_item.clear()
#         plot_item.plot([data[j]])
#     QGuiApplication.processEvents(QEventLoop.AllEvents, 29)

import numpy as np
import pyqtgraph as pg
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import QEventLoop
import serial

# Connect to the serial port
ser = serial.Serial("COM7", 9600)

# PyQtGraph
app = QGuiApplication([])
win = pg.GraphicsLayoutWidget(show=True)
win.resize(800, 480)
plot_items = [win.addPlot(row=i, col=0, title=f"Sensor {i}") for i in range(1, 5)]
plot_curves = [plot_item.plot(pen=(i, 4)) for i, plot_item in enumerate(plot_items)]

# Initialize data
max_length = 340
data = [np.zeros(max_length) for _ in range(4)]

# PyQtGraph
while True:
    while True:
        try:
            raw_data = (
                ser.readline().decode().strip()
            )  # read the line from the serial port and decode it
            break
        except UnicodeDecodeError:
            continue
    # Convert the data to a numpy array
    raw_data = raw_data.split("\t")
    if len(raw_data) == 4:
        new_data = np.array(raw_data).astype(float)
        print(new_data)
    else:
        continue

    # Append new data
    data = [np.append(d, nd)[-max_length:] for d, nd in zip(data, new_data)]

    # Update plot data
    for i, curve in enumerate(plot_curves):
        curve.setData(data[i])

    QGuiApplication.processEvents(QEventLoop.AllEvents, 29)

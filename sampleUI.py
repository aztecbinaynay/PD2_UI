import PySimpleGUI as sg
import serial

# Open a serial connection to the Arduino
ser = serial.Serial('COM8', 1200)

# Define the layout of the GUI
layout = [[sg.Graph(canvas_size=(500, 300), graph_bottom_left=(0, 0), graph_top_right=(500, 300), key='graph')]]

# Create the GUI window
window = sg.Window('Real-time Data Plot', layout)

# Define the data buffer for the graph
data_buffer = []

# Loop to continuously update the graph
while True:
    # Read data from the Arduino
    data = ser.readline().decode().strip()
    # Convert the data to an integer
    data = int(data)
    # Add the data to the buffer
    data_buffer.append(data)
    # If the buffer is longer than 500, remove the oldest value
    if len(data_buffer) > 500:
        data_buffer.pop(0)
    # Clear the graph
    graph = window['graph']
    graph.erase()
    # Plot the data on the graph
    for i, data_point in enumerate(data_buffer):
        graph.draw_line((i-1, data_buffer[i-1]), (i, data_point), color='red')
    # Update the GUI window
    event, values = window.read(timeout=0)
    if event == sg.WIN_CLOSED:
        break

# Close the serial connection and the GUI window
ser.close()
window.close()

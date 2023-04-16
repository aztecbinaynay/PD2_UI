import tkinter as tk
import serial


root = tk.Tk()

root.geometry("800x480")
root.config(bg="#114A9C")

root.title("Sleep Monitor")

# Define the data for each line graph
data1 = [0 for _ in range(150)]
data2 = [0 for _ in range(150)]
data3 = [0 for _ in range(150)]
data4 = [0 for _ in range(150)]

ser = serial.Serial("COM8", 9600)  # replace with the correct port and baud rate

# Define the function to update the line graphs
def update_graphs():
    while True:
        try:
            line = ser.readline().decode().strip()
            break
        except UnicodeDecodeError:
            continue
    values = line.split("\t")

    # Update the data for each line graph
    if len(values) == 4:
        try:
            num1 = float(values[0])
            num2 = float(values[1])
            num3 = float(values[2])
            num4 = float(values[3])

            # Append the received data to the data lists
            data1.pop(0)
            data1.append(num1)
            data2.pop(0)
            data2.append(num2)
            data3.pop(0)
            data3.append(num3)
            data4.pop(0)
            data4.append(num4)

            # Calculate the new range of the y-axis
            y_min = min(min(data1), min(data2), min(data3), min(data4))
            y_max = max(max(data1), max(data2), max(data3), max(data4))
            y_range = y_max - y_min

            # Update the line objects for each sub-canvas
            for canvas, data in zip(
                [canvas1, canvas2, canvas3, canvas4], [data1, data2, data3, data4]
            ):
                # Update the line coordinates
                coords = []
                for i in range(len(data)):
                    x = i * 5 + 22  # Adjust the x coordinate
                    y = (
                        canvas.winfo_height()
                        - ((data[i] - y_min) / y_range) * canvas.winfo_height()
                    )
                    coords += [x, y]

                # Update the line object
                canvas.coords("line", *coords)

        except ValueError:
            pass

    # Schedule the next update
    root.after(29, update_graphs)


# Create the sub-canvases for each line graph using place geometry manager
canvas1 = tk.Canvas(root, width=720, height=100, bg="white")
canvas1.place(x=70, y=0)
canvas1.create_line(0, 50, 710, 50, fill="red", width=2, tags="line")

canvas2 = tk.Canvas(root, width=720, height=100, bg="white")
canvas2.place(x=70, y=107)
canvas2.create_line(0, 50, 710, 50, fill="blue", width=2, tags="line")

canvas3 = tk.Canvas(root, width=720, height=100, bg="white")
canvas3.place(x=70, y=214)
canvas3.create_line(0, 50, 710, 50, fill="green", width=2, tags="line")

canvas4 = tk.Canvas(root, width=720, height=100, bg="white")
canvas4.place(x=70, y=321)
canvas4.create_line(0, 50, 710, 50, fill="brown", width=2, tags="line")


# Schedule the first update
root.after(29, update_graphs)

# Start the main loop
root.mainloop()

#! Original code
# import tkinter as tk
# import random

# root = tk.Tk()

# root.geometry("800x480")
# root.config(bg="#114A9C")

# root.title("Moving Line Graphs")

# # Define the data for each line graph
# data1 = [random.randint(0, 200) for _ in range(50)]
# data2 = [random.randint(0, 200) for _ in range(50)]
# data3 = [random.randint(0, 200) for _ in range(50)]
# data4 = [random.randint(0, 200) for _ in range(50)]

# # Define the function to update the line graphs
# def update_graphs():
#     # Update the data for each line graph
#     data1.pop(0)
#     data1.append(random.randint(0, 200))

#     data2.pop(0)
#     data2.append(random.randint(0, 200))

#     data3.pop(0)
#     data3.append(random.randint(0, 200))

#     data4.pop(0)
#     data4.append(random.randint(0, 200))

#     # Update the line objects for each sub-canvas
#     for canvas, data in zip(
#         [canvas1, canvas2, canvas3, canvas4], [data1, data2, data3, data4]
#     ):
#         # Update the line coordinates
#         coords = []
#         for i in range(len(data)):
#             x = i * 15 + 22  # Adjust the x coordinate
#             y = 100 - data[i] / 2  # Adjust the y coordinate
#             coords += [x, y]

#         # Update the line object
#         canvas.coords("line", *coords)

#     # Schedule the next update
#     root.after(500, update_graphs)


# # Create the sub-canvases for each line graph using place geometry manager
# canvas1 = tk.Canvas(root, width=720, height=100, bg="white")
# canvas1.place(x=70, y=0)
# canvas1.create_line(0, 50, 710, 50, fill="red", width=2, tags="line")

# canvas2 = tk.Canvas(root, width=720, height=100, bg="white")
# canvas2.place(x=70, y=104)
# canvas2.create_line(0, 50, 710, 50, fill="blue", width=2, tags="line")

# canvas3 = tk.Canvas(root, width=720, height=100, bg="white")
# canvas3.place(x=70, y=208)
# canvas3.create_line(0, 50, 710, 50, fill="green", width=2, tags="line")

# canvas4 = tk.Canvas(root, width=720, height=100, bg="white")
# canvas4.place(x=70, y=312)
# canvas4.create_line(0, 50, 710, 50, fill="brown", width=2, tags="line")


# # Schedule the first update
# root.after(500, update_graphs)

# # Start the main loop
# root.mainloop()

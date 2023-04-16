# import random
# import tkinter as tk

# # Create the tkinter root window
# root = tk.Tk()
# root.title("Stacked Line Graphs")

# # Create the four sub-canvases
# canvas1 = tk.Canvas(root, width=200, height=120)
# canvas2 = tk.Canvas(root, width=200, height=120)
# canvas3 = tk.Canvas(root, width=200, height=120)
# canvas4 = tk.Canvas(root, width=200, height=120)

# # Position the sub-canvases
# canvas1.grid(row=0, column=0)
# canvas2.grid(row=1, column=0)
# canvas3.grid(row=2, column=0)
# canvas4.grid(row=3, column=0)

# # Define the data for each line graph
# data1 = [random.randint(0, 200) for i in range(20)]
# data2 = [random.randint(0, 200) for i in range(20)]
# data3 = [random.randint(0, 200) for i in range(20)]
# data4 = [random.randint(0, 200) for i in range(20)]

# # Create the x-axis and y-axis lines for each sub-canvas
# for canvas, data in zip(
#     [canvas1, canvas2, canvas3, canvas4], [data1, data2, data3, data4]
# ):
#     canvas.create_line(20, 100, 180, 100, width=2)  # x-axis
#     canvas.create_line(20, 100, 20, 20, width=2)  # y-axis

#     # Create the line graph for the data
#     coords = []
#     for i in range(len(data)):
#         x = i * 8 + 22  # Adjust the x coordinate
#         y = 100 - data[i] / 2  # Adjust the y coordinate
#         coords += [x, y]
#     canvas.create_line(coords, fill="purple", width=2)


# # Call this function repeatedly to update the line graphs
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
#             x = i * 8 + 22  # Adjust the x coordinate
#             y = 100 - data[i] / 2  # Adjust the y coordinate
#             coords += [x, y]

#         # Update the line object
#         canvas.coords("line", *coords)

#     # Schedule the next update
#     root.after(500, update_graphs)


# # Create the line objects for each sub-canvas
# for canvas in [canvas1, canvas2, canvas3, canvas4]:
#     canvas.create_line(0, 0, 0, 0, tags="line", fill="purple", width=2)

# # Schedule the first update
# root.after(500, update_graphs)

# # Start the tkinter main loop
# root.mainloop()

import random
import tkinter as tk

# Create the tkinter root window
root = tk.Tk()
root.title("Stacked Line Graphs")

# Create the main canvas
main_canvas = tk.Canvas(root, width=800, height=480)
main_canvas.grid(row=0, column=0)

# Create the four sub-canvases
canvas1 = tk.Canvas(main_canvas, width=200, height=120)
canvas2 = tk.Canvas(main_canvas, width=200, height=120)
canvas3 = tk.Canvas(main_canvas, width=200, height=120)
canvas4 = tk.Canvas(main_canvas, width=200, height=120)

# Position the sub-canvases
canvas1.grid(row=0, column=0)
canvas2.grid(row=0, column=1)
canvas3.grid(row=1, column=0)
canvas4.grid(row=1, column=1)

# Define the data for each line graph
data1 = [random.randint(0, 200) for i in range(20)]
data2 = [random.randint(0, 200) for i in range(20)]
data3 = [random.randint(0, 200) for i in range(20)]
data4 = [random.randint(0, 200) for i in range(20)]

# Create the x-axis and y-axis lines for each sub-canvas
for canvas, data in zip(
    [canvas1, canvas2, canvas3, canvas4], [data1, data2, data3, data4]
):
    canvas.create_line(20, 100, 180, 100, width=2)  # x-axis
    canvas.create_line(20, 100, 20, 20, width=2)  # y-axis

    # Create the line graph for the data
    coords = []
    for i in range(len(data)):
        x = i * 8 + 22  # Adjust the x coordinate
        y = 100 - data[i] / 2  # Adjust the y coordinate
        coords += [x, y]
    canvas.create_line(coords, fill="purple", width=2)


# Call this function repeatedly to update the line graphs
def update_graphs():
    # Update the data for each line graph
    data1.pop(0)
    data1.append(random.randint(0, 200))

    data2.pop(0)
    data2.append(random.randint(0, 200))

    data3.pop(0)
    data3.append(random.randint(0, 200))

    data4.pop(0)
    data4.append(random.randint(0, 200))

    # Update the line objects for each sub-canvas
    for canvas, data in zip(
        [canvas1, canvas2, canvas3, canvas4], [data1, data2, data3, data4]
    ):
        # Update the line coordinates
        coords = []
        for i in range(len(data)):
            x = i * 8 + 22  # Adjust the x coordinate
            y = 100 - data[i] / 2  # Adjust the y coordinate
            coords += [x, y]

        # Update the line object
        canvas.coords("line", *coords)

    # Schedule the next update
    root.after(500, update_graphs)


# Create the line objects for each sub-canvas
for canvas in [canvas1, canvas2, canvas3, canvas4]:
    canvas.create_line(0, 0, 0, 0, tags="line", fill="purple", width=2)

# Schedule the first update
root.after(500, update_graphs)

# Start the tkinter main loop
root.mainloop()

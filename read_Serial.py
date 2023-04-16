import serial

ser = serial.Serial("COM7", 9600)  # replace with the correct port and baud rate

while True:
    while True:
        try:
            line = (
                ser.readline().decode().strip()
            )  # read the line from the serial port and decode it
            break
        except UnicodeDecodeError:
            continue
    values = line.split(
        "\t"
    )  # split the line into separate values using the tab character as a separator

    if len(values) == 4:  # check if the number of values is correct
        try:
            num1 = float(values[0])
            num2 = float(values[1])
            num3 = float(values[2])
            num4 = float(values[3])

            print(num1, num2, num3, num4)

        except ValueError:
            pass  # ignore any lines that cannot be parsed as float values

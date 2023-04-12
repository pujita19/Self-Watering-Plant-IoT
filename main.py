import serial
import time
import csv 

arduino = serial.Serial(port="COM3", baudrate=9600, timeout=0.1)
if not arduino.isOpen():
    arduino.open()
print('com3 is open', arduino.isOpen())
f = open('data.txt', 'wb')

# create the csv writer
# writer = csv.writer(f)

def write_read():
    # arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    # write a row to the csv file
    # writer.writerow(data)
    f.write(data)
    return data
while True:
    # num = input("Enter a number: ") # Taking input from user
    value = write_read()
    print(value) # printing the value

f.close()
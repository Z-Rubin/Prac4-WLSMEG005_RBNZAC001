import busio
import digitalio
import board
import threading
import datetime
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

global chanTemp 
global chanLDR 
global startingTime

def setup():
    global chanTemp
    global chanLDR
    # create the spi bus
    spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

    # create the cs (chip select)
    cs = digitalio.DigitalInOut(board.D5)

    # create the mcp object
    mcp = MCP.MCP3008(spi, cs)

    # create an analog input channel on pin 1
    chanTemp = AnalogIn(mcp, MCP.P1)
    # create an analog input channel on pin 2
    chanLDR = AnalogIn(mcp, MCP.P2)

def fetch_sensor_val():
    global chanTemp
    global chanLDR
    global startingTime
    thread = threading.Timer(10.0, fetch_sensor_val)
    thread.daemon = True  # Daemon threads exit when the program does
    thread.start()
    currentTime = time.time()
    celsiusTemp = (chanTemp.voltage - 0.5)/0.01
    print(round(currentTime-startingTime), 's \t \t', chanTemp.value, '\t \t \t', round(celsiusTemp,1) , 'C' , '\t',chanLDR.value)
   # print('Raw ADC Value: ', chanLDR.value)
    #print('ADC Voltage: ' + str(chanLDR.voltage) + 'V')
    #print('Raw ADC Value: ', chanTemp.value)
    #print('ADC Voltage: ' + str(chanTemp.voltage) + 'V')
    #print(celsiusTemp)
   
if __name__ == "__main__":
    global chanTemp
    global chanLDR
    global startingTime    
    setup()
    startingTime = time.time()
    print('Runtime \t Temp Reading \t \t Temp \t \t Light Reading')
    fetch_sensor_val() # call it once to start the thread
    
    # Tell our program to run indefinitely
    while True:
        pass

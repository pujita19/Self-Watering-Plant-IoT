# Self-Watering-Plant-IoT
IoT project demonstrating automatic watering plant

## Content
* [Introduction and need for project](https://github.com/pujita19/Self-Watering-Plant-IoT#introduction-and-need-for-project)
* [Features of the project](https://github.com/pujita19/Self-Watering-Plant-IoT#features-of-the-project)
* [Devices used](https://github.com/pujita19/Self-Watering-Plant-IoT#devices-used)
* [Code setup / Libraries used](https://github.com/pujita19/Self-Watering-Plant-IoT#code-setup)
* [Circuit](https://github.com/pujita19/Self-Watering-Plant-IoT#circuit)
* [Working](https://github.com/pujita19/Self-Watering-Plant-IoT#working)
* [Real time monitoring](https://github.com/pujita19/Self-Watering-Plant-IoT#real-time-monitoring)
* [Extensions](https://github.com/pujita19/Self-Watering-Plant-IoT#extensions)


## Introduction and need for project
It often happens that we’ve forgotten to water the plants and it has dried or even died. Often this happens due to our schedule in spite of the fact that we are really interested in growing plants. Also when we are far from home for vacation it is difficult to judge the status of the soil and water it if required.

To cater to these needs we will create an automated plant watering system that will use ESP8266 and a capacitive soil moisture sensor with a water pump so we can automatically measure the soil moisture content and water it when the soil becomes dry. The pump will also automatically turn off when the soil is no longer dry.

## Features of the project

The project will include:
* Real time monitoring of moisture of the soil
* Automatic turning on and off of water pump when moisture level is below and above a particular threshold respectively
* Real time display of soil moisture value and watering state on IoT dashboard
* Bonus : Manually toggle water pump, LCD Screen, Threshold controller, Data Analytics

Existing work shows automatic watering feature based on moisture content of soil but not other features like remote monitoring of plant.

## Devices used

* ESP8266
* Capacitive soil moisture sensor
* Relay module
* Mini water pump
* Mini water pipe
* Jumper wires
* DC transformer module
* LCD Screen
* I2C Module

### Soil moisture sensor
The job of a soil moisture sensor is to detect the water content of the soil. When it comes to this category of sensor, we have two options that are Capacitive Soil Moisture Sensor and Resistive Moisture Sensor. As the name indicates a Capacitive soil moisture sensor is based on capacitance changes. Unlike resistive sensors, capacitive sensors do not require direct exposure of the metal electrodes, which can significantly reduce the corrosion of the electrodes.

A capacitive moisture sensor works by measuring the changes in capacitance caused by the changes in the dielectric. Capacitance is proportional to the dielectric medium. The output of a capacitive moisture sensor is an analog value. 

### Watering 
Relay, Pump and pipe are used to water the plant. Relay acts like a switch which a controller can turn on to provide power to the pump. It also acts as a step up transformer incase additional power is needed to the pump to be activated.

## Code Setup
### Install ESP8266 to run in Arduino IDE
The code given is written in IoT Cloud but to run code in Arduino IDE
* Include library <ESP8266WiFi.h> and install ESP8266 Board in Arduino IDE. For installation, go to Arduino IDE and follow the path File/preferences and open the preference tab. Paste the link http://arduino.esp8266.com/stable/package_esp8266com_index.json in the additional board manager URL box. After this, go to Tool/ Board Tools/board/board manager and type ESP8266. You will find a board of ESP8266 click on the install option to get the board installed.
* Arduino code shouldn't contain read write IoT cloud dashboard variables.

### Include LiquidCrystal library for LCD


## Circuit 
### Circuit diagram
![Circuit diagram](/circuit_diagram.png)

### Soil moisture sensor
We used the ESP8266 3.3V to power the soil moisture sensor module. ESP8266 3.3V is connected to the VCC on the sensor and ESP8266 GND is connected to the sensor GND. Since the soil moisture sensor gives analog output, we connected the analog output of the soil moisture sensor (marked as AO) to the analog input pin A0 on the ESP8266 board leaving the D0 of the soil moisture sensor unconnected.

###  Water pump via relay
We connected the water pump to the ESP8266 via the relay. Relay module uses 3.3V power supply from ESP8266. The other side of the relay is connected to the motor pump and adjustable power supply. The voltage of the motor pump is set at 3V only. GND of the relay is connected to ESP8266 GND.

## Working

### Soil moisture percentage
We first held the soil moisture sensor in air and noted the analog reading. This gave us the dry value, let's call it air_value. We then took a glass of water and dipped the sensor in it and read the analog value that gave the wet value, let’s call it water_value. We then mapped the readings of the soil moisture sensor in the range air_value to water_value to 0 and 100 respectively. This gave us soil moisture readings in percentages.

### Variables
We used 
* *moistureValue* (read only float variable which takes values from 0 to 1024) which receives values from the ESP8266 using the soil moisture sensor.
* *moisturePerc* (read only CloudPercentage variable which takes values from 0 to 100) calculated from the moistureValue.
* *pumpState* (read only variable if only automatic watering is needed) as read write variable since manual change of pump state is implemented in this project.

### Triggering water pump
The soil moisture is measured periodically (eg. every 1 sec). Each second, after obtaining the soil moisture percentage, we checked if it is less than some desired value. If yes, we digital write the D0 pin as LOW which sends the LOW signal to relay and turns the pump ON. Similarly, the pump is turned OFF when moisture percentage exceeds a threshold as D0 pin is set to HIGH. 

***Note:*** The pump and relay use opposite signals as said above since pump is connected to NC (normally close) pin of the relay. Instead, one can use NO (normally open) pin to give signal to pump and provide HIGH signal to D0 to turn the pump ON.

## Real time monitoring
We used the IoT Cloud platform to integrate the project and monitor it remotely as it is very beginner friendly. One can write sketches and create variables on the website. The variables used in the sketch can take values from the board or the user using the IoT dashboard.

ESP8266 is connected to the internet using WiFi using the <ESP8266WiFi.h> library. It behaves as a Client/STA and share the soil moisture content (measured via the sensor) and the timing for watering to the IoT dashboard. 
Soil moisture percent at any point of time can be depicted on the dashboard using line chart of IoT cloud dashboard.
The status of pump ON or OFF at any instant of time is also shown on the dashboard using a toggle which can be used to change the status of pump manually (explained in next section).

![iot dashboard](/iot_cloud_dashboard.png)

## Extensions
### Manually toggle water pump
The given setup automatically waters the plant if the moisture content goes below a threshold. We used variable *pumpState* as read write bool variable to toggle the water pump manually using dashboard if needed.

### Data Analytics
For data analytics we collected information about the time it takes for the soil moisture content to change. We collected the data using python serial library and wrote it to a csv file. The soil moisture is plotted after allowing water from the pump to flow dop by drop for around 6 minutes.  We then used this data to analyze trends in the time it takes to increase soil moisture by unit percent. We can see whether the relationship between increase in soil moisture and time taken is linear or exponential etc. Using the data collected, we see that initially the moisture drops very fast, later it becomes saturated.

![moisture graph](/line-graph.png)

### LCD Screen
We display the soil moisture content on an LCD screen (in case the user is not able to view the data on the IoT dashboard due to internet disconnection or other problems). LCD character display will take a large number of GPIO pins if connected directly to the NodeMCU, so we use an I2C board for this. VCC and GND of the I2C board is connected to the 3.3V and ground of ESP8266. SCL pin is connected to D1 and SDA pin to D2. 16 pins of LCD screen will be connected to I2C board. 

### Threshold controller
The desired value of soil moisture needed for each plant might be different. Therefore, we provided an option for users to adjust the threshold percentages using IoT dashboard by keeping the thresholds *lowerbound* and *upperbound* as read write float variables. 


# Self-Watering-Plant-IoT
IoT project demonstrating automatic watering plant

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
Relay, Pump and pipe are used to water the plant. Relay acts like a switch a controller can turn on to provide power to the pump. It also acts as a step up transformer incase additional power is needed to the pump to be activated.

## Circuit 
### Circuit diagram
![Circuit diagram](/circuit_diagram.png)

### Soil moisture sensor
We’ll use the ESP8266 3.3V to power the soil moisture sensor module. We’ll connect the ESP8266 3.3V to VCC on the sensor and ESP8266 GND with sensor GND. Since the soil moisture sensor gives analog output we’ll connect the analog output of the soil moisture sensor (marked as AO) to the analog input pin A0 on the ESP8266 board. We’ll leave the D0 of the soil moisture sensor unconnected.

###  Water pump via relay
We will connect the water pump to the ESP8266 via the relay. Relay module uses 3.3V power supply from ESP8266. The other side of the relay is connected to the motor pump and adjustable power supply. The voltage of the motor pump is set at 3V only. GND of the relay is connected to ESP8266 GND.

## Working
### Soil moisture percentage
We will first simply hold the soil moisture sensor in air and note the analog reading. This will give the dry value, let's call it air_value. We’ll then take a glass of water and dip the sensor in it and read the analog value that gives the wet value, let’s call it water_value. We’ll then map the readings of the soil moisture sensor readings in the range air_value to water_value to 0 and 100 respectively. This will give our soil moisture readings in percentages.

### Triggering water pump
The soil moisture is measured periodically (eg. every 1 sec). Each second, after obtaining the soil moisture percentage, we will check if it is less than some desired value. If yes, we digital write the D0 pin as HIGH which sends the HIGH signal to relay and turns the pump ON. Similarly, the pump is turned OFF when moisture percentage exceeds a threshold as D0 pin is set to LOW.

## Real time monitoring
We are using the IoT Cloud platform to integrate the project and monitor it remotely, as this platform is very beginner friendly. One can write sketches and create variables on the website. The variables used in the sketch can take values from the board or the user using the IoT dashboard.

ESP8266 will be connected to the internet using WiFi using the <ESP8266WiFi.h> library. It will behave as a Client/STA and will share the soil moisture content (measured via the sensor) and the timing for watering to the IoT dashboard. 
Soil moisture percent at any point of time can be depicted on the dashboard using line chart of IoT cloud dashboard.
The status of pump ON or OFF at any instant of time is also shown on the dashboard using a toggle which can be used to change the status of pump manually.

## Extensions

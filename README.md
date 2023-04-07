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
![Circuit diagram](/circuit_diagram.png)

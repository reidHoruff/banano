##Banano

Banano is a realtime gpio remote controll library for embedded linux devices like the Raspberry Pi and Beaglebone Black.


Banano provicdes a client to run on a desktop or other embedded device to use as the control station. This 'control station' can take input from the keyboard or other USB input devices like the mouse or joystick controllers. 

Banano provides a web interface. (Powered by python Flask and nginx) This interface is used ro debiggind and manually controlling the gpio's.


Banano is a high level framework and not an an end user piece of software. The user must provide code to be run on the embedded controller to, at the very least, map HID input from the control station to output pins.


It is also worth noting that Banano currently does none of these things and is in development.

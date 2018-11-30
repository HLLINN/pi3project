# The Golden Pi3project
This is a project that uses a DHT11 sensor to track temperature and humidity indoors.



STEPS:

1.create test_DHT11.py 

2.create gettemp.sh

3.create breathing_lights.py ( add two LEDs flashing alternatively)

4.The last step is :sudo nano ~/.config/lxssession/LXDE-pi/autostart
  Then add @sh /home/pi/pi3project/gettemp.sh
   (refer to ../raspberry/tutorial/shell/ )

This is a simple weather predictor which:

*	Download weather data from a thinkspeak channel in csv format. 
*	Predicts Temperature and Humidity using interpolation method. 
*	Shows predicted data In a basic UI created with Tkinter.


The data is uploaded to the channel  using a nodemcu and dht11: 
*	DHT11 reads the temperature and humidity data. 
*	Nodemcu send the data to thinkspeak channel.

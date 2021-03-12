from microbit import display, sleep, pin0

#init radio
from radio import on, config, send, receive

on() #on radio

config(group=186,queue=1,power=7) #cahnge this manually

while True:
	send(str(display.read_light_level()))
	sleep(10)

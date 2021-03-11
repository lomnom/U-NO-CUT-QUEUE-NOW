from microbit import display, sleep, pin0

#init radio
from radio import on, config, send, receive

on() #on radio

#if sensor recieves less then with light source, its true
#if mocrobit not online, its false
#else, its false

config(group=186,queue=2,power=7) #cahnge this manually

data=[None,0,0]

sleep(1000) #delay

def buzz():
	for i in range(0,29):
		pin0.write_analog(800)
		sleep(500)
		pin0.write_analog(0)
		sleep(500)

#needed vars
iteration=0

dueTime1=0
dueTime2=0

waitingFor1=False
waitingFor2=False

while True: #main  loop
	iteration+=1 #increment iteration
	send("syn") #synchronise devices
	sleep(25) #wait for all microbits to transmit

	for microbit in range(1,2): #data loop
		message=bool(receive()) #read message (microbit's data)
		data[microbit]=message

	if data[1]:
		dueTime2=iteration+280 #set buzzer to buzz 7 secs later if person doesnt exit from other side (280 iterations is 7 secs)
		waitingFor2=True #track if need to track if person exits
		waitingFor1=False #stop waiting
	elif dueTime1>=iteration and waitingFor1: #buzz if after dueTime and waiting
		buzz()

	if data[2]:
		dueTime1=iteration+280#set buzzer to buzz 7 secs later if person doesnt exit from other side
		waitingFor1=True #track if need to track if person exits
		waitingFor2=False#stop waiting
	elif dueTime2>=iteration and waitingFor2: #buzz if after dueTime and waiting
		buzz()

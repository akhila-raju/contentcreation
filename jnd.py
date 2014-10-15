import os, sys, time, datetime

def newParticipant(number):
	if not os.path.exists('Participant' + number):
		print('Creating new folder for Participant' + number + '...')
   		os.makedirs('Participant' + number) # make folder for participant

		print('Creating text files...') # create files in participant folder
		actuators = ['Potentiometer']
		for item in actuators: #record values for each file
			fileName = open(os.path.join('Participant' + number, item + '.csv'), 'w')
			runExperiment(fileName, item)
	else:
		print('Participant folder already exists.')


def runExperiment(fileName, experimentName):
	print('Running ' + experimentName + ' Experiment... ')
	fileName.write('Start: ' + datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
	start = time.time()
	#if (fileName == 'potentiometer'):
		# everytime the button is pressed, record the values
		# control the number of times the button is pressed
		#for each (button press):
		#	fileName.write(value)
		# how do you know when the experiment has ended?
	done = time.time()
	timeElapsed = done - start
	fileName.write('\n End: ' + datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
	fileName.write('\n Time: ' + str(timeElapsed) + ' s')

newParticipant(raw_input('Enter Actuator Name: ')) # running per actuator, not participant

# add command args
# -ls outputs all of the actuator names that we have on file
# -r "actuator name" "id"
# - participant
# fit on power law curve; 2 values = a, k
# visualization - Python's graphing software, export to Tableau
# export it to JSON or CSV
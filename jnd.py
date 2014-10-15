import os, sys, time, datetime

# def newParticipant(number):
# 	if not os.path.exists('Participant' + number):
# 		print('Creating new folder for Participant' + number + '...')
#    		os.makedirs('Participant' + number) # make folder for participant

# 		print('Creating text files...') # create files in participant folder
# 		actuators = ['Potentiometer']
# 		for item in actuators: #record values for each file
# 			fileName = open(os.path.join('Participant' + number, item + '.csv'), 'w')
# 			runExperiment(fileName, item)
# 	else:
# 		print('Participant folder already exists.')

def newActuator(actuatorName, data): #takes in json
	if not os.path.exists(actuatorName):
		print('Creating new folder for ' + actuatorName + '...')
		os.makedirs(actuatorName) # make folder for actuator

		print('Creating participant folders...') # create participant folders within actuator folder
		participants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		experiments = [[light, dark]]
		for item in participants: #record values for each participant
			os.makedirs('Participant ' + participants[item]) # creates participant folders
			fileName = open(os.path.join(actuatorName, item + '.csv'), 'w')
			runExperiment(fileName, actuatorName, experiments[item], item)


def runExperiment(fileName, actuatorName, experimentName, participantNumber):
	print('Running ' + actuatorName + ' ' + sexperimentName + ' Experiment for Participant ' + participantNumber + ' ...')
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

def visualize(folder):
	#go into each participant folder and create a visualization for an experiment of an actuator
	# perform logistic regression
	# visualize by exporting json to D3
	# look into vispy and psychopy

newActuator(raw_input('Enter Actuator Name: ')) # running per actuator, not participant

# add command args
# -ls outputs all of the actuator names that we have on file
# -r "actuator name" "id"
# - participant
# fit on power law curve; 2 values = a, k
# export it to JSON or CSV
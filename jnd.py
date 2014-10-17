import os, sys, time, datetime, json

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

def newActuator(actuatorName, participantNumber):
	if not os.path.exists(actuatorName):
		print('Creating new folder for ' + actuatorName + '...')
		os.makedirs(actuatorName) # make folder for actuator
	print('Creating participant folder...') # create participant subfolder within actuator folder, CSV
	experiments = [["light", "dark"]]
	participant = 'Participant'
	participant += str(participantNumber)
	participantFolder = actuatorName + '/' + participant + '/'
	os.makedirs(participantFolder)
	fileName = open(os.path.join(participantFolder, participantNumber + '.csv'), 'w')
	runExperiment(fileName, actuatorName, experiments[item], item)

def runExperiment(fileName, actuatorName, experimentName, participantNumber):
	print('Running ' + actuatorName + ' ' + experimentName + ' Experiment for Participant ' + participantNumber + ' ...')
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

def exportJson(path):
	f = open(path, 'r')
	arr = []
	headers = []
	for header in f.readline().split(','):
		headers.append(header)

	for line in f.readlines():
		lineItems = {}
		for i,item in enumerate(line.split(',')):
			lineItems[headers[i]] = item
		arr.append(lineitems)

	f.close()

	jsonText = json.dumps(arr)

	#return visualize(jsonText)

#def visualize(jsonText):
	#go into each participant folder and create a visualization for an experiment of an actuator
	# perform logistic regression
	# visualize by exporting json to D3
	# look into vispy and psychopy

actuatorName = raw_input('Enter Actuator Name: ')
participantNumber = raw_input('Participant Number: ')
newActuator(actuatorName, participantNumber)

# running per actuator, not participants
# add command args
# -ls outputs all of the actuator names that we have on file
# -r "actuator name" "id"
# - participant
# fit on power law curve; 2 values = a, k
# export it to JSON or CSV
import os, sys, time, datetime, json
from pylab import *
from scipy.optimize import curve_fit

#Create specified actuator folder and specified participant folder
def newActuator(actuatorName, participantNumber):
	if not os.path.exists(actuatorName):
		print('Creating new folder for ' + actuatorName + '...')
		os.makedirs(actuatorName) # make folder for actuator
	print('Creating participant folder...') # create participant subfolder within actuator folder, CSV
#	experiments = [["light", "dark"]]
	participant = 'Participant'
	participant += str(participantNumber)
	participantFolder = actuatorName + '/' + participant + '/'
	os.makedirs(participantFolder)
	runExperiment(actuatorName, item)

#Create JSON for specified actuator and specifie participant
def runExperiment(actuatorName, participantNumber):
	print('Running ' + actuatorName + ' Experiment for Participant ' + participantNumber + ' ...')
	data = {}
	data['actuator'] = actuatorName
	data['participant'] = participantNumber
	data['startTime'] = str(datetime.datetime.now().strftime("%m/%d/%Y %H:%M"))
	data['x-values'] = 
	data['y-values'] = #function
	#buttonpresses
	json_data = json.dumps(data)

#post json to URL
#def postJson(json):
	#url = "http://localhost:8080" #talk to Jasper about where to post, send Json text
	# r = requests.post(url, data=jsonText), headers=headers)


def regressionFunc(x, a, b, c, d):
    return a*np.exp(-c*(x-b))+d

# def actuatorVis():
# 	#visualization that plots data points of all participants
# 	#plot 
# 	# perform exponential regression
# 	# visualize by exporting json to D3

# def participantVis():
# 	#visualize for a particular participant


actuatorName = raw_input('Enter Actuator Name: ')
participantNumber = raw_input('Participant Number: ')
newActuator(actuatorName, participantNumber)

# running per actuator, not participants
# add command args
# -ls outputs all of the actuator names that we have on file
# -r "actuator name" "id"
# - participant
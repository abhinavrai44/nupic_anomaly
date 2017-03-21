import csv
import datetime
from nupic.data.inference_shifter import InferenceShifter
from nupic.frameworks.opf.modelfactory import ModelFactory
from model_params import model_params
import nupic_output

DATE_FORMAT = "%m/%d/%y %H:%M"

def createModel():
	model = ModelFactory.create(model_params.MODEL_PARAMS)
	model.enableInference({
		"predictedField": "IN_OUT_STATUS"
		})
	return model

def runModel(model):
	inputFilePath = "data1.csv"
	inputFile = open(inputFilePath, "rb")
	csvReader = csv.reader(inputFile)
	csvReader.next()
	csvReader.next()
	csvReader.next()

	#shifter = InferenceShifter()
	#output = nupic_output.NuPICFileOutput(["Rec Center"])


	counter = 0
	for row in csvReader:
		counter += 1
		if(counter % 100 == 0):
			print "Read %i Lines ..." % counter
		employee = int(row[0])
		timestamp = row[1]
		movement = row[2]
		#print "\n\n\n\Employee : %d Movement :" % employee
		result = model.run({
			"EMP_NO" : employee,
			"TIME_OF_SWIPE" : timestamp,
			"IN_OUT_STATUS" : movement
			})

		#result = shifter.shift(result)

		prediction = result.inferences["multiStepBestPredictions"][1]
		anomalyScore = result.inferences["anomalyScore"]
		# print anomalyScore
		#output.write([employee], [timestamp], [movement], [prediction])

	inputFile.close()
	# output.close()



def runPred():
	model = createModel()
	runModel(model)

if __name__ == "__main__":
	runPred()
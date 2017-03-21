import os
import pprint

# add logging to output errors to stdout
import logging
logging.basicConfig()

from nupic.swarming import permutations_runner
from swarm_description import SWARM_DESCRIPTION

def writeModelParams(modelParams):
  outDir = os.path.join(os.getcwd(), "model_params")
  if not os.path.isdir(outDir):
  	os.mkdir(outDir)
  outPath = os.path.join(outDir, "model_params.py")
  pp = pprint.PrettyPrinter(indent = 2)
  with open(outPath, "wb") as outFile:
  	modelParamsString = pp.pformat(modelParams)
  	outFile.write("MODEL_PARAMS = \\\n%s" % modelParamsString)
  return outPath

def swarm(filePath):
  swarmWorkDir = os.path.abspath("swarm")
  if not os.path.exists(swarmWorkDir):
  	os.mkdir(swarmWorkDir)
  modelParams = permutations_runner.runWithConfig(
  	SWARM_DESCRIPTION,
  	{"max_workers": 4, "overwrite": True},
  	outputLabel="rec_center",
  	outDir=swarmWorkDir,
  	permWorkDir=swarmWorkDir
  	)

  writeModelParams(modelParams)



if __name__ == "__main__":
  swarm("data1.csv")

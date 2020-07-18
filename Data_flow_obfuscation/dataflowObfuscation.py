#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
This program is the main program to execute data flow confusion, 
its input is a .sol source code file and the corresponding compiled 
json.ast file, its output is a .sol source code file after data 
flow obfuscation.
'''

import os
import json
import sys
from staticDataDynamicGenerate import staticDataDynamicGenerate
from literal2Exp import literal2Exp
from splitBoolVariable import splitBoolVariable
import time


class dataflowObfuscation:
	def __init__(self, _filepath, _jsonFile):
		self.outputFileName = self.getOutputFileName(_filepath)
		self.solContent = self.getContent(_filepath)
		self.json = self.getJsonContent(_jsonFile)
		self.middleContract = "temp.sol"
		self.middleJsonAST = "temp.sol_json.ast"
		#self.finalContract = _filepath.split(".sol")[0] + "_dataflow_confuse.sol"

	def getOutputFileName(self, _filepath):
		temp = _filepath.split(".sol")
		newFileName = temp[0] + "_dataflow_confuse.sol"
		return newFileName

	def getContent(self, _filepath):
		with open(_filepath, "r", encoding = "utf-8") as f:
			return f.read()
		return str()

	def getJsonContent(self, _jsonFile):
		jsonStr = str()
		with open(_jsonFile, "r", encoding = "utf-8") as f:
			jsonStr = f.read()
		jsonDict = json.loads(jsonStr)
		return jsonDict

	def writeStrToFile(self, _filename, _str, _step):
		with open(_filename, "w", encoding = "utf-8") as f:
			f.write(_str)
		print(_step, ".... done")

	def recompileMiddleContract(self):
		compileResult = os.popen("solc --ast-json --pretty-json --overwrite " + self.middleContract + " -o .")
		#print(compileResult.read())
		print("\rIntermediate contract is being generated.", end = " ")
		time.sleep(1.5)
		print("\rIntermediate contract is being generated....done")
		self.solContent = self.getContent(self.middleContract)
		self.json = self.getJsonContent(self.middleJsonAST)



	def run(self):
		'''
		self.SDDG = staticDataDynamicGenerate(self.solContent, self.json) #SDDG is a class which is used to convert static literal to dynamic generated data
		nowContent = self.SDDG.doGenerate()
		self.writeStrToFile(self.middleContract, nowContent, "Dynamically generate static data")
		self.recompileMiddleContract()
		self.L2E = literal2Exp(self.solContent, self.json) #L2E is a class which is used to convert integer literal to arithmetic expressions
		nowContent = self.L2E.doGenerate()
		self.writeStrToFile(self.middleContract, nowContent, "Convert integer literals to arithmetic expressions")
		'''
		self.SBV = splitBoolVariable(self.solContent, self.json)
		self.SBV.doSplit()

#unit test
if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("wrong parameters.")
	else:
		dfo = dataflowObfuscation(sys.argv[1], sys.argv[2])
		dfo.run()
		#print(dfo.solContent)

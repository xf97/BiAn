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


class dataflowObfuscation:
	def __init__(self, _filepath, _jsonFile):
		self.outputFileName = self.getOutputFileName(_filepath)
		self.solContent = self.getContent(_filepath)
		self.json = self.getJsonContent(_jsonFile)
		self.SDDG = staticDataDynamicGenerate(self.solContent, self.json) #SDDG is a class which is used to convert literal to dynamic generated data 

	def getOutputFileName(self, _filepath):
		temp = _filepath.split(".")
		newFileName = temp[0] + "_dataflow_confuse." + temp[1]
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

	def writeStrToFile(self, _filename, _str):
		with open(_filename, "w", encoding = "utf-8") as f:
			f.write(_str)
		print(_filename, "is writed.")

	def run(self):
		self.SDDG.doGenerate()


#unit test
if __name__ == "__main__":
	dfo = dataflowObfuscation("testCase/constant2Variable.sol", "testCase/constant2Variable.sol_json.ast")
	#print(dfo.solContent)
	dfo.run()
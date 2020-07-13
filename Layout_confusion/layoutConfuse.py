#!/bin/usr/python
#-*- coding: utf-8 -*-


'''
This Python program is the main Python file that performs layout confusion. 
The file provides input, output, and call-related operations for layout obfuscation.
input: sol's json_ast
'''

import os
import sys
import json
from replaceVarName import replaceVarName
from splitFunction import splitFunction


class layoutConfuse:
	def __init__(self, _filepath, _jsonFile):
		self.outputFileName = self.getOutputFileName(_filepath)
		self.solContent = self.getContent(_filepath)
		self.json = self.getJsonContent(_jsonFile)
		self.RVN = replaceVarName(self.solContent, self.json) # RVN is the class that performs "Replace Variable Name" operation

	def getContent(self, _filepath):
		with open(_filepath, "r", encoding = "utf-8") as f:
			return f.read()
		return str()

	def getOutputFileName(self, _filepath):
		temp = _filepath.split(".")
		newFileName = temp[0] + "_layout_confuse." + temp[1]
		return newFileName

	def getJsonContent(self, _jsonFile):
		jsonStr = str()
		with open(_jsonFile, "r", encoding = "utf-8") as f:
			jsonStr = f.read()
		jsonDict = json.loads(jsonStr)
		return jsonDict

	def doReplace(self):
		replacedContent = self.RVN.doReplace()
		return replacedContent

	def writeStrToFile(self, _filename, _str):
		with open(_filename, "w", encoding = "utf-8") as f:
			f.write(_str)
		print(_filename, "is writed.")

	#first - split contract
	#second - split function
	#third - replace name
	def run(self):
		#print(self.solContent)
		#print(self.outputFileName)
		#print(self.json)
		'''
		replacedNameContent = self.doReplace()
		self.writeStrToFile("testCase/temp.sol", replacedNameContent)
		'''
		#print(self.solContent.find("uint256") + len("uint256"))
		print(self.solContent[376:(376+84)])


#unit test
if __name__ == "__main__":
	lc = layoutConfuse("testCase/testCase1.sol", "testCase/testCase1_json.ast")
	lc.run()

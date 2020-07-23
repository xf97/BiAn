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
from changeFormat import changeFormat
from deleteComment import deleteComment
import time


class layoutConfuse:
	def __init__(self, _filepath, _jsonFile):
		self.outputFileName = self.getOutputFileName(_filepath)
		self.solContent = self.getContent(_filepath)
		self.json = self.getJsonContent(_jsonFile)		
		self.middleContract = "temp.sol"
		self.middleJsonAST = "temp.sol_json.ast"
		self.configPath = "Configuration.json"
		self.getConfig()
	
	def getConfig(self):
		config = self.getJsonContent(self.configPath)
		self.featureList = config["activateFunc"]

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

	def isActivate(self, _name):
		for _dict in self.featureList:
			try:
				return _dict[_name]
			except:
				continue
		return True

	def run(self):
		if self.isActivate("deleteComment"):
			self.DC = deleteComment(self.solContent)
			nowContent = self.DC.doDelete()
		if self.isActivate("changeFormat"):
			self.CF = changeFormat(nowContent)
			nowContent = self.CF.doChange()
			self.writeStrToFile("temp.sol", nowContent, "Delete comments, disrupt the formatting")
			self.recompileMiddleContract()
		if self.isActivate("replaceVarName"):
			self.RVN = replaceVarName(self.solContent, self.json) # RVN is the class that performs "Replace Variable Name" operation
			nowContent = self.RVN.doReplace()
			self.writeStrToFile("temp.sol", nowContent, "Replace variable name")



#unit test
if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("wrong parameters.")
	else:
		lc = layoutConfuse(sys.argv[1], sys.argv[2])
		lc.run()
		#print(dfo.solContent)


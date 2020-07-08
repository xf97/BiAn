#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
This python file is part of the layout obfuscation and 
is used to replace variable names with less readable 
strings (currently hash values).
'''

import os
import json
import sys
import re

class replaceVarName:
	def __init__(self, _solContent, _jsonContent):
		self.content = _solContent
		self.json = _jsonContent
		#print(type(self.json))

	def getNames(self, _json):
		#dictList = list()
		#dictList.append(_json)
		varName = self._getName(_json, "name", "ElementaryTypeName")
		idenName = self._getName(_json, "name", "Identifier")
		print(varName)
		print(idenName)

	def getDictName(self, _dict):
		for key in _dict:
			if key == "attributes":
				print(_dict["attributes"])
				'''
				if _dict["attributes"].get("value") != None:
					print(_dict["value"])
					return _dict["value"]
					'''


	def _getName(self, _json, _key, _value):
		#print(_key)
		queue = [_json]
		result = list()
		while len(queue) > 0:
			data = queue.pop()
			#print(data)
			for key in data:
				#print(key)
				if key == _key and data[key] == _value:
					name = self.getDictName(data)
					result.append(name)
				elif type(data[key]) == dict:
					queue.append(data[key])
				elif type(data[key]) == list:
					for item in data[key]:
						if type(item) == dict:
							queue.append(item)
		return result
		'''
		print("hahaha")
		dictList = list()
		for _dict in _dictList:
			for key in _dict:
				print(key)
				if isinstance(_dict[key], dict):
					print("lalala")
					dictList.append(_dict[key])
				elif key == _key and _dict.get(key) == _value:
					print(_dict[key])
		if len(dictList) != 0:
			self._getName(dictList, _key, _value)
		for key in _json:
			if key == "children":
				newDict =  _json[key][1]
				for innerKey in newDict:
					if innerKey == "children":
						newNewDict = newDict[innerKey][0]
						print(newNewDict)
						print("")
						if newNewDict.get(_key) == _value:
							print(newNewDict[_key])
		'''


	def doReplace(self):
		#1. get names of all variables and identifiers
		nameList = self.getNames(self.json)
		'''
		replacedResult = self.content
		#2. Replace the name of each variable and identifier with a hash value
		for name in nameList:
			replacedResult = replace1Name(replacedResult, name)
		#3. return result
		return replacedResult
		'''
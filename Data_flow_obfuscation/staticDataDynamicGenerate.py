#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
This part of the program is used to convert 
the constants (address, integer, string, he-
xadecimal) in the contract into dynamically 
generated data without affecting the original 
function of the contract.
'''

'''
key points:
Solidity is a limited language, as is Ethereum.
'''

import os
import json
import sys

ADDRESS_FLAG = "address"
STRING_FLAG = "string"
INT_FLAG = "int"

CORPUS_PATH = "Corpus.txt"


class staticDataDynamicGenerate:
	def __init__(self, _solContent, _jsonContent):
		self.content = _solContent
		self.json = _jsonContent

	def doGenerate(self):
		#1. find each literal 
		literalList = self.findLiteral(self.json, "name", "Literal")
		#2. generate each literal's replacement
		#2.1 declare array to store literal
		typeList = self.getLiteralType(literalList)
		nowContent = self.content
		insertPosition = self.getContractEnd()
		#print(insertPosition)
		#2.2 write getter function into contract
		for _type in typeList:
			if _type == ADDRESS_FLAG:
				nowContent = self.insertFunc(nowContent, _type)
			elif _type == STRING_FLAG:
				nowContent = self.insertFunc(nowContent, _type)
			elif _type == INT_FLAG:
				nowContent = self.insertFunc(nowContent, _type)
			else:
				continue

	def getContractEnd(self):
		_list = self.findLiteral(self.json, "name", "ContractDefinition")
		contractEnd = list()
		temp = list()
		for _dict in _list:
			temp.append(_dict["src"])
		for item in temp:
			print(self.listToInt(item.split(":")))


	def listToInt(self, _list):
		totalSum = 0
		for num in _list:
			totalSum += int(num)
		return totalSum




	#TO DO (TOB)
	def insertFunc(self, _content, _type):
		corpusDict = dict()
		with open(CORPUS_PATH, "r", encoding  = "utf-8") as f:
			corpusDict = json.loads(f.read())
		intStr = str()
		for item in corpusDict:
			if item.get("type") == "getIntFunction" and _type == INT_FLAG:
				intStr = item.get("functionHeadAndBody")
			elif item.get("type") == "getStrFunction" and _type == STRING_FLAG:
				intStr = item.get("functionHeadAndBody")
			elif item.get("type") == "getAddrFunction" and _type == ADDRESS_FLAG:
				intStr = item.get("functionHeadAndBody")






		#self.declareAndInitArray(literalList, self.content, self.json)
		'''
		for literal in literalList:
			typeList = 
		return self.content
		'''

	def getLiteralType(self, _list):
		typeList = list()
		for _dict in _list:
			try:
				typeList.append(_dict["attributes"]["type"].split()[0])
			except:
				continue
		return list(set(typeList))


	def findLiteral(self, _json, _key, _value):
		queue = [_json]
		result = list()
		literalList = list()
		while len(queue) > 0:
			data = queue.pop()
			for key in data:
				if key == _key and  data[key] == _value:
					result.append(data)
				elif type(data[key]) == dict:
					queue.append(data[key])
				elif type(data[key]) == list:
					for item in data[key]:
						if type(item) == dict:
							queue.append(item)
		return result
		'''
		for _dict in result:
			literalList.append(self.getLiteralName(_dict))
		#print(literalList)
		return literalList
		'''

	def getLiteralName(self, _dict):
		try:
			value = _dict["attributes"]["value"]
			location = _dict["src"]
			return value, location
		except:
			return "hex literal is not supported.", 0





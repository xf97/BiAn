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
STRING_FLAG = "literal_string"
INT_FLAG = "int_const"

CORPUS_PATH = "Corpus.txt"

START_FLAG = 1
END_FLAG = 2


class staticDataDynamicGenerate:
	def __init__(self, _solContent, _jsonContent):
		self.content = _solContent
		self.json = _jsonContent
		self.corpusDict = self.getCorpus()

	def getCorpus(self):
		corpusDict = dict()
		with open(CORPUS_PATH, "r", encoding  = "utf-8") as f:
			corpusDict = json.loads(f.read())
		#print(corpusDict,"kkkkkkkk")
		return corpusDict

	def doGenerate(self):
		#1. find each literal 
		literalList = self.findLiteral(self.json, "name", "Literal")
		#2. generate each literal's replacement
		#2.1 declare array to store literal
		typeList = self.getLiteralType(literalList)
		nowContent = self.content
		insertPosition = self.getContractStartOrEnd(END_FLAG)
		#2.2 write getter function into contract
		#print(typeList)
		for _type in typeList:
			if _type == ADDRESS_FLAG:
				(nowContent, insertPosition) = self.insertFunc(nowContent, insertPosition, _type)
			elif _type == STRING_FLAG:
				(nowContent, insertPosition) = self.insertFunc(nowContent, insertPosition, _type)
			elif _type == INT_FLAG:
				(nowContent, insertPosition) = self.insertFunc(nowContent, insertPosition, _type)
			else:
				continue	
		#2.3 insert variable - array
		for _type in typeList:
			if _type == ADDRESS_FLAG:
				pass
			elif _type == STRING_FLAG:
				pass
			elif _type == INT_FLAG:
				pass
			else:
				continue


		print(nowContent)

	def getContractStartOrEnd(self, _flag):
		_list = self.findLiteral(self.json, "name", "ContractDefinition")
		#contractEnd = list()
		temp = list()
		for _dict in _list:
			temp.append(_dict["src"])
		if _flag == END_FLAG:
			return self.listToInt(temp[0].split(":"))
		elif _flag == START_FLAG:
			return self.listToInt(temp[0].split(":")[0])
		'''
		for item in temp:
			contractEnd.append(self.listToInt(item.split(":")))
		return contractEnd
		'''


	def listToInt(self, _list):
		totalSum = 0
		for num in _list:
			totalSum += int(num)
		return totalSum

	def insertFunc(self, _content, _position, _type):
		intStr = str()
		for item in self.corpusDict:
			if item == "insertFunc":
				for _dict in self.corpusDict[item]:
					if _type == INT_FLAG and _dict.get("type") == "getIntFunction":
						intStr = _dict.get("functionHeadAndBody")
					elif  _type == STRING_FLAG and _dict.get("type") == "getStrFunction":
						intStr = _dict.get("functionHeadAndBody")
					elif  _type == ADDRESS_FLAG and _dict.get("type") == "getAddrFunction":
						intStr = _dict.get("functionHeadAndBody")
		#print(self.strInsert(_content, intStr, _position))#, _position + len(intStr))
		return self.strInsert(_content, intStr, _position), _position + len(intStr)

    #Inserting a substr into another str at specific position
	def strInsert(self, _oldContent, _insertContent, _position):
		return _oldContent[:_position - 1] + _insertContent + _oldContent[_position - 1:]

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





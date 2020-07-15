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
import re

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
		#insertPosition = self.getContractStartOrEnd(START_FLAG)
		arrayList = list()
		for _type in typeList:
			if _type == ADDRESS_FLAG:
				(nowContent, insertPosition, array) = self.insertArrayDeclare(nowContent, insertPosition, _type)
				arrayList.append(array)
			elif _type == STRING_FLAG:
				(nowContent, insertPosition, array) = self.insertArrayDeclare(nowContent, insertPosition, _type)
				arrayList.append(array)
			elif _type == INT_FLAG:
				(nowContent, insertPosition,array) = self.insertArrayDeclare(nowContent, insertPosition, _type)
				arrayList.append(array)
			else:
				continue
		#3. find all literals and replace it 
		insertList = list()
		for _dict in literalList:
			(_type, value, startPos, endPos) = self.getLiteralInfor(_dict)
			callStatement = self.makeCallStatement(arrayList, _type, value)
			nowContent = re.sub(r"=(\s)*" + str(value) + r"(\s)*;", callStatement, nowContent)
		print(nowContent)

	def strReplace(self, _oldContent, _insertContent, _startPos, _endPos):
		return _oldContent[startPos:] + _insertContent + _oldContent[:endPos]

	def makeCallStatement(self, _array, _type, _value):
		flag = self.reMakeType(_type)
		for state in _array:
			if flag == state.split()[0]:
				valueList = self.getArrayElement(state, _type)
				for index in range(len(valueList)):
					if str(_value) == valueList[index] and _type == INT_FLAG:
						return " = getIntFunc(" + str(index) + ");"
					elif str(_value) == valueList[index] and _type == ADDRESS_FLAG:
						return " = getAddrFunc(" + str(index) + ");"
					elif  _type == STRING_FLAG and  _value == valueList[index].strip("\""):
						return " = getStrFunc(" + str(index) + ");"
		return str()

	def getArrayElement(self, _state, _type):
		temp = _state.split("=")[1]
		result = list()
		if _type == INT_FLAG:
			for i in re.finditer(r"(\d)+", temp):
				result.append(i.group())
		elif _type == ADDRESS_FLAG:
			for i in re.finditer(r"((0x)|(0X))?(\w){39,41}", temp):
				result.append(i.group())
		elif _type == STRING_FLAG:
			for i in re.finditer(r"(\")(.)*(\")", temp):
				result.append(i.group())
		#print(result)
		return result

	def reMakeType(self, _type):
		if _type == INT_FLAG:
			return "uint256[]"
		elif _type == STRING_FLAG:
			return "string[]"
		elif _type == ADDRESS_FLAG:
			return "address"

	def getLiteralInfor(self, _dict):
		try:
			startPos = _dict["src"].split(":")[0]
			endPos = int(_dict["src"].split(":")[1]) + int(startPos)
			_type = _dict["attributes"]["type"].split()[0]
			if _type == INT_FLAG:
				_value = _dict["attributes"]["type"].split()[1]
			elif _dict["attributes"]["value"] == None:
				return 0, 0, 0, 0
			else:
				_value = _dict["attributes"]["value"]
			return _type, _value, startPos, endPos
		except:
			return 0, 0, 0, 0



	def insertArrayDeclare(self, _content, _position, _type):
		intStr = str()
		for item in self.corpusDict:
			if item == "insertVariable":
				for _dict in self.corpusDict[item]:
					if _type == INT_FLAG and _dict.get("type") == "UintArrayDeclare":
						intStr = _dict.get("variableDeclaration")
						intStr += self.getValue(_type)
					elif  _type == STRING_FLAG and _dict.get("type") == "StringArrayDeclare":
						intStr = _dict.get("variableDeclaration")
						intStr += self.getValue(_type)
					elif  _type == ADDRESS_FLAG and _dict.get("type") == "AddressArrayDeclare":
						intStr = _dict.get("variableDeclaration")
						intStr += self.getValue(_type)
		#print(self.strInsert(_content, intStr, _position))#, _position + len(intStr))
		return self.strInsert(_content, intStr, _position - 1), _position + len(intStr), intStr

	def getValue(self, _type):
		typeList = self.findLiteral(self.json, "name", "Literal")
		valueList = list()
		for _dict in typeList:
			try:
				if _type != INT_FLAG and _type == _dict["attributes"]["type"].split()[0]:
					valueList.append(_dict["attributes"]["value"])
				elif _type == INT_FLAG and _type == _dict["attributes"]["type"].split()[0]:
					valueList.append(_dict["attributes"]["type"].split()[1])
			except:
				continue
		valueList = self.filterList(valueList)
		intStr = str()
		if _type == INT_FLAG:
			for num in valueList:
				if valueList.index(num) == len(valueList) - 1:
					intStr += num
				else:
					intStr += num
					intStr += ", "
			intStr += "];\n"
		elif _type == ADDRESS_FLAG:
			for addr in valueList:
				if valueList.index(addr) == len(valueList) - 1:
					intStr += addr
				else:
					intStr += addr 
					intStr += ", "
			intStr += "];\n"
		elif _type == STRING_FLAG:
			for string in valueList:
				if valueList.index(string) == len(valueList) - 1:
					intStr += "\"" + string + "\""
				else:
					intStr += "\"" + string + "\""
					intStr += ", "
			intStr += "];\n"
		return intStr

	def filterList(self, _list):
		temp = _list
		for item in temp:
			if item == None:
				temp.remove(item)
		return list(set(temp))

	def getContractStartOrEnd(self, _flag):
		_list = self.findLiteral(self.json, "name", "ContractDefinition")
		#contractEnd = list()
		temp = list()
		for _dict in _list:
			temp.append(_dict["src"])
		if _flag == END_FLAG:
			return self.listToInt(temp[0].split(":"))
		elif _flag == START_FLAG:
			return self.listToInt([temp[0].split(":")[0]])
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
		return self.strInsert(_content, intStr, _position - 1), _position + len(intStr)

    #Inserting a substr into another str at specific position
	def strInsert(self, _oldContent, _insertContent, _position):
		return _oldContent[:_position] + _insertContent + _oldContent[_position:]

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





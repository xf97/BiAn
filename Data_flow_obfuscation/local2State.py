#!/usr/bin/python
#-*- coding: utf-8 -*-

import json
from noTouchPure import noTouchPure
import random
import copy

DEFAULT_VISIBILITY = "internal"
CORPUS_PATH = "Corpus.txt"

class local2State:
	def __init__(self, _solContent, _jsonContent):
		self.content = _solContent
		self.json  = _jsonContent
		self.NTP = noTouchPure(self.json)
		self.corpusDict = self.getCorpus()

	def findASTNode(self, _key, _value):
		queue = [self.json]
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

	def findLocalVar(self):
		varList = self.findASTNode("name", "VariableDeclaration")
		localVarList = list()
		for node in varList:
			try:
				if node["attributes"].get("stateVariable") == False:
					localVarList.append(node)
				else:
					continue
			except:
				continue
		return localVarList

	def srcToPos(self, _str):
		_list = _str.split(":")
		return [int(_list[0]), int(_list[0]) + int(_list[1])]

	def getCorpus(self):
		corpusDict = dict()
		with open(CORPUS_PATH, "r", encoding  = "utf-8") as f:
			corpusDict = json.loads(f.read())
		#print(corpusDict,"kkkkkkkk")
		return corpusDict

	def processSameName(self, _list):
		resultList = list()
		temp = list()
		nameDict = dict()
		for node in _list:
			try:
				name = node["attributes"].get("name")
				if name == "":
					continue
				else:
					sPos, ePos = self.srcToPos(node["src"])
					sPos = int(ePos) - len(name)
					_id = node["id"]
					temp.append([name, int(sPos), int(ePos), int(_id)])
			except:
				continue
		# check whether there are duplicate names.
		for _name in temp:
			nameDict[_name[0]] = 0
		for _name in temp:
			nameDict[_name[0]] += 1
		for _name in nameDict:
			if nameDict[_name] >  1:
				resultList.extend(self.reName(_name, temp))
		#Find all identifiers that use the same local variable name
		tempList = copy.deepcopy(resultList)
		for item in tempList:
			resultList.extend(self.findSameNameState(item))
		return resultList

	def findSameNameState(self, _node):
		identifierList = self.findASTNode("name", "Identifier")
		#print(len(identifierList))
		resultList = list()
		for iden in identifierList:
			if iden["attributes"].get("referencedDeclaration") == _node[3]:
				sPos, ePos =  self.srcToPos(iden["src"])
				resultList.append([_node[0], sPos, ePos, _node[3]])
			else:
				continue
		return resultList

	def shuffleStr(self, _str):
		strList = list(_str)
		result = str()
		random.shuffle(strList)
		for char in strList:
			result += char
		return result

	def reName(self, _name, _list):
		resultList = list()
		for item in _list:
			if item[0] == _name:
				newName = self.corpusDict["variableNaming"][random.randint(0, len(self.corpusDict["variableNaming"]) - 1)]
				newName = self.shuffleStr(newName)
				resultList.append([newName, item[1], item[2], item[3]])
			else:
				continue
		return resultList

	def strReplace(self, _oldContent, _list):
		temp = str()
		sliceIndex = list()
		for item in _list:
			if item[1] == 0 and item[2] == 0:
				continue
			else:
				sliceIndex.append(int(item[1]))
				sliceIndex.append(int(item[2]))
		#sliceIndex = self.filterList(sliceIndex)
		sliceIndex.sort()	# from small to big
		flag = 0
		index = 0
		while flag < len(sliceIndex):
			if flag % 2 == 0:
				temp += _oldContent[index : sliceIndex[flag]]
				index = sliceIndex[flag]
				flag += 1
			else:
				temp += self.getNewName(_list, index, sliceIndex[flag])
				index = sliceIndex[flag] 
				flag += 1
		temp += _oldContent[index : ]
		return temp

	def getNewName(self, _list, _sPos, _ePos):
		for item in _list:
			if item[1] == _sPos and item[2] == _ePos:
				return item[0]
			else:
				continue
		return str()

	def resetSolAndJson(self, _solContent, _jsonContent):
		self.content = _solContent
		self.json = _jsonContent

	def preProcess(self):
		#1. find all local varibale
		localVarList = self.findLocalVar()
		localVarList = self.NTP.run(localVarList)
		'''
		for i in localVarList:
			print(i)
		'''
		#2. Process variables with the same name
		sameNameList = self.processSameName(localVarList)
		#print(sameNameList)
		#3. re-specific variables' names 
		nowContent =  self.content
		nowContent = self.strReplace(nowContent, sameNameList)
		return nowContent

	def filterPara(self, _list):
		result = list()
		for i in _list:
			if i["attributes"].get("name") == "":
				continue
			else:
				result.append(i)
		return result

	def makeDeclareState(self, _list):
		declareState = str()
		for var in _list:
			sPos, ePos = self.srcToPos(var["src"])
			declareState +=  "\t"
			declareState += self.content[sPos:ePos]
			declareState += ";\n"
		return declareState



	def doChange(self):
		#1. find all local varibale
		localVarList = self.findLocalVar()
		localVarList = self.NTP.run(localVarList)
		localVarList = self.filterPara(localVarList)
		'''
		for i in localVarList:
			sPos, ePos = self.srcToPos(i["src"])
			print(self.content[sPos:ePos])
			#print(self.srcToPos(i["src"]))
		'''
		#2. make declaration statement
		print(self.makeDeclareState(localVarList))
		#3. Overwrite the original variable declaration statement.

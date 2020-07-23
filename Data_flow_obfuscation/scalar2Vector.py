#!/usr/bin/python
#-*- coding: utf-8 -*-

import json

BOOL_FLAG = "bool"
INT_FLAG = "int"
ADDRESS_FLAG = "address"
ADDRESS_PAYABLE_FLAG = "address payable"
STRING_FLAG = "string"
BYTES_FLAG = "bytes"

CORPUS_PATH = "Corpus.txt"

class scalar2Vector:
	def __init__(self, _solContent, _jsonContent):
		self.content = _solContent
		self.json = _jsonContent
		self.corpusDict = self.getCorpus()
		self.mapping = dict()

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

	def findStateVar(self, _list):
		temp = list()
		for node in _list:
			try:
				if node["attributes"].get("stateVariable") == True:
					temp.append(node)
				else:
					continue
			except:
				continue
		return temp

	def findTargetType(self, _list):
		temp = list()
		for node in _list:
			try:
				if node["attributes"].get("type") == BOOL_FLAG:
					temp.append(node)
				elif node["attributes"].get("type").find(INT_FLAG) != -1 and \
				node["attributes"].get("type").find("[") == -1:
					temp.append(node)
				elif node["attributes"].get("type") == ADDRESS_FLAG or \
				node["attributes"].get("type") == ADDRESS_PAYABLE_FLAG:
					temp.append(node)
				elif node["attributes"].get("type") == STRING_FLAG:
					temp.append(node)
				elif node["attributes"].get("type") == BYTES_FLAG:
					temp.append(node)
				else:
					continue
			except:
				continue
		return temp

	def srcToPos(self, _str):
		_list = _str.split(":")
		return int(_list[0]), int(_list[0]) + int(_list[1])

	def getNodeInfo(self, _list):
		infoList = list()
		for node in _list:
			name = node["attributes"].get("name")
			_type = node["attributes"].get("type")
			_id = node["id"]
			(sPos, ePos) = self.srcToPos(node["src"])
			infoList.append([name, _type, _id, (sPos,  ePos)])
		return infoList


	def findTargetVar(self):
		nodeList = self.findASTNode("name", "VariableDeclaration")
		# 过滤非状态变量
		stateVarList = self.findStateVar(nodeList)
		# 过滤非目标类型变量
		targetVarList = self.findTargetType(stateVarList)
		# 获取目标信息
		infoList = self.getNodeInfo(targetVarList)
		return infoList

	def getCorpus(self):
		corpusDict = dict()
		with open(CORPUS_PATH, "r", encoding  = "utf-8") as f:
			corpusDict = json.loads(f.read())
		#print(corpusDict,"kkkkkkkk")
		return corpusDict

	def makeDeclareStatement(self, _list):
		structPre = self.corpusDict["insertStructPrefix"]
		_str = str()
		for node in _list:
			#声明变量时，表明对应关系
			self.mapping[node[0]] = node[2]
			_str += node[1]
			_str += " "
			_str += node[0]
			if _list.index(node) == len(_list) - 1:
				_str += ";\n"
			else:
				_str += ";\n\t\t"
		structPre += _str
		structPre += "\t}"
		structPre += self.corpusDict["insertStructSuffix"]
		return structPre

	def strInsert(self, _oldContent, _insertContent, _position):
		return _oldContent[:_position] + _insertContent + _oldContent[_position:]

	def insertStruIntoContract(self, _content, _str):
		sPos, ePos = self.srcToPos(self.findASTNode("name", "ContractDefinition")[0]["src"])
		return self.strInsert(_content, _str, ePos - 1)


	#node info: name type id (sPos, ePos)
	def doChange(self):
		#1. 获取目标状态变量信息
		infoList = self.findTargetVar()
		#2. 在合约内部声明结构体——语料库
		declareStatement = self.makeDeclareStatement(infoList)
		#print(declareStatement)
		#3. 插入声明语句
		nowContent = self.content
		nowContent = self.insertStruIntoContract(nowContent, declareStatement)
		print(self.mapping)
		return nowContent
		'''
		for i in infoList:
			print(i)
		'''

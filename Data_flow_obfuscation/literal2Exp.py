#!/usr/bin/python
#-*- coding: utf-8 -*-

import random
from generateExp import generateExp

INT_FLAG = "int_const"

class literal2Exp:
	def __init__(self, _solContent, _jsonContent):
		self.content = _solContent
		self.json = _jsonContent

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

	def getIntNode(self, _list):
		result = list()
		for node in _list:
			try:
				if node["attributes"].get("type").split()[0] == INT_FLAG:
					result.append(node)
				else:
					continue
			except:
				continue
		return result

	def getNodeInfor(self, _node):
		try:
			value = _node["attributes"]["type"].split()[1]
			startPos = int(_node["src"].split(":")[0])
			endPos = int(_node["src"].split(":")[1])
			return value, startPos, endPos
		except:
			return 0, 0, 0

	def generateExp(self, _str):
		ge = generateExp(int(_str))
		return ge.main()

	def replaceContent(self, _content, _exp, _startPos, _endPos):
		return _content[: _startPos] + _exp + _content[(_startPos + _endPos):]

	def doGenerate(self):
		#1. find each literal
		literalList = self.findASTNode("name", "Literal")
		#2. find int literals in all literals
		intLiteralList = self.getIntNode(literalList)
		#3. get literal's  value and position
		intNodeInfor = list()
		for node in intLiteralList:
			(value, startPos, endPos) = self.getNodeInfor(node)
			intNodeInfor.append([value, startPos, endPos])
		#print(intNodeInfor)
		#4. generate corresponding exp
		for node in intNodeInfor:
			#print(node)
			exp = self.generateExp(node[0])
			node[0] = exp
		#5. replace literal
		nowContent = self.content
		for node in intNodeInfor:
			#print(node)
			nowContent = self.replaceContent(nowContent, node[0], node[1], node[2])
		return nowContent

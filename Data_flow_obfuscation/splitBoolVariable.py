#!/usr/bin/python
#-*- coding: utf-8 -*-

class splitBoolVariable:
	def __init__(self, _solContent, _jsonContent):
		self.content = _solContent
		self.json = _jsonContent

	def findBoolList(self):
		nodeList = self.findASTNode("name", "VariableDeclaration")
		#nodeList.extend(self.findASTNode("name", "VariableDeclarationStatement"))
		resultList = list()
		for node in nodeList:
			try:
				if node["attributes"].get("type") == "bool":
					name = node["attributes"].get("name")
					_id = node["id"]
					if name != "":
						resultList.append([name, _id])
					else:
						continue
				else:
					continue
			except:
				continue
		return resultList

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

	def filterBoolVariable(self, _list):
		boolList = list()
		for node in _list:
			try:
				_id = node.get("id")
				#value = node["attributes"].get("value")
				boolList.append(_id)
			except:
				continue
		return boolList

	def findStatement(self):
		resultList = list()
		resultList.extend(self.findASTNode("name", "VariableDeclaration"))
		resultList.extend(self.findASTNode("name", "VariableDeclarationStatement"))
		resultList.extend(self.findASTNode("name", "Assignment"))
		return resultList


	def doSplit(self):
		#1. 先找到每个布尔型变量的名字和id
		boolList = self.findBoolList()
		#print(boolList)
		#2. 找到每个VariableDeclaration、VariableDeclarationStatement、Assignment节点
		statementList = self.findStatement()
		boolOpeStatement = list()
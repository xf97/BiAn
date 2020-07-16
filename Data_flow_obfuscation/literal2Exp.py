#!/usr/bin/python
#-*- coding: utf-8 -*-

import random

INT_FLAG = "int_const"

class literal2Exp:
	def __init__(self, _solContent, _jsonContent):
		self.content = _solContent
		self.json = _jsonContent

	def findASTNode(self, _name, _value):
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

	def generateExp(self):
		#1. find each literal
		literalList = self.findASTNode("name", "Literal")
		#2. find int literals in all literals
		intLiteralList = self.getIntNode()
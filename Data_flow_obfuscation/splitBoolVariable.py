#!/usr/bin/python
#-*- coding: utf-8 -*-

class splitBoolVariable:
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

	def doSplit(self):
		#1. get each bool literal
		print(self.content[334:379])
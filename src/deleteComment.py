#!/usr/bin/python
#-*- coding: utf-8 -*-

import re

class deleteComment:
	def __init__(self, _solContent):
		self.content = _solContent

	def deleteSingleComment(self, _content):
		pattern = r"//(.)*(\n)?"
		return re.sub(pattern, "", _content)

	def deleteMultiComment(self, _content):
		pattern = r"/\*((.)|((\r)?\n))*?\*/"
		return re.sub(pattern, "", _content, re.S)

	def doDelete(self):
		nowContent = self.content
		#print(nowContent)
		#1. delete the single-line comment
		nowContent = self.deleteSingleComment(nowContent)
		#print(nowContent)
		#2. delete the multi-line comment
		nowContent = self.deleteMultiComment(nowContent)
		#print("hahaha", nowContent)
		return nowContent
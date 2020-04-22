#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
__author__ = xf97
__StartDate__ = 2020/4/22
This program takes the smart contract bytecode 
as input, and the output is the memory, storage 
and stack conditions at each step.
'''

import byte2op
from queue import LifoQueue

class Emulator:
	def __init__(self):
		self.fileName = input("Enter the path of the bytecode file: ")
		self.byteCode = self.getContent(self.fileName)
		if not self.byteCode:
			print("Error reading bytecode, please modify and try again.")
		#bytecode to opecode
		self.Opecode = self.byteToOpe(self.byteCode)
		self.stack = LifoQueue()	
		self.memory = LifoQueue()
		self.storage = LifoQueue()
		#run
		self.run(self.stack, self.memory, self.storage)


	def getContent(self, _fileName):
		with open(_fileName, "r") as f:
			return f.read()
		return ""

	def byteToOpe(self, _byteCode):
		pass

	def run(self, _stack, _memory, _storage):
		pass




#unit test
if __name__ == "__main__":
	Emulator()


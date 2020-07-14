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


class staticDataDynamicGenerate:
	def __init__(self, _solContent, _jsonContent):
		self.content = _solContent
		self.json = _jsonContent



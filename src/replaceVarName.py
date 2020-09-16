#!/usr/bin/python
#-*- coding: utf-8 -*-

'''
This python file is part of the layout obfuscation and 
is used to replace variable names with less readable 
strings (currently hash values).
'''

'''
2020/9/15更新：
收窄替换名字的范围，为避免替换Solidity关键字
因为我们进行识别，只替换合约名、函数名、变量名和标识符的名称
2020/9/16更新：
bug重现条件：
１．用户自定义变量与Solidity全局变量重名
２．用户自定义变量与重名的Solidity全局变量同时出现在合约中
导致bug:
Solidity全局bug被重命名
解决办法：
不替换Solidity全局变量的变量名
'''

import os
import json
import sys
import re
import hashlib
import time
from random import random

'''
VAR_FLAG = 1
IDENTIFIER_FLAG = 2
FUNC_FLAG = 3
CONTRACT_FLAG = 4
'''

#不替换变量名的全局变量
BLOCK_FLAG = "block"
MSG_FLAG = "msg"
TX_FLAG = "tx"
ABI_FLAG = "abi"

class replaceVarName:
	def __init__(self, _solContent, _jsonContent):
		self.content = _solContent
		self.json = _jsonContent
		#print(type(self.json))

	def getNames(self, _json):
		varName = set(self._getName(_json, "name", "VariableDeclaration"))
		funcName = set(self._getName(_json, "name", "FunctionDefinition"))
		modifierName = set(self._getName(_json, "name", "ModifierDefinition"))
		contractName = set(self._getName(_json, "name", "ContractDefinition"))
		resultSet = (varName | funcName | modifierName | contractName)	#并集自动去重
		resultSet.discard("") #去空，此处可能存在隐患
		return resultSet

	'''
	def getDictName(self, _dict, _flag):
		for key in _dict:
			if key == "attributes" and _flag == VAR_FLAG:
				if len(_dict[key].get("name")) > 0:
					return _dict[key].get("name")
				else:
					continue
			elif key == "attributes" and _flag == IDENTIFIER_FLAG and \
			     _dict[key].get("referencedDeclaration") != None and \
			     _dict[key].get("referencedDeclaration") > 0 and \
			     _dict[key].get("value") != None and _dict[key].get("type") != "msg":
			     #print(_dict[key].get("referencedDeclaration"))
			     return _dict[key].get("value")
			elif key == "attributes" and _flag == FUNC_FLAG and \
			     _dict[key].get("kind") != None and \
			     _dict[key].get("kind") == "function" :
			     return _dict[key].get("name")
			elif _flag == CONTRACT_FLAG and key == "exportedSymbols":
				return _dict[key].keys()
	'''

	'''
	def _getName(self, _json, _key, _value, _flag):
		queue = [_json]
		result = list()
		while len(queue) > 0:
			data = queue.pop()
			#print(data)
			for key in data:
				if _flag == CONTRACT_FLAG and key == _key:
					namelist = self.getDictName(data, _flag)
					result.extend(namelist)
				#print(key)
				elif key == _key and data[key] == _value:
					name = self.getDictName(data, _flag)
					#print(data)
					#print("****************************")
					result.append(name)
					#result.append(data)
				elif type(data[key]) == dict:
					queue.append(data[key])
				elif type(data[key]) == list:
					for item in data[key]:
						if type(item) == dict:
							queue.append(item)
		return result
	'''

	def _getName(self, _json, _key, _value):
		queue = [_json]
		result = list()
		literalList = list()
		while len(queue) > 0:
			data = queue.pop()
			for key in data:
				if key == _key and data[key] == _value:
					#result.append(data)
					#我们需要的变量名一般都是目标字典下的["attributes"]["name"]
					if data["attributes"].get("name") != None:
						result.append(data["attributes"]["name"])
				elif type(data[key]) == dict:
					queue.append(data[key])
				elif type(data[key]) == list:
					for item in data[key]:
						if type(item) == dict:
							queue.append(item)
		return result


	def doReplace(self, _prob):
		#1. get names of all variables and identifiers
		nameList = self.getNames(self.json)
		'''
		print(nameList)
		print("*" * 40)
		'''
		replacedResult = self.content
		#2. Replace the name of each variable and identifier with a hash value
		for name in nameList:
			if name != None:
				if random() < _prob:
					replacedResult = self.replace1Name(replacedResult, name)
		#3. return result
		return replacedResult

	#(?|X)零宽度负先行断言
	#匹配包含_str但不在右侧包含(.)的语句
	def makeRe(self, _str):
		basePattern = "(\\b)" + _str + "(\\b)"
		if BLOCK_FLAG == _str:
			return basePattern + "(?!(\\.))"
		elif MSG_FLAG == _str:
			return basePattern + "(?!(\\.))"
		elif ABI_FLAG == _str:
			return basePattern + "(?!(\\.))"
		elif TX_FLAG == _str:
			return basePattern + "(?!(\\.))"
		else:
			return basePattern


	'''
	Why do we choose sha1 algorithm? 
	There are two reasons for this:
	1. Although the SHA1 algorithm can be cracked, 
	in our intention, cracking the "variable name" is actually meaningless.
    2. The output of the SHA1 algorithm is a 160-bit hash value, which is 
    the same as Solidity's address type and can interfere with some static 
    code scanning tools.
	'''
	def makeHashName(self, _str):
		sha1 = hashlib.sha1()
		sha1.update(_str.encode("utf-8") + str(time.time()).encode("utf-8"))
		res = sha1.hexdigest()
		return "Ox" + res


	def replace1Name(self, _content, _name):
		#1. construct the re expression
		reExp = self.makeRe(_name)
		#2. generate the replacement
		hashName = self.makeHashName(_name)
		#3. find the name and replace it
		#temp = _content
		return re.sub(reExp, hashName, _content)


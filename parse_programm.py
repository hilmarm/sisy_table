import re

class ParseProgramm(object):

	def __init__(self, prog):
		self.string = prog

	def pri(self, hi):
		print(hi)
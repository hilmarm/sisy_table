import re

class ParseProgramm(object):

	def __init__(self):
		self.string = None
		self.timetable = []

	def read_table(self, filename):
		text_file = open(filename, "r")
		lines = text_file.readlines()

		reg = '\s*(.*)// (.*)\[(.*)\]<br/>'
		for line in lines:
			a = re.match(reg, line)
			if a:
				dj = []
				for item in a.groups():
					dj.append(item)
					# print item
				self.timetable.append(dj)
		text_file.close()
		
	def print_table(self):
		for dj in self.timetable:
			print(dj)
import re
import io


day_time = {'DO':0, 'FR':24, 'SA':48, 'SO':72, 'MO':96, 'DI':120, 'MI':144}

class ParseProgramm(object):

	def __init__(self):
		self.string = None
		self.program = []
		self.timetable = []
		self.len = 0

	def read_table(self, filename):
		text_file = open(filename, "r")
		lines = text_file.readlines()

		reg = '\s*(.*)// (.*)\[(.*)\s(.*)-(.*)\]<br/>'
		for line in lines:
			a = re.match(reg, line)
			if a:
				dj = []
				for item in a.groups():
					dj.append(item)
				self.program.append(dj)
		text_file.close()

		self.len = len(self.program)
		for i in range(self.len):
			self.program[i][3] = int(self.program[i][3]) 
			self.program[i][4] = int(self.program[i][4])

	
	def print_table(self):
		for dj in self.program:
			print(dj)

	def print_table_utf(self):
		for dj in self.timetable:
			for name in dj:
				print(name.decode('utf-8'))

	def parse_timetable(self):
		for i in range(self.len):
			self.program[i].append(self.parse_time([self.program[i][2],
													self.program[i][3],
													self.program[i][4]]))

	def parse_time(self, time):

		if time[2] > time[1]:
			if len(time[0]) == 2:
				return [day_time[time[0]] + time[1], day_time[time[0]] + time[2]]
			else:
				return [day_time[time[0][3:]] + time[1], day_time[time[0][3:]] + time[2]]
				
		else:
			if len(time[0]) == 2:
				return [day_time[time[0]] + time[1], day_time[time[0]] + time[2] + 24]
			else:
				return [day_time[time[0][3:]] + time[1], day_time[time[0][3:]] + time[2] + 24]

    	